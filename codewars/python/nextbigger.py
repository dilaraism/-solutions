def next_bigger(n):
    l = [int(i) for i in str(n)]
    lenl = len(l)
    for i in range(lenl-2, -1, -1):
	    c = l[i]
	    r= l[i+1]
	    if c<r:
	    	temp_c_index = l.index(c);
	    	print "temp c index is ", temp_c_index, "value", c
	    	temp_r_index = l.index(r);
	    	print "temp r index is ", temp_r_index, "value", r	    	
	    	l[temp_c_index] = r
	    	print l[temp_c_index]
	    	l[temp_r_index] = c
	    	print l[temp_r_index]
	    	right_side = l[temp_c_index+1:];
	    	right_side.sort();left = l[:temp_c_index+1];
	    	whole = left+right_side
	    	return int("".join(map(str, whole)))
    return -1

print next_bigger(41312)