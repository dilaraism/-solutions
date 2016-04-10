
def dirReduc(u)
	op = {"SOUTH" => "NORTH", "WEST" => "EAST", "EAST" => "WEST", "NORTH" => "SOUTH"}
	u.each do |w|
		if op[u[u.index(w)+1]] == w
			u.delete(u[u.index(w)+1]); u.delete(w)
		end 
	end
	u
end

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
puts dirReduc(a)

