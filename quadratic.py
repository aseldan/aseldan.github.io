from math import sqrt
def solve_quadratic(a,b,c):
    z=(b**2)-(4*a*c)
    if z<0:
        return None
    else:
        x=int((-b+sqrt(z))/(2*a))
        y=int((-b-sqrt(z))/(2*a))
        if x==y:
            return x
        else:
            return x,y