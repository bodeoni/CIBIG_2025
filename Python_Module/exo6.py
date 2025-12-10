#!/usr/bin/env python3

sequence = "TCTGTTAACCATCCACTTCG"
'''
# OPTION 1 - Using count function
seq = list(sequence)
print("A -", seq.count("A"))
print("T -", seq.count("T"))
print("G -", seq.count("G"))
print("C -", seq.count("C"))

# OPTION 2 -Using loops
num_A = 0
num_T = 0
num_G = 0
num_C = 0

for base in seq:
    if base == "A":
        num_A = num_A + 1
    elif base == "T":
        num_T = num_T + 1
    elif base == "C":
        num_C = num_C + 1
    else:
        num_G = num_G +1

print("The number of A -", num_A)
print("The number of T -", num_T)
print("The number of G -" , num_G)
print("The number of C -", num_C)
'''
## OPTION 3- Using a function which allows the user to retrieve the individual counts and percentages

def base_composition(sequence):
    # Convert all sequences to uppercase
    seqeunce = sequence.upper()
    # Convert seqeunce to list
    seq = list(seqeunce)
    # Count the bases
    num_A = seq.count("A")
    num_T = seq.count("T")
    num_G = seq.count("G")
    num_C = seq.count("C")

    # Calculate percentage
    per_A = num_A/len(seq)
    per_T = num_T/len(seq)
    per_G = num_G/len(seq)
    per_C = num_C/len(seq)

    #Calculate GC percentage
    GC = (num_G + num_C) / len(seqeunce)

    print(f"Base Composition: A:{num_A}({per_A}%), T:{num_T}({per_T}%), G:{num_G}({per_G}%), C:{num_C}({per_C}%)")
    print(f"GC:{GC}")
    return {
    "Count": {"A": num_A, "T": num_T, "G": num_G, "C": num_C},
    "Percentage": {"A": per_A, "T": per_T, "G": per_G, "C": per_C},
    "GC": GC}


result = base_composition(sequence)
print(result["Count"]["A"])
