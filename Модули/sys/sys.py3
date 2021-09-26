import sys
a = '0'
#функция exit закрывает программу
sys.exit()
#Объект stdin используется для считывания информации с клавиатуры
sys.stdin.readline()
#Одно из различий readline от input, в том, что здесь в (ограничение_длины_строки)
r = sys.stdin.readline(12)
#Объект stdout  используется для вывода информации(аналог print)
sys.stdout.write(a)
w = sys.stdout.write(r)
#Переменная versions содержит информацию о версии python
v = sys.version
print(v)