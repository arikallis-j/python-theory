class Person:
	name = "Ivan"
	age = 18
	def set(self, name, age):
		self.name = name
		self.age = age
	
vlad = Person()
vlad.name = 'Влад'
print(vlad.name)

ivan = Person()
ivan.age = 40
print(ivan.age)

igor = Person()
igor.set('Игорь',25)
print(igor.name)
print(igor.age)