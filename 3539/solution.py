n = int(input())

while len(str(n)) != 1:
    n = sum(int(x) for x in str(n))

print(n)