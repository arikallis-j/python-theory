inp = None
lis = []
while inp!="ok":
	inp = input("заполните массив ")
	lis.append(inp)
del lis[len(lis)-1]
lis = list(map(int,lis))