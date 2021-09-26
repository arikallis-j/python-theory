import sys
#Рекурсия

#def x(x):
#	x(x)

#Изменение максимальной рекурсии
sys.setrecursionlimit(10000)

def f(x):
	g(1)
def g(x):
	f(1)	
f(1)