def Fuc(mass):
    prov = True
    count = 0
    while prov:
        tmpper = list(mass[0])[count]
        for word in mass:
            if tmpper != list(word)[count]:
                prov = False
        count+=1
    if count == 0:
        return ""
    else:
        return mass[0][:count-1]

mass = ["flower","flow","floight", "flol"]
print(Fuc(mass))