def simple_pig(s):
	from string import punctuation
	sp = lambda x: x[1:]+x[0]+"ay" if x not in punctuation else x 
	return " ".join([sp(i) for i in s.split(" ")])

print simple_pig("Quis custodiet o ipsos custodes ?")
print simple_pig("Pig latin is cool")