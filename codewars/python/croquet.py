def openOrSenior(data):
	f = lambda x,y: "Senior" if ((x>54) and (y>7)) else "Open"
	return [f(*i) for i in data]

a = [[45, 12],[55,21],[19, -2],[104, 20]]
print openOrSenior(a)