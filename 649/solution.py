a = int(input())
b = int(input())

primes = []

for i in range(a+1, b):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(str(i))

print(','.join(primes))
