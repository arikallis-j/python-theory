import turtle
#создание объекта черепашка
t = turtle.Pen()
t.forward(50)#вперед на px
t.left(90)#влево на °
t.right(90)#вправо на °
#t.left(90)==t.right(270)

#reset - очищение холста с возвращением черепашки
t.reset()
i= 0
while i <4 :
	t.forward(50)
	t.left(90)
	i+=1
#clear - очищение холста без возврата черепашки
t.clear()
#
t.backward(50)#назад на px
t.up()#поднять перо
t.left(90)
t.forward(100)
t.right(90)
t.down()#опустить перо
t.forward(100)