a = [int(i) for i in input().split()]
a.sort()
d = 1
for i in range(len(a) - 1):
    if a[i] == a[-1]:
        print(a[i])
        break
    elif a[i] == a[i + 1]:
        d += 1
    elif a[i] != a[i + 1] and d >= 2:
        print(a[i], end=' ')
        d = 1





