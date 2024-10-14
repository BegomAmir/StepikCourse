x = int(input())
p = x % 10
q = (x%100)//10
if p == 0 or (5 <= p <= 9) or q == 1:
    print(str(x), 'программистов')
elif p == 1:
    print(str(x),'программист')
else:
    print(str(x),'программиста')
