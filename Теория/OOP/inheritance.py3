class Person:
	name = "Ivan"
	age = 18
	#Инкапсуляция
	#Свойство id не наследуется
	__id = 0
	def set(self, name, age):
		self.name = name
		self.age = age
#класс Student унаследовал все свойства класса Person, кроме id
class Student(Person):
	course = 1
igor = Student()
igor.course = 2
igor.set('Игорь',25)
print(igor.name+' '+str(igor.age)+' '+str(igor.course))
print(igor._Person__id)
#print(igor.id)#ошибка инкапсуляции
#Полиморфизм
print(2+2)
print('2'+'2')
#Один и тот же метод (+) работает по разному в разных классах