def add(x, y):
    return x+y
def minus(x, y):
    return x-y
def sum_args(*args):
    return reduce(add, args, 0)
def arg(*args):
    return args

print arg(12,3)

def spread(f, *args):
	if hasattr(f, '__call__'):
		return reduce(f, *args) 
	else:
		  l = list(f)
		  l.append(args)
		  return tuple(l)



print spread(lambda x, y: x+y, [1,2])
print spread(add, [6,5])

print spread(minus, [2,1])
print spread(minus, [9,2])

print spread(sum_args, [1,1,1])
print spread(sum_args, [9,10,11])

print spread(arg, [19,22,16])
print spread(arg, [3,13,5])  # (3,13,5) 