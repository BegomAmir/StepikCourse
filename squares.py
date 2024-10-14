s=input()
if s == 'треугольник':
    a=float(input())
    b=float(input())
    c=float(input())
    p=(a+b+c)/2
    print(((p*(p-a)*(p-b)*(p-c))**(1/2)))
if s == 'прямоугольник':
    a=float(input())
    b=float(input())
    print(a*b)
if s == 'круг':
    r=float(input())
    print(3.14*(r**2))




