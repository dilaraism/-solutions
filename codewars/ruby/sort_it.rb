def sort_it(list_, n)
	list_.split(", ").sort_by {|w| w[n-1]}.join(", ")
end

puts sort_it('bill, bell, ball, bull', 2)
