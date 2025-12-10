#!/usr/bin/env python3

# Count how many times an Amino acid appears in a sequence
import time
sequence = "AGWPSGGASAGLAILWGASAIMPGALW"

# Option 1
import time

start_time = time.perf_counter()
# empty dictionary
result = {}
# loop to iterate through every value of the string and count it.
for i in sequence:
    count  = sequence.count(i)
    # Check if the Amino acid already exists in the dictionary
    if i in result.keys():
        continue
    else:
        result[i] = count
print(result)
end_time = time.perf_counter()
print(end_time - start_time)

# Option 2 (More efficient)
start_time = time.perf_counter()
# empty dictionary
result = {}
# loop to iterate through every value of the string and count it.
for i in sequence:
    # Check if the Amino acid already exists in the dictionary, otherwise don't count
    if i in result.keys():
        continue
    else:
        count = sequence.count(i)
        result[i] = count
print(result)
end_time = time.perf_counter()
print(end_time - start_time)