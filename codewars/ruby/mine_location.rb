def mineLocation(a)
	m = []
	a.each {|s| m.push a.index(s), s.index(1) if s.index(1) }
	m
end


print mineLocation([ [1, 0], [0, 0] ])
print mineLocation([ [1, 0, 0], [0, 0, 0], [0, 0, 0] ])
print mineLocation([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ])