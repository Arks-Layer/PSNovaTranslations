[3]: https://github.com/Arks-Layer/PSO2JPTranslations/blob/master/resources/rightmeow.png

<p align="center">
  <img src="https://github.com/Arks-Layer/PSNovaTranslations/blob/master/resources/Phantasy-Star-Nova-Logo.png" alt="PS Nova Logo"/>
</p>

[Build status](https://api.travis-ci.org/Arks-Layer/PSNovaTranslations.svg?branch=master)

# PS: Nova Translations

Welcome to the PS: Nova Translations Github Repository.

This repository is dedicated to translating PS: Nova game texts from Japanese to English. We hope our disclosing of game texts and opening this repository will pave a quicker way for non-Japanese speaking ARKS to enjoy the game in their native languages in the future.

<i>While we appreciate the efforts of those who don't speak Japanese (through Google translate and the like), we would like for only those who have a grasp of the Japanese language to submit edits to those. ありがとう～ (*＾▽＾)／</i>

### Getting Started/Helping Out
A full guide on how to get started is [available here](https://github.com/Arks-Layer/PSNovaTranslations/wiki/How-to-contribute)

## Editing Process

Please put your translation in the "Text" field like so:
  
```
  "310040": {
    "OriginalText": "ポストアタック",
    "Text": "Post Attack",
    "Enabled": false
  },
```

Then, change the false to true, so it ends up like this:

```
  "310040": {
    "OriginalText": "ポストアタック",
    "Text": "Post Attack",
    "Enabled": true
  },
```

Please note that there may be "weird" things in the text! For example, `\n`. These will be detailed below.

We welcome your contributions in the form of pull requests. You may create new issues to discuss the translations with other translators. Please note that issues not related to translation may be deleted without notice.

## Don't know Japanese but still want to contribute?

If you don't understand Japanese, but still want to help out, you can look over the translated lines and make sure all grammar and spelling is correct. (US English, please!)

## Entry Sizes

Here is a list of sizes a region will accept before it starts to resize. These should be kept as close to as possible so that text doesn't appear too small due to the automatic resizing.

```
Affix Descriptions - 40 Characters, 4 Lines
Class Descriptions - 40 Characters, 4 Lines
Item Descriptions - 40 Characters, 4 Lines
Skill/GA/Technique Descriptions - 40 Characters, 4 Lines

Quest Names - 25 Characters
Loading Screen - 60 Characters, 2 Lines

Effects - 20 Characters
          15-18 Characters if it's a numeric effect to make room for the maximum potential number/percentage
```

## Message (RMD) System

The following is some basic information about RMD, the format the game uses to store and handle its string entries and string table.

### ID Ranges

You can refer to NovaParse's [Export JSON](https://github.com/Arks-Layer/Nova-Tools/blob/master/NovaParse/Export.json) file for a reference of RMD ID ranges. If you find any that seem incorrect or that need investigating, feel free to point them out in an issue or in the Discord channel.

### Text Regions

Nova's GUI system uses the concept of regions to align and contain UI and text elements. The system is smart enough to attempt to automatically fit controls inside of its containing region. This can be taken advantage of to fit in larger amounts of text than is immediately obvious. Keep in mind though that there is no restriction to this rule, so care must be taken to make sure that you do not stretch text vertically or horizontally to the point where individual glyphs become unreadable.

### Control Codes

These control codes are used to do various things, such as change the text color or insert images.

#### Basic

```
\n - Newline
```

#### Ruby

Ruby is a special control code with special handling. Ruby control codes place the specified text on top of the surrounding text. It begins with `[ruby ` and then is proceeded with the text to place over top of the surrounding text and then a closing `]`. Use `[/ruby]` to close the Ruby block. An example:

```
msg_100000010010013.rmd:
お願い……わたしの[ruby ほし]惑星[/ruby]を……助けて。
```

will show up as:

```
               ほし
お願い……わたしの惑星を……助けて。
```

#### Colors

These control codes will change the surrounding text's color. You must prefix the text you wish to color with a color control code, then, after the text, append the color close control code.

```
[a 03] - Orange
[a 06] - Blue
[a 07] - Yellow
[b] - Color Close
```

#### Variables

There are 4 variable control codes. The meaning of these variables will change depending on the context of the message they are contained within. Therefore, <b>they are very specific and should only be used within the proper messages to prevent potential issues occurring in the game!</b>

```
[e 00 00] - Variable 1
[e 01 00] - Variable 2
[e 02 00] - Variable 3
[e 03 00] - Variable 4
```

#### Images

These control codes can be used to insert button and icon images into the text.

```
[f 01] - X
[f 02] - Circle
[f 03] - Square
[f 04] - Triangle
[f 07] - L
[f 08] - R
[f 09] - Start
[f 0a] - Select
[f 0b] - Left Thumbstick
[f 0c] - Right Thumbstick
[f 1b] - Circle
[f 1c] - X
[f 64] - PS Button
[f 66] - Right Thumbstick
[f 67] - Left Thumbstick
[f 68] - Left Thumbstick + X
[f 69] - Left Thumbstick + Triangle
[f 6a] - Left Thumbstick + Square
[f 6b] - Left Thumbstick + L
[f 6c] - Left Thumbstick + R
[f 6d] - L1
[f 6e] - R1
[f 6f] - L2
[f 70] - R2
[f 71] - L3
[f 72] - R3
[f 73] - Square
[f 74] - Triangle
[f 75] - X
[f 76] - Circle
[f 77] - Left Thumbstick + Circle
[f 78] - L
[f 79] - R
[f 7a] - D-Pad Left
[f 7b] - D-Pad Right
[f 7c] - D-Pad Up
[f 7d] - D-Pad Down
[f 7e] - Select
[f 7f] - Gran Icon
[f 80] - Unknown Icon
[f 9c] - Unknown Icon
```

#### Miscellanous Information
<ul class="task-list">
<li><p><strong>DO NOT CHANGE</strong> the line's ID or any of the first values in quotes (OriginalText, Text, or Enabled). Only edit the text in the second part, in quotes!</p></li>
<li><p>To use quotes inside strings, use \"". For example: "ARKS stands for \""ARTIFICIAL RELICT TO KEEP SPECIES\"". Isn't that neat?"</p></li>
<li><p>「」 『』 Single and double quotation marks should be replaced by English quotes '"'.</p>
<li><p>Replace the Japanese numbers and punctuation ?/！/（ ）/…/ー/＃/：... with their English counterparts.</p>
</ul>

#### Capitalization
Not all words are created equal - Certain ones should be capitalized. The following items should have every world in them capatizalized (with exceptions to this rule listed below them):
```
Window Titles
Job Subtitles
Story Titles
Ratio/Checkboxes
Buttons
Abbreviations
```

Some words should not be capitalized (unless they are the first word):
```- Articles: a, an, the
- Conjunctions: and, as, but, for, if, nor, once, or, so, than, that, till, when, yet
- Prepositions: at, by, down, for, from, in, into, like, near, of, off, on, onto, over, past, to, upon, with
'。' Japanese period: English titles and sub-titles should not end with a period.
```
So if there was a mission named "searching for comrades", we would label it as "Searching for Comrades". If someone was talking about going to search for comrades literally, we would format it as "I will keep looking, searching for my comrades!".

For translations that refer to names (classes, items, enemies, etc), please treat them as proper nouns and use uppercase for the first letter of each word. </p>

<ul class="task-list">
<li>Example: Gran piece (Fire) -&gt; Gran Piece (Fire), Coral dragon blood -&gt; Coral Dragon Blood</li>
</ul>
</li>
