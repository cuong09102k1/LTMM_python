def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)
def is_primitive_root(a, p):
    if gcd(a, p) != 1:
        return False
    values = set(pow(a, i, p) for i in range(1, p))
    return len(values) == p - 1

a = 3
p = 7
print(is_primitive_root(a, p))