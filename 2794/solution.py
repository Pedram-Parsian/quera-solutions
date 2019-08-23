from collections import Counter

p1_x, p1_y = input().split()
p2_x, p2_y = input().split()
p3_x, p3_y = input().split()

x_list = [p1_x, p2_x, p3_x]
y_list = [p1_y, p2_y, p3_y]

x_target = Counter(x_list).most_common()[-1][0]
y_target = Counter(y_list).most_common()[-1][0]

print(x_target, y_target)