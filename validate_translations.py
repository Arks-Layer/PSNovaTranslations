#!/usr/bin/env python3
# coding=utf-8
"""
validate_translations.py — PS Nova translation pre-submit checker.

Catches MECHANICAL and COSMETIC problems before submitting. For every ENABLED
translation entry it checks:

  1. Invalid characters   -> chars with no game glyph (e.g. curly quotes ’, dashes)
                             get silently dropped by the inserter. WARNING.
  2. Control-code damage  -> unclosed/unbalanced [ ] break the inserter parser. ERROR.
  3. Length              -> per-type soft limits (40/25/60, auto-resize) = warnings;
                             the ~256-glyph RMD buffer (truncation) = error.
  4. Style               -> leftover Japanese punctuation, with English suggestions.

SCOPE / WHAT THIS DOES NOT DO: it does NOT catch the known cutscene crash. That bug
is content-specific and its trigger is still unidentified (it is NOT length, NOT a
missing font glyph, NOT brackets). Passing this checker means the text is mechanically
clean, not that it is guaranteed crash-free.

Whitespace (space, tab, newline) is renderer-handled, not glyph-based, so it is never
flagged as an invalid character.

Usage:
    python validate_translations.py              # check all files in ./rmd
    python validate_translations.py rmd/Affixes.json   # check one file

No external dependencies (uses only the standard library). Run from the repo root
(the folder that contains the 'rmd' directory and Nova-Tools-master).
"""

import json
import os
import re
import sys
import glob

# --------------------------------------------------------------------------- #
# Control codes. These are stripped before counting visible length, and the
# text between them is considered valid. Order matters: longest/most specific
# patterns first so we don't half-match.
# --------------------------------------------------------------------------- #
CONTROL_CODE_RE = re.compile(
    r"""
      \[n\]                 # newline (alt form)
    | \[b\]                 # color close
    | \[/ruby\]             # ruby close
    | \[ruby[^\]]*\]        # ruby open (contains japanese text)
    | \[a\s+[0-9A-Fa-f]{2}\]            # color open  [a XX]
    | \[e\s+[0-9A-Fa-f]{2}\s+[0-9A-Fa-f]{2}\]  # variable   [e XX XX]
    | \[f\s+[0-9A-Fa-f]{2}\]            # button icon [f XX]
    """,
    re.VERBOSE,
)

# Absolute hard ceiling from the decrypted eboot: RMD buffer is 4096 bits / 16
# bits-per-glyph = 256 glyphs. Anything at or beyond this is guaranteed unsafe.
ABSOLUTE_MAX_GLYPHS = 256

# Japanese punctuation the style guide says to replace with English equivalents.
# Flagged as warnings (mechanical, but a human should pick the right replacement).
# Maps each JP character to the suggested English form.
JP_PUNCTUATION = {
    "？": "?", "！": "!", "（": "(", "）": ")", "…": "...", "ー": "-",
    "＃": "#", "：": ":", "、": ",", "。": ".",
    "「": '"', "」": '"', "『": "'", "』": "'",
    "・": "-", "〜": "~", "～": "~", "％": "%", "／": "/",
    "０": "0", "１": "1", "２": "2", "３": "3", "４": "4",
    "５": "5", "６": "6", "７": "7", "８": "8", "９": "9",
}

# Per-file soft limits, keyed by a substring of the filename. (max_chars_per_line,
# max_lines). These come from the project's empirically-tested renderer regions.
# None means "no specific limit known" -> only the absolute ceiling applies.
# A line over the limit is a WARNING (tiny text); the absolute ceiling is an ERROR.
FILE_LIMITS = {
    "Affixes":          (40, 4),
    "Classes":          (40, 4),
    "Consumable Items": (40, 4),
    "Boost Items":      (40, 4),
    "Materials":        (40, 4),
    "Food":             (40, 4),
    "Weapons":          (40, 4),
    "Shields":          (40, 4),
    "Attachments":      (40, 4),
    "Costumes":         (40, 4),
    "Skills":           (40, 4),
    "Gran Arts":        (40, 4),
    "Techniques":       (40, 4),
    "Status Effects":   (40, 4),
    "Quests":           (25, None),
    "Loading Screens":  (60, 2),
    "Effects":          (20, None),
}
# Story dialogue: soft 110/line, no line cap.
STORY_LINE_LIMIT = 110


def load_allowed_chars(repo_root):
    """Build two character sets from glyphs.json:

      basic   - glyphs in 'BasicCharSet', the global font available in EVERY
                script. These always render (includes symbols like ★ ① → ※).
      anyset  - glyphs that exist in ANY script. A char here but not in `basic`
                might render (depends on the file's script) — treated as a soft
                warning, not a hard error.

    A character in neither set usually isn't in the game and is dropped by the
    inserter -> warning (not a hard error, since the renderer handles some chars
    like whitespace specially).

    Returns (basic, anyset) or (None, None) if glyphs.json can't be found.
    """
    matches = glob.glob(os.path.join(repo_root, "**", "glyphs.json"), recursive=True)
    if not matches:
        print("WARNING: glyphs.json not found — skipping invalid-character checks.\n")
        return None, None
    with open(matches[0], encoding="utf-8") as fh:
        glyphs = json.load(fh)

    basic, anyset = set(), set()
    for entry in glyphs.values():
        text = entry.get("Text", "")
        if len(text) != 1:
            continue
        anyset.add(text)
        for ref in entry.get("References", []):
            if ref.get("Item1") == "BasicCharSet":
                basic.add(text)
                break
    # Whitespace is handled directly by the renderer (cursor advance), NOT via
    # glyph lookup — there are no whitespace glyphs in glyphs.json at all, yet
    # space/newline/tab all render. Per SynthSy: \t = tab, \n = newline. So treat
    # these as always-valid regardless of the font.
    WHITESPACE = {" ", "\n", "\t"}
    basic.update(WHITESPACE)
    anyset.update(WHITESPACE)
    return basic, anyset


def visible_lines(text):
    """Strip control codes, then split into rendered lines.

    Both literal '\\n' and the '[n]' code produce a line break.
    Returns a list of strings (the visible text of each line).
    """
    stripped = CONTROL_CODE_RE.sub("", text)
    stripped = stripped.replace("[n]", "\n")
    return stripped.split("\n")


def file_limit_for(filename):
    base = os.path.basename(filename)
    if "Story" in base and "Summaries" not in base:
        return ("story", STORY_LINE_LIMIT, None)
    for key, (chars, lines) in FILE_LIMITS.items():
        if key in base:
            return ("limit", chars, lines)
    return ("none", None, None)


def check_entry(filename, rmid, entry, basic_chars, any_chars):
    """Return (errors, warnings) lists of human-readable strings for one entry."""
    errors, warnings = [], []
    text = entry.get("Text", "")
    if text == "":
        return errors, warnings  # nothing to validate

    enabled = entry.get("Enabled", False)
    if not enabled:
        # Has text but disabled — it won't ship. Informational only.
        warnings.append("has Text but Enabled is false (won't be used)")
        return errors, warnings

    # --- 1. Control-code bracket integrity ---------------------------------- #
    # Literal brackets are legal (e.g. titles like "[Techniques]"), so we only
    # flag UNBALANCED brackets — an unclosed code is what actually breaks the
    # inserter's parser (it scans to the next ']' and can swallow real text).
    if text.count("[") != text.count("]"):
        errors.append("unbalanced [ ] — unclosed control code or bracket")

    # --- 2. Invalid characters (silently dropped in-game) ------------------- #
    if basic_chars is not None:
        missing, risky = set(), set()
        for ch in CONTROL_CODE_RE.sub("", text).replace("[n]", "\n"):
            if ch in basic_chars:
                continue
            if ch in any_chars:
                risky.add(ch)      # exists, but only in some script's font
            else:
                missing.add(ch)    # not in the game at all
        if missing:
            # NOTE: not a hard error. A char absent from glyphs.json is usually
            # dropped, but some chars (whitespace, control codes) are handled by
            # the renderer directly — so we warn and let a human confirm rather
            # than block. Common real cases: curly quotes ’, en/em dashes.
            shown = " ".join(repr(c) for c in sorted(missing))
            warnings.append("characters not in any game glyph (likely dropped — "
                            "use ASCII equivalents): %s" % shown)
        if risky:
            shown = " ".join(repr(c) for c in sorted(risky))
            warnings.append("characters not in global font, may not render here: %s" % shown)

    # --- 3. Length checks --------------------------------------------------- #
    lines = visible_lines(text)
    total_glyphs = sum(len(ln) for ln in lines)
    if total_glyphs >= ABSOLUTE_MAX_GLYPHS:
        # The RMD string buffer is ~256 glyphs. Past it the encoder trips its
        # overflow flag and the string is truncated / not fully encoded. (This
        # is NOT the known cutscene crash, which is content-specific, not length.)
        errors.append("exceeds the ~%d-glyph RMD buffer (%d) — will be truncated"
                      % (ABSOLUTE_MAX_GLYPHS, total_glyphs))

    kind, max_chars, max_lines = file_limit_for(filename)
    if max_chars is not None:
        for i, ln in enumerate(lines, 1):
            if len(ln) > max_chars:
                tag = "warning" if kind == "story" else "warning"
                warnings.append("line %d is %d chars (limit %d): %r"
                                % (i, len(ln), max_chars, ln))
    if max_lines is not None and len(lines) > max_lines:
        warnings.append("%d lines (limit %d) — may overflow its box"
                        % (len(lines), max_lines))

    # --- 4. Leftover Japanese punctuation (style guide) --------------------- #
    # Most of these also render fine, so they're warnings, not errors — but they
    # should be swapped for the English form per the project style guide.
    jp_found = {ch for ch in text if ch in JP_PUNCTUATION}
    if jp_found:
        suggestions = ", ".join("%r->%r" % (ch, JP_PUNCTUATION[ch])
                                for ch in sorted(jp_found))
        warnings.append("Japanese punctuation, replace with English: %s" % suggestions)

    return errors, warnings


def check_file(path, basic_chars, any_chars):
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as e:
        print("  [JSON ERROR] %s: %s" % (path, e))
        return 1, 0
    except OSError as e:
        print("  [READ ERROR] %s: %s" % (path, e))
        return 1, 0

    n_err, n_warn = 0, 0
    for rmid, entry in data.items():
        if not isinstance(entry, dict):
            continue
        errors, warnings = check_entry(path, rmid, entry, basic_chars, any_chars)
        for msg in errors:
            print("  ERROR  %s:%s  %s" % (os.path.basename(path), rmid, msg))
            n_err += 1
        for msg in warnings:
            print("  warn   %s:%s  %s" % (os.path.basename(path), rmid, msg))
            n_warn += 1
    return n_err, n_warn


def main():
    # Windows consoles are often cp1252; flagged bad characters can be anything.
    # Force UTF-8 output (replacing anything still unprintable) so we never crash
    # while reporting a problem.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    repo_root = os.path.dirname(os.path.abspath(__file__))
    basic_chars, any_chars = load_allowed_chars(repo_root)

    args = sys.argv[1:]
    if args:
        files = args
    else:
        files = sorted(glob.glob(os.path.join(repo_root, "rmd", "*.json")))

    if not files:
        sys.exit("No JSON files found. Run from the repo root, or pass a file path.")

    total_err, total_warn = 0, 0
    for path in files:
        e, w = check_file(path, basic_chars, any_chars)
        total_err += e
        total_warn += w

    print("\n" + "=" * 50)
    print("Checked %d file(s): %d error(s), %d warning(s)"
          % (len(files), total_err, total_warn))
    if total_err:
        print("Fix the ERRORs before submitting — broken control codes or buffer overruns.")
        sys.exit(1)
    print("No mechanical errors found. (Note: does not detect the cutscene crash.)")


if __name__ == "__main__":
    main()
