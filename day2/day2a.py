#!/usr/bin/python

# import re

pattern = re.compile('(\d+)-(\d+) (\w): (\w+)\n')

nb=0

f = open('day2_input.txt')
for line in f:
    min,max,letter,password = pattern.match(line).groups()
    password  = ''.join(sorted(password))
    if (letter*int(min) in password) and (letter*(int(max)+1) not in password):
        nb = nb +1
print nb

