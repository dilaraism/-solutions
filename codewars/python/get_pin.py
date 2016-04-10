from itertools import product
def get_pin(n):
	possible  =[['0', '8'], 
				['1', '2', '4'], 
				['1', '2', '3', '5'],
				['2', '3', '6'],
				['1', '4', '5', '7'],
				['2', '4', '5', '6', '8'],
				['3', '5', '6', '9'],
				['4', '7', '8'],
				['5', '7', '8', '9', '0'],
				['6', '8', '9']
			]
	retval = []	 
	adjs = map(int, n)
	
	for i in adjs:
		retval.append(possible[i])
	
	retval = list(product(*retval))

	return map("".join, retval)		

	 
	# return [i for i in possible[int(i)]] 

print get_pin('3456')

