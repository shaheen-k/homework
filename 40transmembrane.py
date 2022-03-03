#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

#KD calculation
#signal peptide (moves every 8 AA for first 30AA, then every 11AA until *)



#KDcalc 

def kdcalc(aaSeq):
	KDsum = 0
	for aa in aaSeq:
		if aa == 'I': KDsum += 4.5
		if aa == 'V': KDsum += 4.2
		if aa == 'L': KDsum += 3.8 
		if aa == 'F': KDsum += 2.8 
		if aa == 'C': KDsum += 2.5 
		if aa == 'M': KDsum += 1.9 
		if aa == 'A': KDsum += 1.8
		if aa == 'G': KDsum += -0.4  
		if aa == 'T': KDsum += -0.7 
		if aa == 'S': KDsum += -0.8 
		if aa == 'W': KDsum += -0.9 
		if aa == 'Y': KDsum += -1.3 
		if aa == 'P': KDsum += -1.6 
		if aa == 'H': KDsum += -3.2 
		if aa == 'E': KDsum += -3.5 
		if aa == 'Q': KDsum += -3.5 
		if aa == 'D': KDsum += -3.5 
		if aa == 'N': KDsum += -3.5 
		if aa == 'K': KDsum += -3.9 
		if aa == 'R': KDsum += -4.5 
	return KDsum/len(aaSeq)
	
#alpha-helix

def a_helix(seq, w, t):
	for i in range(len(seq) - w + 1):
		peptide = seq[i:i+w]
		if 'P' in peptide: continue 
		if kdcalc(peptide) >= t: return True
	return False 

#print( a_helix(seq, 8, 2.5))

w = 8 
h = 11
seq = ""
names = []
sequences = []
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line[0] == ">":
			words = line.split()
			name = words[0][1:]
			names.append(name)
			if len(seq) == 0: continue
			sequences.append(seq)
			seq = ""
		else:
			seq += line.rstrip()

sequences.append(seq)

for name, seq in zip(names, sequences):
	if not a_helix(seq[0:30], 8, 2.5) and not a_helix(seq[30:], 11, 2.0):
		print(name)
		
			



			
			
			

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
