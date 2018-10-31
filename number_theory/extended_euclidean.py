def ext_euclidean(a, b):
    if b == 0:
        return a, 1, 0

    d1, x1, y1 = ext_euclidean(b, a%b)
    d, x, y = d1, y1, x1 - a//b * y1

    return d, x, y


def ext_iter(a,b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while(r2 > 0):
        q = r1//r2

        r = r1%r2
        r1, r2 = r2, r

        s = s1 - q * s2
        s1, s2 = s2, s

        t = t1 - q * t2
        t1 ,t2  = t2, t

    return r1,s1,t1
