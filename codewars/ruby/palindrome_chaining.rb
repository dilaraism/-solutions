def revint(n)
	n.to_s.reverse.to_i
end

def is_palindrome?(i)
	i == revint(i)
end

def pcl(n)
	if is_palindrome?(n)
		return 0
	end
	i = 0
	until is_palindrome?(n)
		print n, "\t", revint(n), "\t", n+revint(n),"\n"
		n = n+revint(n)
		i+=1
	end
	return i
end

puts pcl(87)
puts "---------------"
puts pcl(17)
puts "---------------"
puts pcl(27)
puts "---------------"
puts pcl(587)

