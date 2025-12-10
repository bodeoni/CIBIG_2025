#!/usr/bin/env python3

sequence = "TCTGTTAACCATCCACTTCGATG"

# solution 1
if sequence.find("ATG") == -1:
    print("No")
else:
    print("Yes")


#print(sequence.find("ATG"))

# solution 2
if "ATG" in sequence:
    print("Yes")
else:
    print("No")


for i in range(0, len(sequence)):
    j = i +3
    codon = sequence[i:j]
    if codon != "ATG":
        break
    elif codon =="ATG":
        print(f"ATG found at position {i}")
    else:
        print("No")

### another solution
sequence = "ATGTCTGTTAACCATCCACTTCGATG"
found = False
for i in range(0, len(sequence)):
    j = i + 3
    codon = sequence[i:j]
    if codon == "ATG":
        print(f"ATG found at position {i+1}")
        found = True
if not found:
    print("No")



