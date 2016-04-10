import os 
def lcs(x, y):
  return "".join([i for i in y if i in x])


print lcs("anothertest", "notatest")
print os.system("ping google.az -c 10")
print "---------------------------"