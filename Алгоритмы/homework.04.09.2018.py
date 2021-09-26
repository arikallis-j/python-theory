n = int(input("Введите число: "))
def mult_str(char,num):
	j = 1
	str = char
	while j!=num:
		str = str + char
		j+=1
		if j==num:
			break
	return str
i = 2
print (mult_str("* ",n))
while i!=n:
	print("* "+mult_str(" ",2*(n-2))+"*")
	i+=1
print (mult_str("* ",n))