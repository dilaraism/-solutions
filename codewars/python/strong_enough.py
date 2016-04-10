def strong_enough(earthquake, age):
	return "Safe!" if 1000*(1.00-0.01)**age - reduce(lambda x,y:x*y, map(sum, earthquake)) >0 else "Needs Reinforcement!"
