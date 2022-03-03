#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
# Use a dictionary to count the letters #DONT DO THAT!
# Sorting the amino acids by frequency is optional



def AA(letter):
	m = 0 
	total = 0
	with open(sys.argv[1]) as fp:
		for line in fp.readlines():
			if line[0] != ">":
				seq = line.rstrip()
				for aa in seq:
					if aa != "*": total += 1
					if aa == letter: m += 1 
	print(letter, m, m/total)

AA("W")
AA("C")
AA("H")
AA("M")
AA("Y")
AA("Q")
AA("F")
AA("N")
AA("P")
AA("T")
AA("R")
AA("I")
AA("D")
AA("G")
AA("A")
AA("K")
AA("E")
AA("V")
AA("L")
AA("S")


"""
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

