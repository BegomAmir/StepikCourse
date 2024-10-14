H = int(input())
if ((H%4==0 and H%100!=0) or H%400==0):
    print('Високосный')
else:
    print('Обычный')
