t = int(input())

results = []

for _ in range(t):
    x, y = map(int, input().split())
    if y not in (x, x-2):
        results.append(-1)
        continue
    if x % 2 == 0:
        results.append(x+y)
    else:
        results.append(x + y - 1)

print(*results, sep='\n')
