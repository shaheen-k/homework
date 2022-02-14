#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math



#args = [float(x) for x in sys.argv[1:]]
#print(args)

args = []
for x in sys.argv[1:]:
	args.append(float(x))
print(args)

print('Count:', len(args))

args.sort()
print(args)
print('Minimum:', float(args[1]))

print('Maximum:', float(args[len(args)-1]))

sum = 0
for x in args:
	sum += x
mean = sum/len(args)
print('Mean:', f'{(mean):.3f}')

sum1 = 0
for x in args:
	sum1 += (x-mean) ** 2
std = (sum1/len(args)) ** (1/2)
print('Std. dev:', f'{(std):.3f}')

print('Median:', f'{(args[len(args)//2]):.3f}')


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
