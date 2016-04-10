t1 = [1,5,100]
t2 = [1,6,1]

t1s=reduce(lambda a,b: a^b,t1,0)
t2s=reduce(lambda a,b: a&b,t2,0)

print t1s
print t2s

print t1>t2