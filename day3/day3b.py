#!/usr/bin/python

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

fichier = open('day3_input.txt')
terrain = fichier.readlines()

nblig = len(terrain)
nbcol = len(terrain[0].strip('\n'))

total = 1
for s in slopes:
    i,j,compteur = 0,0,0
    i = (i+s[0])%nbcol
    j = j+s[1]
    while j<nblig:
        if terrain[j][i] == '#':
            compteur = compteur +1
        i = (i+s[0])%nbcol
        j = j+s[1]
    print(s,compteur)
    total = total * compteur
print(total)