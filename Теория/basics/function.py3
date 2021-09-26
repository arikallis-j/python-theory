#<constructionFunction>
def function(x,y):
	return x+y
#</constructionFunction>

#ключевое слово return выводит значение из функции
def function_1(x,y):
	res = x + y
	return res
print(function_1(23,12))
#одну функцию можно вызывать через другую
def func(x):
	def add(a):
		return x + a
	return add
test = func(100)
print(test(200))

#ключевое слово pass не выводит из функции ничего
def function_2():
	x = 34
	y = 43
	pass
#функция может содержать параметры по умолчанию
#они должны указываться в конце
def function_3(r,w,y=2):
	res = r + w
	res*= y
	return
print(function_3(2,4,3))

#функции можно использовать для создания кортежей
def function_4(*args):
	return args
print(function_4('sd',4,3.5))

#функции можно использовать для создания словарей
def function_5(**args):
	return args
print(function_5(one='sd',two=4,three=3.5))

#анонимные функции lambda пишутся в одну строчку и не требуют return
add = lambda x,y: x*y
print(add(2,5))
#lambda также можно вызывать самостоятельно, указывая после функции в() значение аргументов
print((lambda x,y: x*y)(2,5))
#c помощью lambda можно так же создавать кортежи и словари
fun = lambda *args: args
print(fun(23,44.55,'qw'))