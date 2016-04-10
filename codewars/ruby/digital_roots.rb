def digital_roots(n)
	r = (n.to_s.split("").map!{|x| x.to_i}).inject(&:+)
	r < 10 ? r : digital_roots(r)
end

print digital_roots(254)