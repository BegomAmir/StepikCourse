dnk = input().lower()
i = 0
for g in dnk:
    if g == 'c' or g == 'g':
        i += 1
print(float((i/len(dnk))*100))
