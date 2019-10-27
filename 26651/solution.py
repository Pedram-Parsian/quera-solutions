n = int(input())
a_i_list = list(map(int, input().split()))
b_i_list = list(map(int, input().split()))

total = 0

for a_i, b_i in zip(a_i_list, b_i_list):
    total += b_i * a_i

print(total)
