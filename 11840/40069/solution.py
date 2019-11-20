w = int(input())
n = int(input())

dimensions = []
area = 0
for _ in range(n):
    x, y = map(int, input().split())
    area += (x * y)

print(int(area/w))
