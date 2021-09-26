import keyword
a = 'if'
b = 'ozwald'
#функция iskeyword проверяет наличие в строке ключевых слов
keyword.iskeyword('string')
def kw(string):
	bl = keyword.iskeyword(string)
	print(bl)
kw(a)#//True
kw(b)#//False

#Переменная kwlist содержит ключевые слова
listKeyWord = keyword.kwlist
print(listKeyWord)