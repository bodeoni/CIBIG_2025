#!/usr/bin/env python3
# Extract fasta headers from a multi fasta file
# using sysagv to take in arguements

import sys
print(sys.argv)

# Check that the correct number of arguments were passed
if len(sys.argv) != 3:
    sys.exit("Please provide the path of the file and the output file")
# check that a fasta file was provided
with open(sys.argv[1], "r") as input:
    if not input.read().startswith(">"):
        sys.exit("Please provide a properly formatted fasta file that starts with >.")

# Define arguments
path = sys.argv[1] # input path
out = sys.argv[2] # output path

output  = open(out, "w") # open (create) the output file
with open(path, "r") as data: # open the input file
    for line in data:
        if ">" in line:
            print(line.strip()) # Print the current line into the output file
            output.write(line) # write the current line into the output file

print(f"The headers have been saved to {out}")
output.close() # close the output file