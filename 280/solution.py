inp = map(int, [input() for _ in range(3)])

square = sorted([i ** 2 for i in inp], reverse=True)

if square[0] == sum(square[1:]):
    print('YES')
else:
    print('NO')
