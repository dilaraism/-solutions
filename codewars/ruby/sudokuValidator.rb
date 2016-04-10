require 'matrix'
def validSolution(board)
  n = Matrix.empty()	
  board.each {|r| n=Matrix.rows(n.to_a << r) }
  minorranges = [0..2, 3..5, 6..8]*2
  mr = minorranges.combination(2).to_a.uniq!
  o = []
  mr.each {|u| o << ((n.minor(u[0], u[1]).to_a.flatten.inject(&:+) == 45) and (n.minor(u[0], u[1]).to_a.flatten.uniq == n.minor(u[0], u[1]).to_a.flatten)) ? true : false }
  (0..8).each {|f| o<< ((!n.include?(0)) and (n.column(f).to_a.inject(&:+)==45) and (n.column(f).to_a.uniq == n.column(f).to_a)  and (n.row(f).to_a.uniq == n.row(f).to_a) and (n.row(f).to_a.inject(&:+)==45)) ? true : false }
  !o.include?(false)
end


b1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8],[1, 9, 8, 3, 4, 2, 5, 6, 7],[8, 5, 9, 7, 6, 1, 4, 2, 3],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 6, 1, 5, 3, 7, 2, 8, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 4, 5, 2, 8, 6, 1, 7, 9]]
puts validSolution(b1)
b2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                         [6, 7, 2, 1, 9, 0, 3, 4, 9],
                         [1, 0, 0, 3, 4, 2, 5, 6, 0],
                         [8, 5, 9, 7, 6, 1, 0, 2, 0],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 0, 1, 5, 3, 7, 2, 1, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 0, 0, 4, 8, 1, 1, 7, 9]]

puts validSolution(b2)