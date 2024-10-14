s = [input().lower().split()]
d={}
for i in s:
    if s[i] not in d:
        d[i]=[1]
    if s[i] in d:
        d[i] = d[i+1]