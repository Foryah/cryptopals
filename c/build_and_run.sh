#!/bin/zsh
if [ -z $1 ]; then
    echo "Usage $0 <file_name> ";
    return;
fi

gcc $1
./a.out
rm a.out
