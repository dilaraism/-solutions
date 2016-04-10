def pat(n)
 r =""
 if n<1
 	r=r
 else
	 i=1
	 until i==n+1
	   n.downto(i) {|q| r<<"#{q}"}
	     i=i+1
	     r<<"\n"
	 end
 end
 r
end
w = "---------"
puts pat(-1)
puts w
puts pat(3)
puts w
puts pat(5)
puts w
puts pat(12)


