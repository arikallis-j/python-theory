Array = ['1','2','3','4','5','6','7','8','9','10']
def linearSearch(li, x):
    i = 0
    length = len(li)
    while i<length and x != li[i]:
        i+=1
    if i<length:
    	return print('Number element is '+ str(i+1))
    else :
    	print('isn\'t element in Array')
linearSearch(Array,'11')