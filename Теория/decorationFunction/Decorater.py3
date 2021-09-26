#Обертка, декорация функции
def decoreter(func):
	def wrapper():
		print('код до выполнения')
		func()
		print('код после выполнения')
	return wrapper
#Декорируемая функция
def show ():
	print('All is okey')
#Декорация 
show = decoreter(show)
show()
#или
@decoreter #таких декораторов может быть несколько, и каждый оборачивает следующий(построчно)
def show1 ():
	print('All is okey, too')
show1()