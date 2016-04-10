def tribonacci_(signature, n):
	[a, b, c] = signature
	for i in xrange(n):
		yield a
		a,b,c = b, c, a+b+c


def tribonacci(signature, n):
	return list(tribonacci_(signature, n))