from math import pi

def area(r):
    '''
    На вход подается радиус окружности
    На выходе возвращается площадь окружности
    '''
    if type(r) == str:
        return "error: r must be int"
    if r < 0:
        return "error: circle's area can't be negative"
    return pi * r**2

def perimeter(r):
    '''
    На вход подается радиус окружности
    На выходе возвращается периметр окружности
    '''
    if type(r) == str:
        return "error: r must be int"
    if r < 0:
        return "error: circle's perimeter can't be negative"
    return 2 * pi * r
