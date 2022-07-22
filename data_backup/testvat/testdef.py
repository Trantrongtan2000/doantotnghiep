def add(a, b):
    x = a + b
    return x

c=add(1, 2)
d=add(5, 6)
print(c)
print(d)

def catanh(a):
    w=int(a)
    tt=w/3
    cc=w+10
    pp=w-12
    return (tt,cc,pp)
y,n,m=catanh(2)
print(catanh(2))
print(y)
print(n)
print(m)

def catanh(fillter,img):
    width= int(fillter.shape[1])
    A = img[:, 0:int(width / 3)]
    B = img[:, int(width / 3):int(width / 3 * 2)]
    RH = img[:, int(width / 3 * 2):int(width)]
    return (A,B,RH)
