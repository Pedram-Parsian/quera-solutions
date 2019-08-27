result_list = []
while True:
    m, n = (int(x) for x in input().split())
    if m == n == 0:
        break
    customer_key = [int(_) for _ in input().split()]
    trash_box_keys = []
    for i in range(n):
        trash_box_keys.append([int(_) for _ in input().split()])
    counter = 0
    for item in trash_box_keys:
        for a, b in zip(item, customer_key):
            if not a <= b:
                break
        else:
            counter += 1
    result_list.append(str(counter))
print('\n'.join(result_list))
