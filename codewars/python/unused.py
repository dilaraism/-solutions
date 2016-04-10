def unused(*args):
    d = list(set(range(10)) - set([int(j) for j in "".join([str(i) for i in args])]))
    d.sort()
    return "".join([str(t) for t in d])

print unused(12, 34, 90)
print unused(12, 3, 4, 56)
print unused(1234, 56)
print unused(123456)

