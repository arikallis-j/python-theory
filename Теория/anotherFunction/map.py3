W = ["234","145","14","1235","14"]
rule=(map(int,W))
#функция map создаёт правило применения какой либо функции к объектам данного массива
s=list(rule)
print(s)
s_1 = ["234","145","14","1235","25"]
s_2 = ["23","14","1","123","2"]
ruleInt_1 = map(int,s_1)
ruleInt_2 = map(int,s_2)
s_1 = ruleInt_1
s_2 = ruleInt_2
def summing(x,y):
	summ=x+y
	print(summ)
summing(21,2)
#правило может применяться для нескольких массивов
ruleSumm = map(summing,s_1,s_2)
s = list(ruleSumm)