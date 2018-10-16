def gcd_recursion(a, b):
    if b == 0:
        return a
    return gcd_recursion(b,a%b)

res = gcd_recursion(0,5)
print(res)

def gcd_iter(a, b):
    while b:
        a = a%b
        a, b = b, a
    return a

