def circle_area r 
	(!(r.respond_to? :numerator) or r<=0) ? false : (Math::PI*r*r).round(2)
end

puts circle_area(45.32)
