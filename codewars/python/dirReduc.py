def dirReduc(u):
	op = {"SOUTH": "NORTH", "WEST":"EAST", "EAST":"WEST", "NORTH":"SOUTH"}

	for i in u:
		n = u.index(i)
		if u[n+1] == op[i]:
			u.remove(u[n])
			u.remove(u[n+1])
		else:
			continue
	return u

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print dirReduc(a)

