#!/usr/bin/python

expenses = []
fichier = open('day1_input.txt')
for l in fichier:
	expenses.append(int(l))

expenses.sort()

for a in expenses:
	for b in expenses:
		if a+b == 2020:
			print("%s + %s = %s ; produit = %s" % (a,b,a+b,a*b))
			sys.exit(0)
