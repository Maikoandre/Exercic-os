def isBiggerThanZero(sides):
    return all(side > 0 for side in sides)
    
def is_triangle(sides):
    return (sides[0] + sides[1] > sides[2] 
            and sides[0] + sides[2] > sides[1] 
            and sides[2] + sides[1] > sides[0])
    
def equilateral(sides):
    return (isBiggerThanZero(sides)
            and is_triangle(sides) 
            and sides[0] == sides[1] == sides[2])

def isosceles(sides):
    if not isBiggerThanZero(sides):
        return False
    
    is_isosceles = (sides[0] == sides[1]
                   or sides[0] == sides[2]
                   or sides[2] == sides[1])
    
    return (isBiggerThanZero(sides)
            and is_triangle(sides) 
            and is_isosceles)

def scalene(sides):
    if not isBiggerThanZero(sides):
        return False

    isScalene = (sides[0] != sides[1]
                and sides[1] != sides[2]
                and sides[0] != sides[2])

    return (isBiggerThanZero(sides) 
            and is_triangle(sides) 
            and sides[0] != sides[1]
            and sides[1] != sides[2]
            and sides[2] != sides[0])