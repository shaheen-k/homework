#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

shared_birthdays = 0
days = 365
people = 25
trials = 10000

calendar = []
for i in range(days):
	calendar.append(0)
	
for j in range(trials):
	for i in range(people):
		r = random.randint(0, days-1)
		calendar[r] += 1
	#print(calendar)
	for birthday in calendar:
		if birthday >= 2:
			shared_birthdays += 1
avg = (shared_birthdays)/(trials)
print(avg)


"""
python3 33birthday.py
0.571
"""

