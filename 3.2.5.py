d = {7:[3,2,1], 8:[8,6,-1]}
def update_dictionary(d , key, value):
    if key in d:
        d[key]+=[value]
    elif key not in d:
        if 2 * key not in d:
            d[2*key]=[value]
        elif 2 * key in d:
            d[2*key]+=[value]
    return d
print(update_dictionary(d,4,4))

 