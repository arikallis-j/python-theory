password = output("password: ")
pln = password.length
text = output("text: ")
tln = text.length
text_code = ""
while i<tln:
	text_code += password[j]
	if j==i:
		j = 0
	else:
		j+=1
	i+=1
print(text_code)