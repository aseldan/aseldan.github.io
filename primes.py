def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True

def primes_below(n):
    l=[]
    for i in range (2,n):
        if is_prime(i):
            l.append(i)
    return l 
