def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    

def palindrome_primes():
    primes=[]
    for i in range (10000,100000):
        if is_prime(i):
            primes.append(i)
    primes_str=[]
    for j in primes:
        primes_str.append(str(j))
    palindrome=[]
    for v in primes_str:
        if v == v[::-1]:
            palindrome.append(v)
    return palindrome