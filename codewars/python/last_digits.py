h = {'2': [2,4,8,6],
	 '3': [3,9,7,1],
	 '4': [4,6,4,6],
	 '5': [5,5,5,5],
	 '6': [6,6,6,6],
	 '7': [7,9,3,1],
	 '8': [8,4,2,6],
	 '9': [9,1,9,1]
	 }

 

def last_digit(n1, n2):
	if (n2 == 0) or (n1%10 == 1):
		return 1
	if n1%10 == 0:
		return 0

	p = int(str(n2%4))
	q = n1%10

	return h[str(q)][p-1] 

print last_digit(4, 1)
print last_digit(4, 2)
print last_digit(9, 7)
print last_digit(10, 10 ** 10)


