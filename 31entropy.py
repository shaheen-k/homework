#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

#args = [float(x) for x in sys.argv[1:]]

args = []
for x in sys.argv[1:]:
	args.append(float(x))
print(args)

sum1 = 0
for x in args:
	sum1 += x
	

if abs(sum1 - 1) < 0.0001:
	sum = 0 
	for x in args:
		sum += -x * math.log2(x)
	print(f'{(sum):.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""