l = ['a','b','c']
word= ""
a=0
while a<3:
	word += l[a]
	b=0
	while b<3:
		if l[b]!=l[a]:
			word+= l[b]
			c = 0
			while c<3:
				if l[c]!=l[a] or l[c]!=l[b]:
					word+=l[c]
					print(word)
					word = ""
					c+=1
				else:
					c+=1
					continue
			b+=1
		else:
			b+=1
			continue
	a+=1
		
		
		 