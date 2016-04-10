from itertools import combinations

def power(s):
    i = 0
    x=[]
    while i<len(s)+1:
        x+=map(list, list(combinations(s, i)))
        print x
        i+=1
    return sorted(x)

print power([1,2,3,4])