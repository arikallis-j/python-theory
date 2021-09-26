class Matrix:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.array = []
        for i in range(x):
            self.array.insert(i,[])
            for j in range(y):
                self.array[i].insert(j,0)
    def mInOne(self,x,y,arg):
        self.array[x-1][y-1] = arg
    def mInAll(self,array):
        self.array = array
    def mOutOne(self,x,y):
        return self.array[x-1][y-1]
    def mOutAll(self):
        return self.array
#операции над двумя матрицами
def mWMat(a,d,b):
    x = a.x
    y = a.y
    if b.x>a.x:
        x = b.x
    if b.y>a.y:
        y = b.y
    r = Matrix(x,y)
    for i in range(x):
        for j in range(y):
            if a.mOutOne(i,j)== None:
                r.mInOne(i,j,b.moutOne(i,j))
            elif b.moutOne(i,j)==None:
                r.minOne(i,j,a.moutOne(i,j))
            elif d=="+":
                r.minOne(i,j,a.moutOne(i,j) + b.moutOne(i,j))
            elif d=="-":
                r.minOne(i,j,a.moutOne(i,j) - b.moutOne(i,j))
            elif d=="*":
                r.minOne(i,j,a.moutOne(i,j) * b.moutOne(i,j))
            elif d=="/" and b.moutOne(i,j)!=0:
                r.minOne(i,j,a.moutOne(i,j) / b.moutOne(i,j))
            else:
                r.minOne(i,j,a.moutOne(i,j))
    return r
#операции над матрицей и числом
def mWNum (a,d,k):
    r = Matrix (a.x,a.y)
    for i in range(a.x):
        for j in range(a.y):
            if d== "+":
                r.minOne(i,j,a.moutOne(i,j)+k)
            elif d== "-":
                r.minOne(i,j,a.moutOne(i,j)-k)
            elif d== "*":
                r.minOne(i,j,a.moutOne(i,j)*k)
            elif d== "/":
                r.minOne(i,j,a.moutOne(i,j)/k)
            else:
                r.minOne(i,j,a.moutOne(i,j))
    return r
#отображение матрицы
def mprint(a):
    l = 5 #сдвиг слева
    line = " "*l
    for i in range(a.x):
        for j in range(a.y):
            line += str(a.moutOne(i+1,j+1)) + " "
        line += "\n" + " "*l
    return ("\n"+line+"\n")

a = Matrix(3,4)
b = Matrix(4,3)
a.minOne(1,1,1)
b.minOne(2,1,1)
r = mwithmat(a,"+",b)
r = mwithmat(a,"-",b)
r = mwithnum(r,"+",1)
print(r.moutAll())
print(mprint(r))

#python matrix.py
