n = input()
b = sum(map(int, list(n)))

n = int(n)
i = 1
while i <= b:
    n += 1
    for j in range(2, n):
        if n % j == 0:
            break
    else:
        i += 1

print(n)
