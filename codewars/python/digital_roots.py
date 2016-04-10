def digital_root(n):
    a = sum([int(i) for i in str(n)]) 
    return a if  a <10 else digital_root(a)


print digital_root(345)