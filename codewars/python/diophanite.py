def sol_equa(n):
    m = [i for i in range(1,n+1) if n%i==0]
    c = len(m)/2
    p = m[:c] if len(m)%2==0 else m[:c]+[m[c]]
    q = m[c:]
    q.sort(reverse = True)
    p1 = []
    q1= []
    for i in range(len(p)):
        if p[i]%2 == q[i]%2:
            p1.append(p[i])
            q1.append(q[i])
    solutions = []
    for j in range(len(p1)):
        if (int((p1[j]+q1[j])/2.0) == (p1[j]+q1[j])/2.0) and  (int((q1[j]-p1[j])/4.0) == (q1[j]-p1[j])/4.0):
            solutions.append([(p1[j]+q1[j])/2, (q1[j]-p1[j])/4])            
    
    return solutions

print sol_equa(90000001)