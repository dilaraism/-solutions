def iq_test(numbers):
	odd_even = lambda x: x%2
	nums = [int(i) for i in numbers.split(" ")]
	binary = map(odd_even, nums)
	return (binary.index(0)+1) if sum(map(odd_even, nums))>1 else (binary.index(1)+1)
	
print iq_test("1 2 22 4 56")
print iq_test("1 2 3 5 7 15")