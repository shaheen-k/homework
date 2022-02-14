#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_length = int(sys.argv[3])


coverage = []
for i in range(genome_size):
	coverage.append(0)

for i in range(read_num):
	r = random.randint(0, genome_size - read_length)
	for j in range(read_length):
		coverage[r+j] += 1
#print(coverage[read_length: -read_length])

total = 0 
for count in coverage[read_length: -read_length]:
	total += count
avg = total/(genome_size - (2*read_length))

coverage.sort()
#print(coverage[read_length: -read_length])
print(coverage[read_length], coverage[-read_length], avg)

'''
a = "abcdefghijk"
print(a)
print(a[1:])
print(a[:-1])
for letter in a:
	print(letter)
'''

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
