# ------------------------------------------------------------------
# 	Create a Vector object that supports addition, subtraction, 
# 	dot products, and norms. So, for example:
# 	a = Vector([1,2,3])
# 	b = Vector([3,4,5])
# 	c = Vector([5,6,7,8])
# 	a.add(b) # should return Vector([4,6,8])
# 	a.subtract(b) # should return Vector([-2,-2,-2])
# 	a.dot(b) # should return 1*3+2*4+3*5 = 26
# 	a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
# 	a.add(c) # raises an exception
# 	If you try to add, subtract, or dot two vectors with different lengths, 
#   you must throw an error!
# 	Also provide:
#     a toString function, so that using the vectors from above, a.toString() === '(1,2,3)' 
# 	(in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
#     an equals function, so that two vectors who have the same components are equal
# 	The test cases will utilize the user-provided equals method.
# ------------------------------------------------------------------

class Vector(list):
	def __init__(self, arr):
		self.arr = arr 

	def toString(self):
		# return str(tuple(self.arr))
		s = map(str, self.arr)
		w = ",".join(s)
		return "("+w+")"


	def add(self, o):
		if len(self.arr) == len(o.arr):
			r = [self.arr[i]+o.arr[i] for i in range(0, len(o.arr))]
			return Vector(r)
		else:
			raise TypeError

	def subtract(self, o):
		if len(self.arr) == len(o.arr):
			r = [self.arr[i]-o.arr[i] for i in range(0, len(o.arr))]
			return Vector(r)
		else:
			raise TypeError

	def dot(self, o):
		if len(self.arr) == len(o.arr):
			r = [self.arr[i]*o.arr[i] for i in range(0, len(o.arr))]
			return sum(r)
		else:
			raise TypeError

	def norm(self):
		from math import sqrt
		r = [i*i for i in self.arr]
		return sqrt(sum(r))

	def equals(self, o):
		return set(self.arr) == set(o.arr)


	def __repr__(self):
		return self.toString()




	# def add(self, vec):
	# 	if isinstance(vec, Vector):
	# 		s = map(sum, zip(self.arr, vec.elm))
	# 	return Vector(s)



a = Vector([3,4,5])
b = Vector([3,6,9])
c = Vector([1,2,3])
print a.add(b).equals(Vector([6,10,14]))
print a.subtract(b)
print a.dot(b)			
print a.norm()
print a.toString()
print a.equals(b)
print a.equals(Vector([5,4,3]))