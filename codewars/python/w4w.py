def s(n):
	return sum([int(i) for i in n])

def order_weight(strng):
	a = [i for i in strng.split(" ")]
	a.sort(key = lambda x: s(x))
	return a# " ".join(a)

print order_weight("234 126 456 414 764 123")