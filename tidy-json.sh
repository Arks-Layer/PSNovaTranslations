#!/bin/sh
mkdir -p new/rmd
find rmd -maxdepth 1 -name "*.json" -exec ./jq-tidy.sh {} \;
rm -rf new
