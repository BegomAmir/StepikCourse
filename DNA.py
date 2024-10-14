genome = input().lower()
d = 1
for i in range(len(genome) - 1):
    if genome[i] == genome[i + 1]:
        d += 1
    else:
        print(genome[i], end='')
        print(d, end='')
        d = 1
print(genome[-1], end='')
print(d, end='')
