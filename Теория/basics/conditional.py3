x=1
y=0
result = None
var = input("Enter var ")

#<construction>
if x>0:
	result = True
elif x==0: 
	result = None 
else :
	result = False
#</construction>

#<mayConstruction_1>
if x>0:
	if x!=0:
		if x>1:
		else:
			x+=1
	else:
		x+=2
else:
#</mayConstruction_1>

#<mayConstruction_2>
result = True if var!="test" else False
#</mayConstruction_1>

if 1: 
	print("True")
#данное условие всегда верно, так как 1=True
if 0:
	print("True")
#данное условие всегда неверно, так как 0=False
if 1:
	print("True\n")
	#табуляция обязательна, так как print("All is okey") не находится в условии
print("All is okey")

if x==y:
	result = True
#true, если x равно y
if x>y:
	result = True
#true, если x больше y
if x<y:
	result = True
#true, если x меньше y
if x>=y:
	result = True
#true, если x больше или равно y
if x<=y:
	result = True
#true, если x меньше или равно y
if x!=y:
	result = True
#true, если x не равно y

#Для рассмотрения работы оператора is создадим класс AlwaysEqual который всегда возвращает True
class AlwaysEqual(object):
    def __eq__(self, other):
        return True
#Создаем объект этого класса
instance = AlwaysEqual()
#Сравнивая его с чем либо всегда возвращается True
print (instance == 42)  # True
#Но при проверке,//ЯВЛЯЕТСЯ ЛИ instance 42//Не может возвращаться True
#Так как instance это ОБЪЕКТ, а не ЧИСЛО 42
print (instance is 42)  # False
#Так же при сравнении его с Классом AlwaysEqual будет False 
print (instance is AlwaysEqual())  # False
#Но при сравнении instance и класс AlwaysEqual имеют одни и теже свойства и значит они равны
print (instance == AlwaysEqual())  # True
#И выражение типа //a is a// будет всегда True
print (instance is instance)  # True


login = input("Enter login ")
password = input("Enter password ")
if password == "test1234":
	print("Hello," + login)