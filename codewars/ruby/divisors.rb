def divisors(n)
   a = []
   (2..(n/2)).to_a.each {|d| a<<d if n%d==0}
   a.length > 0 ? a : "#{n} is prime"
end
