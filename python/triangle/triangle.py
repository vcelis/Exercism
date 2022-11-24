def equilateral(sides):
    return len(set(sides)) == 1 and sides[0] > 0

def isosceles(sides):
    a, b, c = sorted(sides)
    return 0 < a and c < a + b and b in (a, c)
    
def scalene(sides):
    a, b, c = sorted(sides)
    return 0 < a < b < c < a + b
