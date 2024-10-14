a=float(input())
b=float(input())
s=input()
if (s == '/') and (b == 0):
    print('Деление на 0!')
elif (s == '/'):
    print(a/b)
if (s == '+'):
    print(a+b)
if (s == '-'):
    print(a-b)
if (s == '*'):
    print(a*b)
if (s == 'mod') and (b == 0):
    print('Деление на 0!')
elif (s == 'mod'):
    print(a%b)
if (s == 'pow'):
    print(a**b)
if (s == 'div') and (b == 0):
    print('Деление на 0!')
elif (s == 'div'):
    print(a//b)


