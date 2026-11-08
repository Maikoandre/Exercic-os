def is_bigger_than_zero(sides):
    return all(side > 0 for side in sides)
    
def is_triangle(sides):
    return (sides[0] + sides[1] > sides[2] 
            and sides[0] + sides[2] > sides[1] 
            and sides[2] + sides[1] > sides[0])
    
def equilateral(sides):
    return (is_bigger_than_zero(sides)
            and is_triangle(sides) 
            and sides[0] == sides[1] == sides[2])

def isosceles(sides):
    if not is_bigger_than_zero(sides):
        return False
    
    is_isosceles = (sides[0] == sides[1]
                   or sides[0] == sides[2]
                   or sides[2] == sides[1])
    
    return (is_bigger_than_zero(sides)
            and is_triangle(sides) 
            and is_isosceles)

def scalene(sides):
    if not is_bigger_than_zero(sides):
        return False

    is_scalene = (sides[0] != sides[1]
                and sides[1] != sides[2]
                and sides[0] != sides[2])

    return (is_bigger_than_zero(sides) 
            and is_triangle(sides) 
            and is_scalene)