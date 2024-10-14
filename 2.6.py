a = [int(i) for i in input().split()]
n = a[0]
for x in a:
    if n > x:
        n=x
print(n)
