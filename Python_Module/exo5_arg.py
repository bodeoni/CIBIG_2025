#!/usr/bin/env python3

import sys
print(sys.argv)

# Check that the correct number of arguments were passed
if len(sys.argv) != 2:
        sys.exit("Please provide a sequence")

# Define arguments
seq = sys.argv[1]

def reverse_complement(sequence):
    # define dictionary of pairs
    pairs = {"A":"T", "C":"G", "G":"C", "T":"A"}
    rev = []
    for base in sequence:
        rev.append(pairs[base])
    rev.reverse()
    result = "".join(rev)
    print(f"Sequence : {sequence}")
    print(f"Reverse complement : {result}")
    return reverse_complement

reverse_complement(seq)
