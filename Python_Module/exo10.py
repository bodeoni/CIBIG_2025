#!/usr/bin/env python3

import sys
print(sys.argv)

# Check that the correct number of arguments were passed
if len(sys.argv) != 2:
        sys.exit("Please provide the path of the file")

# Define arguments
path = sys.argv[1]

with open(path, "r") as data:
    for line in data:
        if ">" in line:
            continue
        print(line.strip().lower()) #remove \n

## using startswith()
'''
with open(path, "r") as data:
    for line in data:
        if line.startswith(">"):
            continue
        print(line.lower())
'''