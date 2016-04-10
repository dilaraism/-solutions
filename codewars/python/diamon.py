def shape(n):
    for i in range(2*n+ 1):
        if (i < n):
            print "$" * (n - i) + "*" * 2 * i + "$" * (n - i)
        elif i == n:
            print "*" * 2 * n
        elif i > n:
            print "&" * (i - n) + "*" * 2 *  (2* n - i) + "&" * (i - n)

shape(5)