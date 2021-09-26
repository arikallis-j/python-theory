#<construction>
var = 1
#</construction>

#Для объявления переменной в python нужно назвать её имя и значение
#Тип переменной в python указывать не нужно
varInteger = 23
#Тип переменной Целые числа(Integer)
varFloat = 23.25
#Тип переменной Дробные числа(Float)
varString = "23"
#Тип переменной Строки(String)
varBoolean = True
#Тип переменной Логическое значение(Boolean)
varNone = None
#Переменная не содержит значения(без типа,или None)

#в текстовую переменную можно подставить число(в саму строку)
#для этого нужно поставить в строке метку %s
#после поставить после текстовой переменной знак % и имя переменной с числом
myscore = 1000
message = "Мой счет: %s очков"
print(message % myscore);

var = input("Enter number: ")
#Функция input является функцией ввода в python
#Тип переменной из input это string 
print(var)
#В python  есть набор функций для изменения типа переменной
int(var)
#переменная получает тип Integer
float(var)
#переменная получает тип Float
str(var)
#переменная получает тип String
bool(var)
#переменная получает тип Bolean
del var
#функция del удаляет переменную
num_1 = int( input("Enter first num: ") )
num_2 = int( input("Enter second num: ") )
res = num_1 + num_2
print("Result is "+ str(res))
res = res * 5
res *= 5
#Это две эквивалентные записи
varString *= 5
print(varString) #ДвТриДвТриДвТриДвТриДвТри

#Lokal_Global variable
#Локальные переменные действуют в пределах функций,циклов и т.д.
def test():
	global a
	a = 1
	b = 2
test()
print(a)#//1
#print(b)#//NameError