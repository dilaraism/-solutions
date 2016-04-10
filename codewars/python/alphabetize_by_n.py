def sort_it(list_, n):
	list_ = list_.split(", ")
	list_.sort(key = lambda w: w[n-1])
	return ", ".join(list_)

print sort_it('bill, bell, ball, bull', 2)


#	wl = [j for j in args[0]]
#	k = args[1]-1
#	wl.sort(key = lambda w: w[k])
#	return wl

