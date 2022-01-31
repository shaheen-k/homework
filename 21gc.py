#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gc = 0
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'G': gc += 1
	elif nt == 'C': gc += 1
fgc = gc/len(dna)
print('%.2f' % (fgc))       #Method1
print('{:.2f}'.format(fgc)) #Method2
print(f'{(fgc):.2f}')       #Method3


"""
python3 21gc.py
0.42
0.42
0.42
"""
