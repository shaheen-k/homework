#!/usr/bin/env python3
# 61dust.py

import argparse
import sys
import math
import re
import gzip
import mcb185

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase) in place fo low complexity
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library
#command python3 61dust.py --fasta ../Data/chr1.fa --ws 11 --e 0.5


#seq = "GCAAACACCCCACAAAAAAAAAATAGCTACTGAAAT"
ws = 10
e = 3

#setup
parser = argparse.ArgumentParser(description = "Masking low entropy regions")

#arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='needs fasta file')
parser.add_argument('--ws', required=True, type=int,
	metavar='<str>', help='needs window size')
parser.add_argument('--e', required=True, type=float,
	metavar='<str>', help='needs entropy threshold')
	
#switches
parser.add_argument('--lowercase', action='store_true',
	help='lowercase masking option, N-masking default')

#finalization
arg = parser.parse_args()

output = ''
for name, seq in mcb185.read_fasta(arg.fasta):
	seq = seq.upper()
	for i in range(0, len(seq)-arg.ws+1, arg.ws):
		window = seq[i:i+arg.ws]
		window_probs = mcb185.count(window)
		if mcb185.entropy(window_probs) < arg.e:
			if arg.lowercase:
				output += window.lower()
			else:
				output += 'N' * arg.ws
		else:
			output += window
	print(name, output)
