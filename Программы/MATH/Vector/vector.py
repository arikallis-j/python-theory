class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.r = (x*x + y*y + z*z)**0.5
a = Vector(1,2,0)
b = Vector(-1,2,0)
def vsum(a,b):
    x = a.x + b.x
    y = a.y + b.y
    z = a.z + b.z
    c = Vector(x,y,z)
    return c
def vdiff(a,b):
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    c = Vector(x,y,z)
    return c
def vmultn(a,n):
    x = a.x * n
    y = a.y * n
    z = a.z * n
    c = Vector(x,y,z)
    return c
def vmults(a,b):
    c = a.x*b.x + a.y*b.y
    return c
def vmultv(a,b):
    x = a.y*b.z - a.z*b.y
    y = a.z*b.x - a.x*b.z
    z = a.x*b.y - a.y*b.x
    c = Vector(x,y,z)
    return c
def vprint(r):
    print(r.x)
    print(r.y)
    print(r.z)
    print(r.r)
r = vsum(a,b)
vprint(r)
r = vdiff(a,b)
vprint(r)
r = vmultn(a,2)
vprint(r)
r = vmults(a,b)
print(r)
r = vmultv(a,b)
vprint(r)
