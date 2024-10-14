a=int(input())
b=int(input())
c=int(input())
if a>=b and b>=c:
    print(a, '\n', c, '\n', b)
elif a>=c and c>=b:
    print(a, '\n', b, '\n', c)
elif b>=a and a>=c:
    print(b, '\n', c, '\n', a)
elif b>=c and c>=a:
    print(b, '\n', a, '\n', c)
elif c>=a and a>=b:
    print(c, '\n', b, '\n', a)
else:
    print(c, '\n', a, '\n', b)

