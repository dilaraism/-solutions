def Xbonacci(signature, n):
	l = signature
	i = len(signature)
	t = 0
	if i>n:
		return signature[:n]
	while i<n:
		l.insert(i, sum(l[t:i]))
		t+=1; i+=1
	return l

print Xbonacci([1,2,3,4,5,6,7,8,9], 5)