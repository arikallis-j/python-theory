from decimal import Decimal
#derivative - производная
def der(f,x):
	dx = 10**(-5)
	t = 1 + dx
	df = f(x+dx/2) - f(x-dx/2)
	d = df/dx
	d = Decimal(str(d))
	d = d.quantize(Decimal(str(t)))
	d = float(d)
	return d

#integral
def intg(f,a,b):
	#параметры вычислений
	dx = 10**(-8)
	t = 1 + dx
	m = 1
	i = 0
	#направление интегрирования
	if (b-a)<0:
		c = a
		a = b
		b = c
		m = -1
	elif (a-b)==0:
		return i

	n = int(abs(a-b)/dx)
	for k in range(n):
		i += f(a+k*dx+dx/2)*dx
	i = Decimal(str(i))
	i = i.quantize(Decimal(str(t)))
	i = m*float(i)
	return i

def e(x):
	exp = 2.718281828459045
	return exp**(x)
def y(x):
	return (1/(2*x**(1/2)))

print(intg(y,0,4))


