import pickle
game_data = {
	'позиция-игрока' : 'С23 В45',
	'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
	'рюкзак' : ['веревка', 'молоток', 'яблоко'],
	'деньги' : 158.50
}
save_file = open('save.dat', 'wb')
#функция dump записывает значение указанного в () массива в указанный в () файл
pickle.dump(game_data, save_file)
save_file.close()

load_file = open('save.dat', 'rb')
#функция load открывает значение указанного в () файла
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)