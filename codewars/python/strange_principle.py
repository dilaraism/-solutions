t = lambda x: 0 if x==1 else 1

def metamorphosis(arr):
	l = len(arr)
	i = 0
	while i<=l:
		arr = [t(arr[i]) for i in range(i, l, i)]
		i+=1
		print arr

x = [0,0,0,0]
metamorphosis(x)