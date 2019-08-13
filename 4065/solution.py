a, b, l = [int(x) for x in input().split()]
print(sum((a if _%2 == 0 else b) for _ in range(l)))
