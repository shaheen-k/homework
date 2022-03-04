#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

#File Import
seq = ""
found_origin = False
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line.startswith("ORIGIN"): 
			found_origin = True
		if found_origin:
			words = line.split() #convert to words 
			seq += "".join(words[1:]) #join w/ no characters btwn
			
#genome = 'attatgaattcattagaattcattatcg'

#Restriction Enzyme Cut

pattern = sys.argv[2]

start = 0 
for match in re.finditer(pattern, seq):
	print(len(seq[start:match.start()+2]))
	start = match.start()+2
print(len(seq[start:]))
		
												

"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
289?
"""
