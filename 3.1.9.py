l = [int(i) for i in input().split()]
def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 1:
            del l[i]
        elif l[i] % 2 == 0:
            j = l[i] // 2
            del l[i]
            l.insert(i, j)
    return l
print(modify_list(l))




