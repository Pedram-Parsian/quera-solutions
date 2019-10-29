inp_list = [input() for _ in range(5)]

found_index = []

for i, item in enumerate(inp_list):
    if 'HAFEZ' in item or 'MOLANA' in item:
        found_index.append(str(i + 1))

if not found_index:
    print('NOT FOUND!')
else:
    print(' '.join(found_index))
