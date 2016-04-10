from math import factorial

def going(n):
	return round(sum(map(factorial, range(1,n+1)))/(factorial(n)*1.0), 6)

print going(5)
print going(6)
print going(7)