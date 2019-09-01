from collections import Counter

n = int(input())
marker_list = [int(_) for _ in input().split()]

print(sorted(Counter(marker_list).items(), key=lambda x: (x[1], x[0]))[0][0])

