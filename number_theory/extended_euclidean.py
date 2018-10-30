def ext_euclidean(a, b):
    if b == 0:
        return a, 1, 0

    d1, x1, y1 = ext_euclidean(b, a%b)
    d, x, y = d1, y1, x1 - a//b * y1

    return d, x, y

