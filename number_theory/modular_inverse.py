from extended_euclidean import ext_euclidean

def modular_invers_iter(num, mod):
    r1, r2 = mod, num
    t1, t2 = 0, 1

    while(r2 > 0):
        q = r1//r2

        r = r1 - q* r2
        r1, r2 = r2, r

        t = t1 - q * t2
        t1, t2 = t2, t
    
    if r1 == 1:
        if t1 < 0:
            return t1 + mod
        else:
            return t1

print(modular_invers_iter(23,100))

def modular_invers(num, mod):
    res = ext_euclidean(num, mod)
    if res[0] == 1:
        if res[1] < 0:
            return res[1] + mod
        else:
            return res[1]
    else:
        return None
    
print(modular_invers(23,100))
