import  itertools
inp = input()

g_count = inp.count('G')
y_count = inp.count('Y')
r_count = inp.count('R')

if r_count >= 3 or (r_count >= 2 and y_count >= 2) or g_count == 0:
    print('nakhor lite')
else:
    print('rahat baash')