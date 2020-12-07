#!/usr/bin/python

from functools import reduce

fichier = open('day6_input.txt')
groupes_txt = fichier.read().split('\n\n')

compteur = 0
for g in groupes_txt:
    reponses = list()
    i = 0
    for q in g.split('\n'):
        reponses.append(set())
        for r in q:
            reponses[i].add(r)
        print('reponses',i,reponses[i])
        i = i+1
    tous = reduce(lambda a,b: a.intersection(b), reponses )
    print('tous',tous,'=>',len(tous))
    compteur = compteur + len(tous)
    print('compteur',compteur)
print('fin',compteur)