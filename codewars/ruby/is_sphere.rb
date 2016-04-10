def in_sphere?(coords, radius)
  coords.length.zero? ? true : (coords.map {|c| c*c }).inject(&:+) <= radius**2
end