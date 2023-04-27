def tinh_mod(b1,n):
    # return = b1 mod(n)
    rb = b1 // n
    t = b1 - rb*n
    return t

#chon 2 so p,q:
print("nhap hai so nguyen to lon khac nhau(form: 4k + 3): ")
while True:
    k1 = int(input('nhap k1 cua p(4*K1+3 = p):'))
    p = 4*k1+3
    print('p =', p)
    count = 0
    for i in range(1, p + 1):
        if p % i == 0:
            count += 1
    if count != 2:
        print('nhap lai')
    else:
        break

while True:
    k2 = int(input('nhap k2 cua q(4*K1+3 = q):'))
    q = 4 * k2 + 3
    print('p =', p)
    count = 0
    for i in range(1, q + 1):
        if q % i == 0:
            count += 1
    if count != 2 or q == p:
        print('nhap lai')
    else:
        break
n = p*q

#cac khoa:
print('khoa cong khai(n):',n)
print('khoa bi mat(q,n)',q,',',n)

#nhap ban tin ro:
t2 = []
t2 = input("nhap plaintext: ")
text = []
for i in range(0,len(t2)):
    text.append(ord(t2[i]))
print(text)

#ma hoa: C = M^2 (mod n)
ma = []
for i in range(0,len(text)):
    ma.append(tinh_mod(text[i]**2,n))

print('ma hoa:', ma)
'''''''''''''''
#giai ma: M = C^1/2 (mod n)
tin = []
for i in range(0,len(text)):
    m = tinh_mod(ma[i] ** 0.5, n)
    print(m)
    tin.append(m)

gm1 = "".join(tin)
print('giai ma:',gm1)
'''''''''''''''