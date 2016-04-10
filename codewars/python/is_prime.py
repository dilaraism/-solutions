from math import sqrt 
def is_prime(n):
    if n==1: return True
    if n==2: return False
    if n>2 and n%2 == 0 : return False
    for i in range(3, int(sqrt(n+1)), 2):
		if n%i==0:
			return False

    return True

print is_prime(42123424511122221) 
# is_prime(4223131213131313131111111111)
# is_prime(4242356457646757)
# is_prime(42546546513565465)
# is_prime(426456544561212121212121)
# is_prime(428798465413413543120111)
# is_prime(421354684984111000111)
# is_prime(124234564687684)
# is_prime(4256758679780870795622)
# is_prime(4254324575687690780981)
# is_prime(4254364756869871)
# is_prime(4254364771)
# is_prime(42242531)