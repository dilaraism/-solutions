def breakChocolate(n,m):
	s=0
	while m*n != 1:
		s+=1
		if n>m:
			breakChocolate(n-1, m)	
		else:
			breakChocolate(n, m-1)	
	return s

print breakChocolate(5,2)


