word = [ch for ch in input()]

remove_index = 1

for i, ch in enumerate(word):
    if i == 0:
        print(''.join(word))
        continue
    word[:i] = word[i] * i
    print(''.join(word))
