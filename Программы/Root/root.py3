from math import sqrt 
a = int(input("input a "))
print(" ")
b = int(input("input b "))
print(" ")
c = int(input("input c "))
print(" ")
print(str(a)+"x^2 + "+str(b)+"x + "+str(c))
if a!=0:
	d=b*b-4*a*c
if d>=0:
	x1 = (-b+sqrt(d)/2*a)
	x2 = (-b-sqrt(d)/2*a)
	print('x1='+str(x1))
	print('x2='+str(x2))
else:
	print('нет вещественных корней')