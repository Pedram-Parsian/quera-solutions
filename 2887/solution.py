from functools import reduce
from math import gcd

n = int(input())
n_list = [int(x) for x in input().split()]
n_list_gcd = reduce(gcd, n_list)
print(sum(list(map(lambda x: int(x/n_list_gcd), n_list))))
