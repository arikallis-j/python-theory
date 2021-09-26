x = 1
y = 2
z = x + y
i = 0
print("максимальная точность 38")
n = int(input("точность: "))
while i<n:
	f = (x+y)/y 
	x = y 
	y = z
	z = x + y
	i+=1
print("f = " + str(f))