#!/bin/sh
mkdir -p new
find . -maxdepth 1 -name "*.json" -exec ./jq-tidy.sh {} \;
rm -rf new
