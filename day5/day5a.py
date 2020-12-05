#!/usr/bin/python

from math import floor

def rang(str):
    rangees = [0,127]
    print(str)
    for c in str:
        if c =='F':
            rangees[1] = floor((rangees[0]+rangees[1])/2)
        elif c == 'B':
            rangees[0] = floor((rangees[0]+rangees[1])/2)+1
    if str[-1] == 'F':
        return rangees[0]
    elif str[-1] == 'B':
        return rangees[1]

def colo(str):
    rangees = [0,7]
    print(str)
    for c in str:
        if c =='L':
            rangees[1] = floor((rangees[0]+rangees[1])/2)
        elif c == 'R':
            rangees[0] = floor((rangees[0]+rangees[1])/2)+1
    if str[-1] == 'L':
        return rangees[0]
    elif str[-1] == 'R':
        return rangees[1]    

boarding_passes = list()
fichier = open('day5_input.txt')
for l in fichier:
    boarding_passes.append(l.strip('\n'))

maxid = 0
for b in boarding_passes:
    r = rang(b[0:7])
    c = colo(b[7:10])
    #print(b,r,c,r*8+c)
    maxid=max(r*8+c,maxid)
print('fin',maxid)
