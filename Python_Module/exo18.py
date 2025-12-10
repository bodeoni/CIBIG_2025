#!/usr/bin/env python3

input_path = "files/sequences_especes.tsv"
output_path = "out.out"

# initialise empty dictionary
data = {}

with open(input_path) as f:
    for line in f:
        species = line.strip().split("\t")[0]
        count = line.strip().split("\t")[1]

        # If species not in data, then create it but its value will be a list
        if species not in data:
            data[species] = [] # this is important since dictionaries (sadly) cannot have duplicate values

        # Add corresponding count to the species
        data[species].append(count)

# Sort species alphabetically, this helps to ensure we can exhaust 
# all counts for a specific species before moving to the next
sorted_species = sorted(data.keys())

# Write output
with open(output_path, "w") as out:
    #loop through the sorted species list
    for species in sorted_species:
        out.write(f"# {species}\n")
        # loop through the list which is the value of the corresponding species
        for count in data[species]:
            out.write(f"{count}\n")
        out.write("...............\n")