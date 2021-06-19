def my_reverse(l):
    ll=[]
    n=len(l)-1
    while len(l)>len(ll):
        ll.append(l[n])
        n=n-1
    return ll   
    