#!/bin/sh
python coverage.py | fgrep --invert-match -e "000.0%:0FILE" | sed 's/\.json//' | sort --numeric-sort --reverse
