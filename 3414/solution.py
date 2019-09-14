x1, y1, x2, y2 = [int(x) for x in input().split()]

if y1 == y2:
    print('Horizontal')
elif x1 == x2:
    print('Vertical')
else:
    print('Try again')