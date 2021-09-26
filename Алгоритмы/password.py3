d = None
while d!=0:
	fby = 2011 + 2004 + 1979 +1979
	id = 208845342
	d = int(input("day: "))
	w = int(input("week: "))
	m = int(input("moon: "))
	def password(fby,id,m,w,d):
		p = (((fby*id)/m)+d)/w
		p%=10**9
		p = str(p)
		x = p[:5]
		y = p[10:14]
		p = int(x+y)
		return p
	pw = password(fby,id,m,w,d)
	print(pw)