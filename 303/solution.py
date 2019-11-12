def ShowFibNth(n, n_1):
    print(n)
    if not n_1 == 1:
        ShowFibNth(n_1-n, n)


n = int(input())
n_1 = int(input())
ShowFibNth(n, n_1)

