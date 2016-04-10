def fibo(n):
    a, b = 1, 1
    for i in xrange(n):
        yield a
        a, b = b, a + b



def perimeter(n):
	s = 0
	for i in fibo(n+1):
		s+=i

	return 4*s

# print perimeter(5)
# print perimeter(6)
# print perimeter(7)
# print perimeter(30)
# print perimeter(34500)
 
a = [i for i in fibo(100)]
print a

print [1.0*a[i+1]/a[i] for i in range(0, len(a)-2)]
