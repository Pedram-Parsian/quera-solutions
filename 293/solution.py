a = int(input())
b = int(input())

if a > b:
    a, b = b, a

for i in range(a, b+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
