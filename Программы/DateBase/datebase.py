def dateRead(date):
	list = []
	DATE = open(date,'r')
	eval("list.append(DATE.read())")
	DATE.close()
	return list[0]
	
def dateWrite(date, inputing):
	list = []
	DATE = open(date,'r')
	eval("list.append(DATE.read())")
	DATE.close()
	list[0]  += inputing
	DATE = open(date,'w')
	DATE.write(list[0])
	DATE.close()
	
def dateDelite(date):
	DATE = open(date,'w')
	DATE.write("")
	DATE.close()

dateWrite("DATE.txt","hi6")
text = dateRead("DATE.txt")
print(text)
dateDelite("DATE.txt")