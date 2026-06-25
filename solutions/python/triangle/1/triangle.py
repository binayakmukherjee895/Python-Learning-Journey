def equilateral(sides):
    a,b,c=sides
    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or b+c<a or c+a<b:
        return False
    if a==b and b==c and c==a:
        return True
    else:
        return False
def isosceles(sides):
    a,b,c=sides
    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or b+c<a or c+a<b:
        return False
    if a==b or b==c or c==a:
        return True
    else:
        return False
def scalene(sides):
    a,b,c=sides
    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or b+c<a or c+a<b:
        return False
    if a!=b and b!=c and c!=a:
        return True
    else:
        return False
