#свести цвета к булевским переменным
#черные все те же буквы у фигур, только другого регистра(р - белый, Р- черный)
"""
cd "C:/Users/Таня/Desktop/Кодирование/Python"
python x.py3
"""
"""
color = True
if color is white
color = False
if color is black
"""

xList = ('a','b','c','d','e','f','g','h')
yList = ('1','2','3','4','5','6','7','8')
def linearSearch(li, x):
    i = 0
    length = len(li)
    while i<length and x != li[i]:
        i+=1
    if i<length:
    	return i
    else :
    	print('isn\'t element in Array')
class figure(object):
	c = None #color
	f = 'x' #figure
	x = xList[0]
	y = yList[0]
	def __init__(self,c,f,x,y):
		self.c = c
		self.f = f
		self.x = x
		self.y = y

class Empty(figure):
	f = 'x'
	c = None
	x = None
	y = None
	def __init__(self):
		pass
class Pawn(figure):
	f = 'p'
	def __init__(self,c,x,y):
		self.c= c
		self.x = x
		self.y = y
class Rook(figure):
	f = 'r'
	def __init__(self,c,x,y):
		self.c = c
		self.x = x
		self.y = y
class Knigh(figure):
	f = 'k'
	def __init__(self,c,x,y):
		self.c = c
		self.x = x
		self.y = y
class Bishop(figure):
	f = 'b'
	def __init__(self,c,x,y):
		self.c = c
		self.x = x
		self.y = y
class Queen(figure):
	f = 'q'
	def __init__(self,c,x,y):
		self.c = c
		self.x = x
		self.y = y
class King(figure):
	f = 'K'
	def __init__(self,c,x,y):
		self.c = c
		self.x = x
		self.y = y

pw1 = Pawn(w,'a','2')
pw2 = Pawn(w,'b','2')
pw3 = Pawn(w,'c','2')
pw4 = Pawn(w,'d','2')
pw5 = Pawn(w,'e','2')
pw6 = Pawn(w,'f','2')
pw7 = Pawn(w,'g','2')
pw8 = Pawn(w,'h','2')

rw1 = Rook(w,'a','1')
kw1 = Knigh(w,'b','1')
bw1 = Bishop(w,'c','1')
kw = King(w,'e','1')
qw = Queen(w,'d','1')
bw2 = Bishop(w,'f','1')
kw2 = Knigh(w,'g','1')
rw2 = Rook(w,'h','1')

pb1 = Pawn(b,'h','7')
pb2 = Pawn(b,'g','7')
pb3 = Pawn(b,'f','7')
pb4 = Pawn(b,'e','7')
pb5 = Pawn(b,'d','7')
pb6 = Pawn(b,'c','7')
pb7 = Pawn(b,'b','7')
pb8 = Pawn(b,'a','7')

rb1 = Rook(b,'h','8')
kb1 = Knigh(b,'g','8')
bb1 = Bishop(b,'f','8')
kb = King(b,'e','8')
qb = Queen(b,'d','8')
bb2 = Bishop(b,'c','8')
kb2 = Knigh(b,'b','8')
rb2 = Rook(b,'a','8')

listFigure = [rw1,kw1,bw1,qw,kw,bw2,kw2,rw2,pw1,pw2,pw3,pw4,pw5,pw6,pw7,pw8,rb1,kb1,bb1,qb,kb,bb2,kb2,rb2,pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8]

class cage(object):
	figure = Empty()
	x = xList[0]
	y = yList[0]
	def __init__(self, figure,x,y):
		self.figure = figure
		self.x = x
		self.y = y

a1 = cage(Empty,'a','1')
b1 = cage(Empty,'b','1')
c1 = cage(Empty,'c','1')
d1 = cage(Empty,'d','1')
e1 = cage(Empty,'e','1')
f1 = cage(Empty,'f','1')
g1 = cage(Empty,'g','1')
h1 = cage(Empty,'h','1')

a2 = cage(Empty,'a','2')
b2 = cage(Empty,'b','2')
c2 = cage(Empty,'c','2')
d2 = cage(Empty,'d','2')
e2 = cage(Empty,'e','2')
f2 = cage(Empty,'f','2')
g2 = cage(Empty,'g','2')
h2 = cage(Empty,'h','2')

a3 = cage(Empty,'a','3')
b3 = cage(Empty,'b','3')
c3 = cage(Empty,'c','3')
d3 = cage(Empty,'d','3')
e3 = cage(Empty,'e','3')
f3 = cage(Empty,'f','3')
g3 = cage(Empty,'g','3')
h3 = cage(Empty,'h','3')

a4 = cage(Empty,'a','4')
b4 = cage(Empty,'b','4')
c4 = cage(Empty,'c','4')
d4 = cage(Empty,'d','4')
e4 = cage(Empty,'e','4')
f4 = cage(Empty,'f','4')
g4 = cage(Empty,'g','4')
h4 = cage(Empty,'h','4')

a5 = cage(Empty,'a','5')
b5 = cage(Empty,'b','5')
c5 = cage(Empty,'c','5')
d5 = cage(Empty,'d','5')
e5 = cage(Empty,'e','5')
f5 = cage(Empty,'f','5')
g5 = cage(Empty,'g','5')
h5 = cage(Empty,'h','5')

a6 = cage(Empty,'a','6')
b6 = cage(Empty,'b','6')
c6 = cage(Empty,'c','6')
d6 = cage(Empty,'d','6')
e6 = cage(Empty,'e','6')
f6 = cage(Empty,'f','6')
g6 = cage(Empty,'g','6')
h6 = cage(Empty,'h','6')

a7 = cage(Empty,'a','7')
b7 = cage(Empty,'b','7')
c7 = cage(Empty,'c','7')
d7 = cage(Empty,'d','7')
e7 = cage(Empty,'e','7')
f7 = cage(Empty,'f','7')
g7 = cage(Empty,'g','7')
h7 = cage(Empty,'h','7')

a8 = cage(Empty,'a','8')
b8 = cage(Empty,'b','8')
c8 = cage(Empty,'c','8')
d8 = cage(Empty,'d','8')
e8 = cage(Empty,'e','8')
f8 = cage(Empty,'f','8')
g8 = cage(Empty,'g','8')
h8 = cage(Empty,'h','8')

listCage = [a1,b1,c1,d1,e1,f1,g1,h1,a2,b2,c2,d2,e2,f2,g2,h2,a3,b3,c3,d3,e3,f3,g3,h3,a4,b4,c4,d4,e4,f4,g4,h4,a5,b5,c5,d5,e5,f5,g5,h5,a6,b6,c6,d6,e6,f6,g6,h6,a7,b7,c7,d7,e7,f7,g7,h7,a8,b8,c8,d8,e8,f8,g8,h8]

def check(fig,cage):
	if fig.x==cage.x and fig.y == cage.y:
		cage.figure = fig
def redefind():	
	i = 0
	while i < 64:
		j = 0
		while j < 32:
			check(listFigure[j],listCage[i])
			j += 1
		i += 1

def printChessBoard():
		redefind()
		print('   - - - - - - - -')
		print('8|',a8.figure.f,b8.figure.f,c8.figure.f,d8.figure.f,e8.figure.f,f8.figure.f,g8.figure.f,h8.figure.f,'|')
		print('7|',a7.figure.f,b7.figure.f,c7.figure.f,d7.figure.f,e7.figure.f,f7.figure.f,g7.figure.f,h7.figure.f,'|')
		print('6|',a6.figure.f,b6.figure.f,c6.figure.f,d6.figure.f,e6.figure.f,f6.figure.f,g6.figure.f,h6.figure.f,'|')
		print('5|',a5.figure.f,b5.figure.f,c5.figure.f,d5.figure.f,e5.figure.f,f5.figure.f,g5.figure.f,h5.figure.f,'|')
		print('4|',a4.figure.f,b4.figure.f,c4.figure.f,d4.figure.f,e4.figure.f,f4.figure.f,g4.figure.f,h4.figure.f,'|')
		print('3|',a3.figure.f,b3.figure.f,c3.figure.f,d3.figure.f,e3.figure.f,f3.figure.f,g3.figure.f,h3.figure.f,'|')
		print('2|',a2.figure.f,b2.figure.f,c2.figure.f,d2.figure.f,e2.figure.f,f2.figure.f,g2.figure.f,h2.figure.f,'|')
		print('1|',a1.figure.f,b1.figure.f,c1.figure.f,d1.figure.f,e1.figure.f,f1.figure.f,g1.figure.f,h1.figure.f,'|')
		print('   - - - - - - - -')
		print('  ','a','b','c','d','e','f','g','h')
printChessBoard()

a = 0
b = 0
while True:
	a = input()
	if a=='stop':
		break
	a_zero = int(len(a)/2)
	a_one = a[:a_zero]
	a_two = a[a_zero:]
	b = input()
	if b =='stop':
		break
	b_zero = int(len(b)/2)
	b_one = b[:b_zero]
	b_two = b[b_zero:]
	def find(_1,_2):
		i = 0
		while i < 64:
			if listCage[i].x == _1 and listCage[i].y == _2:
				return listCage[i]
			else:
				i+=1
	def findNum(_1,_2):
		i = 0
		while i < 64:
			if listCage[i].x == _1 and listCage[i].y == _2:
				return i
			else:
				i+=1
	if find(a_one,a_two).figure.c=='b':
		print('color error')
		continue
	else:
		if find(a_one,a_two).figure.f=='x':
			print('empty error')
		elif find(a_one,a_two).figure.f=='p':
			PmoveOneCage = (int(find(a_one,a_two).y)+1==int(find(b_one,b_two).y)) and (find(b_one,b_two).figure.f=='x')
			PmoveTwoCage = (int(find(a_one,a_two).y)==2 and (int(find(a_one,a_two).y)+2)==int(find(b_one,b_two).y)) and (find(b_one,b_two).figure.f=='x')
			PmoveAttack = (int(find(a_one,a_two).y)+1==int(find(b_one,b_two).y)) and ((linearSearch(xList,(find(a_one,a_two).x))+1)==(linearSearch(xList,(find(b_one,b_two).x))) or (linearSearch(xList,(find(a_one,a_two).x)))==(linearSearch(xList,(find(b_one,b_two).x))+1)) and (find(b_one,b_two).figure.f !='x')
			Pmove = PmoveOneCage or PmoveTwoCage or PmoveAttack
			if Pmove==True:
				find(b_one,b_two).figure = find(a_one,a_two).figure
				find(a_one,a_two).figure = Empty()
				listCage[findNum(a_one,a_two)] = find(a_one,a_two).figure
				listCage[findNum(b_one,b_two)] = find(b_one,b_two)
				printChessBoard()
			else:
				print('error pawn move')
		elif find(a_one,a_two).figure.f=='r':
			print('rook error')
		elif find(a_one,a_two).figure.f=='k':
			print('knihg error')
		elif find(a_one,a_two).figure.f=='b':
			print('bishop error')
		elif find(a_one,a_two).figure.f=='q':
			print('queen error')
		elif find(a_one,a_two).figure.f=='K':
			print('king error')
		else:
			find(b_one,b_two).figure = find(a_one,a_two).figure
			find(a_one,a_two).figure = Empty()
			listCage[findNum(a_one,a_two)] = find(a_one,a_two).figure 
			listCage[findNum(b_one,b_two)] = find(b_one,b_two).figure
			printChessBoard()
print('thank you for playing!')
