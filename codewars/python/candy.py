def candies(s):
	return sum([(max(s)-i) for i in s]) if len(s) > 1 else -1

print candies([5,8,6,4]) #,9)
print candies([1,2,4,6])#,11)
print candies([1,2]) #,1)
print candies([4,2]) #,2)
print candies([])