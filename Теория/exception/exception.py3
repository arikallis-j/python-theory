#Исключения нужны для устранения ошибок при работе программы
#print(10/0)#ZeroDivisionError:
#print(int('qwerty'))#ValueError:
#print('2'+1)#TypeError:

x = int(input("Первое число "))
y = int(input("Второе число "))
#Исключения в python
try:
	#в try указывается то, где используется исключение
	res = x/y
except ZeroDivisionError:
	#в except указывается тип ошибки и решение
	print("Ошибка.На ноль делить нельзя")
	y = int(input("Второе число "))
	while y == 0:
		y = int(input("Второе число "))
		res = x/y
print(res)
try:
	z = int(input("Выведите число"))
except ValueError :
	print("Ошибка.Вы вели не число")
	z = 0
print(z)


try:
	x = int(input("Выведите число"))
except ValueError :
	print("Ошибка.Вы вели не число")
	x = 0
try:
	y = int(input("Выведите число"))
except ValueError :
	print("Ошибка.Вы вели не число")
	y = 0
try:
	res = x/y
except ZeroDivisionError:
	print("Ошибка.На ноль делить нельзя")
	res = 0
finally:
	print("Завершено 100%")