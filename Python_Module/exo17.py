#!/usr/bin/env python3
# print the organism with the largest genome

species_dict = {'Escherichia coli':3.6,'Homo sapiens':3200,'Saccharomyces cerevisae':12,'Arabidopsis thaliana':125}

# loop through the key value pair
for key, value in species_dict.items():
    # check if value is the same as the max of all values
    if value==max(species_dict.values()):
        # print the corresponding key
        print(f"The organism with the largest genome is:{key}")

