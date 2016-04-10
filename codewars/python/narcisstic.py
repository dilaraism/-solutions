def narcisstic(num):
	power = len(str(num))
	digits = [int(i) for i in str(num)]
	s = sum([i**power for i in digits])
	return s==num

print narcisstic(153)
print narcisstic(1643)
print narcisstic(7)
print narcisstic(1634)

