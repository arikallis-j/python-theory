import copy
class Animal:
	def __init__(self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color
harry = Animal('гиппогриф', 6, 'розовый')
#функция copy возвращает (новой	переменной) характеристики обЪекта в скобках
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)

harry = Animal('гиппогриф', 6, 'розовый')
carrie = Animal('химера', 4, 'в зеленый горошек')
billy = Animal('богл', 0, 'узорчатый')
#так же эта функция может возвращать(новому списку) характеристики списка в скобках
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)

#!НО! при изменении характеристик копии изменияется и оригинал(и обратно)
#При копировании списка с объектами списки пересоставляются из одних и тех же объектов
my_animals[0].species = 'вампир'
print(my_animals[0].species)
print(more_animals[0].species)	
#И при изменении состава списка копия и оригинал не зависимы
sally = Animal('сфинкс', 4, 'песочный')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

#функция deepcopy создает копии всех объектов списка
more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'дракон'
print(my_animals[0].species)
print(more_animals[0].species)