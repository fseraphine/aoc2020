#!/usr/bin/python

import re

champs = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}

def estValide(p):
    valide = True
    for e in p.keys():
        valide = valide and verifie(e,p[e])
    print('*** passeport',valide,'\n')
    return valide

def verifie(k,v):
    if k == 'byr':
        test = (int(v) >=1920) and (int(v) <= 2002)
        print(k,v,test)
        return test
    elif k =='iyr':
        test = (int(v) >=2010) and (int(v) <= 2020)
        print(k,v,test)
        return test
    elif k == 'eyr':
        test = (int(v) >=2020) and (int(v) <= 2030)
        print(k,v,test)
        return test
    elif k == 'hgt':
        if m := re.match(r'(\d+)(cm|in)',v):
            n,u = m.groups()
            if u == 'in':
                test = int(n) >= 59  and int(n) <= 76
                print(k,v,test)
                return test
            elif u =='cm':
                test = int(n) >= 150  and int(n) <= 193
                print(k,v,test)
                return test
            else:
                test = False
                print(k,v,test)
                return test
    elif k == 'hcl':
        test = True if re.match(r'\#[0-9a-f]{6}',v) else False
        print(k,v,test)
        return test
    elif k == 'ecl':
        test = v in ['amb','blu','brn','gry','grn','hzl','oth']
        print(k,v,test)
        return test
    elif k == 'pid':
        test = True if re.match(r'(\d{9})',v) else False
        print(k,v,test)
        return test
    elif k == 'cid':
        test = True
        print(k,v,test)
        return True


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
nbok,nbko = 0,0
for p in passports:
    if (champs.symmetric_difference(set(p.keys())) == {'cid'} or champs.symmetric_difference(set(p.keys())) == set()) :
        print('*** passeport',p)
        if estValide(p):
            nbok = nbok +1
        else:
            nbko = nbko +1
    else:
        nbko = nbko +1

print(len(passports),nbok,nbko)