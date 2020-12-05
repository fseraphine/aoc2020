#!/usr/bin/python

champs = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}

i=0
passports = list()
d = dict()
fichier = open('day4_input.txt')
for ligne in fichier:
    if ligne != '\n':
        for e in ligne.split():
            k,v = e.split(':')
            d[k] = v
    else:
        i = i +1
        passports.append(d)
        d = dict()
passports.append(d)
compteur = 0
for p in passports:
    if champs.symmetric_difference(set(p.keys())) == {'cid'} or champs.symmetric_difference(set(p.keys())) == set():
        compteur = compteur +1
print(compteur)