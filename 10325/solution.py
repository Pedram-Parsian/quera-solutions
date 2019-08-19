r, c = (int(x) for x in input().split())


if 1 <= c <= 10:
    direction = 'Right'
    b = c
else:
    direction = 'Left'
    b = 21 - c


a = 11 - r


print(direction, a, b)