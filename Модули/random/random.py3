import random
#случайные целые числа в диапазоне
x = random.randint(1,10)
i = 0
print(x)
print(' ')
while i<10:
	x = random.randint(1,10)
	print(x)
	i+=1
k=0
#Угадай число
while k<2:
	num = random.randint(1,10)
	print('Угадай число')
	quess = input()
	i = int(quess)
	if i==num:
		print('Правильно')
	elif i<num:
		print('Загаданное число больше')
	elif i>num:
		print('Загаданное число меньше')
	k+=1
dessert = ['торт','мороженное','конфеты']
#случайный элемент массива
des = random.choice(dessert)
print(des)
#перемешивание элементов массива
random.shuffle(dessert)
print(dessert)