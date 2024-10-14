a = [int(i) for i in input().split()]
d = 0
for i in range(len(a)):
    if len(a) == 1:
        d = a[i]
    elif i == len(a) - 1:
        d = a[i-1] + a[0]
    else:
        d = a[i - 1] + a[i + 1]
    print(d, end=' ')

