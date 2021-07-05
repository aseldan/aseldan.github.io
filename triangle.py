from math import sqrt
class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def is_valid(self):
        if (self.a+self.b)>self.c and (self.b+self.c)>self.a and (self.c+self.a)>self.b:
            return True 
        else:
            return False

    def perimeter (self):
        return self.a + self.b + self.c
    
    def area(self):
        s=(self.a + self.b + self.c)/2
        x=sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return x

t=Triangle(5,5,5)

print("Triangle is %s" % t.is_valid())
print("Perimeter = %d" % t.perimeter())
print("Area = %d" % t.area())