import random

circle_of_fifths = ['C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G'];

random.shuffle(circle_of_fifths)

print('On each fret, say the note\'s chord name (therefore think of degree)')

for i in circle_of_fifths:
    print(i)
    input()

exit()