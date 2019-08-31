nums = []
while True:
    x = input()
    if x == '0':
        break
    nums.append(x)
for item in reversed(nums):
    print(item)