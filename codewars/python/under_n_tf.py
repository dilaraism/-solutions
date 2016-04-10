def solution(number):
    tf = lambda x: x if (x%3==0) or (x%5==0) else 0
    return sum(map(tf, range(n)))