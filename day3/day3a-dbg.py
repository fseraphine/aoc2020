#!/usr/bin/python

compteur = 0
i,j = 3,1
terrain = []
fichier = open('day3_input.txt')
for l in fichier:
    terrain.append(fichier.readline().strip('\n'))

nblig = len(terrain)
nbcol = len(terrain[0])
print('nblig : %s / nbcol : %s' % (nblig,nbcol))

for f in terrain:
    print(f)

while j<nblig:
    #print(i,j,terrain[j][i],compteur)
    if terrain[j][i] == '#':
        compteur = compteur +1
        print(terrain[j][0:i-1]+'X'+terrain[j][i+1:nbcol-1])
    else:
        print(terrain[j][0:i-1]+'O'+terrain[j][i+1:nbcol-1])
    i = (i+3)%nbcol
    j = j+1
print(compteur)