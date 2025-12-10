#!/usr/bin/env python3

#### Solution 1
# Solution without a function
'''
sequence = "TCTGTTAACCATCCACTTCG"

# Convert string to list
seq_list = list(sequence)

# define empty list for the complement
complement = []

# Iterate over the input sequence and return the complement

for base in seq_list:
    if base == 'T':
        complement.append("A")
    elif base == 'C':
        complement.append("G")
    elif base == "G":
        complement.append("C")
    else:
        complement.append("T")

print(f"Complement: ", complement)
# invert the list
complement.reverse()
print(f"Reverse Complement: ", complement)

# convert back to a list
reverse_complement = "".join(complement)
print(f"Reverse complement : {reverse_complement}")
'''


#### Solution 2
# Solution using a function with long for loop
## Define function
def reverse_complement(sequence):
    complement = []
    for base in sequence:
        if base == 'T':
            complement.append("A")
        elif base == 'C':
            complement.append("G")
        elif base == "G":
            complement.append("C")
        else:
            complement.append("T")
    #invert complement
    complement.reverse()
    # convert back to a string
    reverse_complement = "".join(complement)
    print(f"Sequence : {sequence}")
    print(f"Reverse complement : {reverse_complement}")
    return reverse_complement
# call function on a seqeunce
reverse_complement("TCTGTTAACCATCCACTTCG")


#### Solution 3
### Solution Using a dictionary in a function
# define dictionary
#sequence = "TCTGTTAACCATCCACTTCG"

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

reverse_complement("TCTGTTAACCATCCACTTCG")