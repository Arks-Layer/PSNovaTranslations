#!/bin/sh
cat "$1" | jq --indent 2 -r -M '.' | cat > "new/$1"
size=$(du -k "new/$1" | cut -f 1)
if [ $size -ne "0" ]; then
    mv "new/$1" "$1"
fi
