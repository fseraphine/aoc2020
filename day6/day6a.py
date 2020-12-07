#!/usr/bin/python

fichier = open('day6_input.txt')
groupes_txt = fichier.read().split('\n\n')

compteur = 0
for g in groupes_txt:
    reponses = set()
    for q in g.split('\n'):
        for r in q:
            reponses.add(r)
    print(reponses)
    compteur = compteur + len(reponses)
print('fin',compteur)