#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
cdna = ''
for i in range(len(dna)):
	if dna[i] == 'A': cdna += 'T'
	elif dna[i] == 'C': cdna += 'G'
	elif dna[i] == 'T': cdna += 'A'
	elif dna[i] == 'G': cdna += 'C'
print(cdna[len(cdna)::-1])  #splice [start:end(1 larger): pattern]

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
