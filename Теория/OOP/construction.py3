class Person:
	name = "NoName"
	age = 18
	#конструктор __init__ позволяет передавать все свойства объекта в скобках
	def __init__(self, name, age):
		self.name = name
		self.age = age
igor = Person('Игорь', 25)
print(igor.name + ' ' + str(igor.age))

class  person:
	name = "Ivan"
	age = 18
	__id = 0
	def set(self, name, age):
		self.name = name
		self.age = age
class Student(person):
	course = 1
	#переопределение функции set
	def set(self, name, age, course):
		self.name = name
		self.age = age
		self.course = course
igor = Student()
print(igor.name+' '+str(igor.age)+' '+str(igor.course))