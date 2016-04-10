def pentafib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	elif n ==2:
		return 1
	elif n==3:
		return 2
	elif n==4:
		return 4
	else:
		return pentafib(n-5)+pentafib(n-4)+pentafib(n-3)+pentafib(n-2)+pentafib(n-1)



# map(pentafib, range(10))

def count_odd_pentaFib(n):
	return sum(map(lambda x: 1 if (x%6==1) or (x%6==0) else 0, range(n+1)))-1 



# def count_off_pentafib(n):
#     return len(filter(lambda x: x%2 != 0, map(pentafib, range(n+1))))-1

print count_odd_pentaFib(5)
print count_odd_pentaFib(10)
print count_odd_pentaFib(15)
print count_odd_pentaFib(20)
print count_odd_pentaFib(25)
print count_odd_pentaFib(45)
print count_odd_pentaFib(68)