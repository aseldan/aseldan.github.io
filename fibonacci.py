def big_fibonacci(n):
    sequence=[0,0,1]
    while len(str(sequence[-1]))!=n:
        new=sequence[-1]+sequence[-2]
        sequence.append(new)
    return sequence[-1]


#def big_fibonacci(n):
    #c=1
    #a=0
    #b=0
    #while len(str(c))!=n:
        #a=b
        #b=c
        #c=a+b
    #print(c)

