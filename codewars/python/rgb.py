def to_rgb(r,g,b):
	l = lambda x: 0 if x<0 else x
	w = map(l, (r,g,b)); return str(bytearray(w)).encode('hex')
	
	#return str(bytearray(w)).encode('hex').upper()
    

print to_rgb(-20,215,125)