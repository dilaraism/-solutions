def decompose(n):
	r = lambda x: False if x**(0.5)>int(x**(0.5)) else True
	filter(r, range(2*n))
	
