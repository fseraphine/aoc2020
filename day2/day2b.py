import re

pattern = re.compile('(\d+)-(\d+) (\w): (\w+)\n')

nb=0

f = open('day2_input.txt')
for line in f:
    p1,p2,letter,password = pattern.match(line).groups()
    if (password[int(p1)-1] == letter) ^ (password[int(p2)-1] == letter):
        nb = nb +1
print nb

