#Prokaryotic Gene Finding

#sample 

import random
import sys
import re
import math
import argparse

# setup
parser = argparse.ArgumentParser(description='Prokaryotic Gene Finding:How many genes fit your definition?.')

# required arguments
parser.add_argument('--genome', required=True, type=int,
	metavar='<str>', help='needs genome length')
parser.add_argument('--size', required=True, type=int,
	metavar='<int>', help='needs orf size threshold to define a gene')
parser.add_argument('--hist', required=True, type=int,
	metavar='<int>', help='needs histogram bin length to count orf frequencies')

#finalization
arg = parser.parse_args()

dna = ''
for i in range(arg.genome):
	dna += random.choice('ACTG')
	
#dna = "GCAATGACGATGTCATGACGGCACCCTAATC"

#find ORF (starts - ATG; ends - TAA, TAG, TGA)

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

def orfs(seq):
	for frame in range(3):
		pro = ''
		for i in range(frame, len(seq), 3):
			codon = seq[i:i+3]
			if codon in gcode: pro += gcode[codon]
			else: pro += 'X'
		#print(pro)
		porfs = pro.split('*')
		for porf in porfs:
			#orf_found = False
			if 'M' in porf:
				for i in range(len(porf)):
					if porf[i] == 'M': 
						yield porf[i:]
						#orf_found = True
						break
				#if orf_found: break

count = 0
size = 100	
block = [0]*20
for orf in orfs(dna):
	if len(orf) > arg.size: count += 1
	block[(len(orf))//arg.hist] += 1
print("'possible' genes:", count)
print("histogram:", block)
		
		

	
