#!/usr/bin/python

import itertools

expenses = [int(x) for x in open('day1_input.txt').readlines()]

for i,j in itertools.combinations_with_replacement(expenses,2):
    if i+j == 2020:
        print(i*j)
