a = [int(i) for i in input().split()]
b = int(input())
n = []
c = a.count(b)
for i in range(len(a)):
    if c == 0:
        print('Отсутствует')
        break
    elif a[i] == b:
        n.append(i)
    elif a[i] != b:
        continue
print(*n)
