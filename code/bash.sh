#!/bin/bash

echo "Gen plaintext and caesarKey and Rail-fenceKey"
python gen.py > input.txt

echo "Run code"
python main.py < input.txt > output.txt
