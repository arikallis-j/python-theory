inp = None
lis = []
while inp!="ok":
	inp = input("заполните массив ")
	lis.append(inp)
del lis[len(lis)-1]
lis = list(map(int,lis))
n = 0
while n!=(len(lis)-1):
	i = 0
	for i in range(len(lis)):
		a=lis[i]
		if lis[i] == lis[(len(lis)-1)]:
			print(a)
		else:
			i+=1
			b=lis[i]
			i=i-1
			if a>b:
				x=a
				a=b
				b=x
				lis[i]=a
				i+=1
				lis[i]=b
				i=i-1
				print(a)
				i+=1
			else:
				print(a)
				i+=1
	print("_______________")
	n+=1
print(lis)
