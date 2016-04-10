class Calculator(object):
  def evaluate(self, string):
    return round(eval(string), 10)

print Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
print Calculator().evaluate("1.1 * 2.2 * 3.3")
