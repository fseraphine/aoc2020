#!/usr/bin/python

compteur = 0
i,j=3,1

fichier = open('day3_input.txt')
terrain = fichier.readlines()

nblig = len(terrain)
nbcol = len(terrain[0].strip('\n'))

while j<nblig:
    if terrain[j][i] == '#':
        compteur = compteur +1
    i = (i+3)%nbcol
    j = j+1
print(compteur)