class triangle:
	name = "ABC"
	ang1 = 0
	ang2 = 0
	ang3 = 0
	side1 = 0
	side2 = 0
	side3 = 0
ABC = triangle()
DEF = triangle()
def define (t,a1,a2,a3,s1,s2,s3):
	if a1+a2+a3!=180:
		print("error")
		return 0
	t.ang1 = a1
	t.ang2 = a2
	t.ang3 = a3
	t.side1 = s1
	t.sude2 = s2
	t.side3 = s3
define(ABC,60,30,90,5,4,3)
define(DEF,60,30,90,5,4,3)
I_sign_of_similarity =  (ABC.side1==DEF.side1 ) and (ABC.side2==DEF.side2) and (ABC.ang2 == DEF.ang2)
assertion = ""
if I_sign_of_similarity:
	assertion = "треугольники подобны по I признаку"
print(assertion)


