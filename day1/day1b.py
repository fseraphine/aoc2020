#!/usr/bin/python

expenses = []
fichier = open('day1_input.txt')
for l in fichier:
    expenses.append(int(l))

expenses.sort()

for a in expenses:
    for b in expenses:
        for c in expenses:
            if a+b+c == 2020:
                print("%s + %s +%s = %s ; produit = %s" % (a,b,c,a+b+c,a*b*c))
                sys.exit(0)
