a,b = int(input()), int(input())
a += -a%3
b -= b%3
print((a+b)/2)