import numpy as n
R = 3
k = [2, 3, 2, 1]
L = 0.0001

x1 = 1
x2 = 1
DB = [[1,1,0,0],[1,0,0,1],[0,0,0,0],[0,1,0,1]]


def f(x):
	return 1/(1 + n.exp(x))

def df(x):
	return x*(1 - x)

###инициализация

#инициализация весов

def initNullWeit():
	x = []
	for i in range(R):
		y = []
		for j in range(R):
			z = []
			for k in range(R):
				z.append(0)
			y.append(z)
		x.append(y)
	return x


def initWeit(r):
	x = initNullWeit()
	for i in range(R):
		y = x[i]
		for j in range(r[i]):
			z = y[j]
			for k in range(r[i+1]):
				z.insert(k,n.random.random())
				z.pop(k+1)
			y.insert(j,z)
			y.pop(j+1)
		x.insert(i,y)
		x.pop(i+1)
	return x

#инициализация значений

def initNullValu():
	x = []
	for i in range(R+1):
		y = []
		for j in range(R):
			y.append(0)
		x.append(y)
	return x

def initValu(r,A,W):
	x = initNullValu()
	for i in range(R+1):
		y = x[i]
		if i==0:
			for j in range(r[0]):
				z = A[j]
				y.insert(j,z)
				y.pop(j+1)
		else:
			for j in range(r[i]):
				z = 0
				for k in range(R):
					z+= x[0][k]*W[i-1][k][j]
				z = f(z)
				y.insert(j,z)
				y.pop(j+1)

		x.insert(i,y)
		x.pop(i+1)
	return x



WEIT = initWeit(k)

VALU = initValu(k,DB[0],WEIT)

y = VALU[R][0]


d = DB[0][R]

print(WEIT)
print(VALU)
print(y)

###ошибки



BELT = initNullValu()



def update():
	e = y - d
	print(e)
	BELT[R][0] =  e*df(y)
	for i in range(R):
		for j in range(R):
			b = 0
			for k in range(R):
				b += BELT[-i-1][k]*WEIT[-i-1][j][k]
			BELT[-i-2][j] = b
			for k in range(R):
				WEIT[-i-1][j][k] -= L*b*df(VALU[-i-1][j])





for p in range(100):
	update()
	t = DB[n.random.randint(1,3)]
	VALU = initValu(k,t,WEIT)
	y = VALU[R][0]
	d = t[R]


VALU = initValu(k,[0,1,0,1],WEIT)
y = VALU[R][0]
print(y)
