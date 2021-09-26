print("x10,x20,v1,v2,k")
date = input()
date  = date.split(",")
x10 = int(date[0])
x20 = int(date[1])
v1 = int(date[2])
v2 = int(date[3])
k = int(date[4])
l = x20-x10
t = (l + k)/(v1-v2)
x2 = x20 + v2*t
print("t : "+ str(t) + " с")
print("x : " + str(x2) + " м")