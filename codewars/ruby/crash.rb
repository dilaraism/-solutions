f = File.read("gs.txt")
l = f.split("\n")
puts l.length
l.each {|s| l.delete(s) if s.length<1}
puts l.length
w = f.split()
print w.uniq.length
puts ''
print w.length

# class Person
# 	attr_accessor :name
# 	def initialize(name)
# 		@name = name
# 	end

# 	def greet 
# 		"hello #{@name}"
# 	end
# end

# class Student < Person
# 	def study
# 		"ZzzzZzzzz"
# 	end
# end

# p = Person.new("Ziya")
# puts p.greet
# puts p.name
# p.name = "Arif"
# puts p.name
# puts p.greet
# s = Student.new("Wyatt")
# puts s.greet
# puts s.name
# puts s.study