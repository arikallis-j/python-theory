i=0
#<constructionWhile>
while i==0:
	i+=1
#</constructionWhile>
#цикл while подходит для проверки переменных
while i<10:
	print(i)
	i +=1

j = None
#<constructionFor>	
for j in "hello world":
	print(j*2,end='')
#</constructionFor>
#цикл for_in подходит для проверки массивов

#Операторы в циклах
j = None
for j in "hello world":
	if j == "w":
		#Оператор continue пропускает одну итерацию
		continue
	print(j*2, end='')

j = None
for j in "hello world":
	if j == "w":
		#Оператор break прерывает все итерации
		break
	print(j*2, end='')

j = None
for j in "hello world":
	if j == "a":
		break
#Оператор else  в циклах выполняется, если не выполняется ни один break
else:
	print("a isn't in array")