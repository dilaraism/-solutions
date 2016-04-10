def smallest(n):
	from fractions import gcd
	return reduce(lambda x, y: x*y/gcd(x,y), range(1,n+1))

	