a = 10
b = -10
#функция abs возвращает абсолютное значение числа
abs(a)
def modNum(num):
	mod = abs(num)
	print(mod)
modNum(a)#//10
modNum(b)#//10

a = 0
b = 1
c = ''
d = 'h'
#функция bool возвращает False от 0 или '' и True от всего остального
bool(a)
def boolNum(num):
	boolean = bool(num)
	print(bolean)
boolNum(a)#//False
boolNum(b)#//True
boolNum(c)#//False
boolNum(d)#//True

a = 1
b = 1.5
c = 'h'
#функция выдает полную информацию об объекте
dir(a)
def inf(var):
	inf = dir(var)
	print(inf)
inf(a)
inf(b)
inf(c)

a = 2
b = 3
res = a+b
#функция eval выполняет выражение в кавычках как код python
eval('print(res)')

my_small_program = '''print('бутерброд')
print('с колбасой')'''
#функция exec может выполнять многострочное выражение как код python
exec(my_small_program)

a = 'это тестовая строка'
#функция len определяет количество элементов в массиве 
len(a)
def length(arr):
	length = len(arr)
	print(length)
length(a)

numbers = [5, 4, 10, 30, 22]
i = 0

#функция max возвращает наибольший элемент списка, кортежа или строки
max(numbers)
def maxNum(arr):
	maxNum = max(arr)
	print(maxNum)
maxNum(numbers)

#Функция min возвращает наименьший элемент списка, кортежа или строки
min(numbers)
def minNum(arr):
	minNum = min(arr)
	print(minNum)
minNum(numbers)

#функция range повторяет какое либо действие 
#range(от_какого_элемента,до_какого_элемента,длинна_шага)
range(0,5,1)
def printArr(arr):
	for i in range(0,len(arr),1):
		print(arr[i])
printArr(numbers)
#при отрицательном шаге счет идет назад
range(0,5,-1)
def printArrBack(arr):
	for i in range(len(arr)-1,0,-1):
		print(arr[i])
printArrBack(numbers)

#функция sum складывает элементы массива
sum(numbers)
def sumNum(arr):
	sumNum = sum(arr)
	print(sumNum)
sumNum(numbers)