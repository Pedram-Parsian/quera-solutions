num_a = int(input())
total_list = input().split()

num_b = int(input())
total_list.extend(input().split())

num_c = int(input())
total_list.extend(input().split())

print(7 - len(set(total_list)))

