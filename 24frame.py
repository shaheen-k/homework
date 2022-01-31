#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'
'''
i=0
for position in range(len(dna)):
	 letter = dna[position]
	 frame = i
	 print(position, frame, letter)
	 i += 1
	 if i > 2: 
	 	i = 0
'''
i=0
for position in range(len(dna)):
	 letter = dna[position]
	 frame = i
	 print(position, frame, letter)
	 i += 1
	 if i > 2: 
	 	i = 0
		

	

"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
