a = int(input())
b = []
for i in range(1, a + 1 ):
        for j in range(1, i + 1):
                b.append(i)
print(*b[:a])
