import math

def area(r):
    '''
    Returns area of given circle.
    
    Arguments:
		r (float): circle radius
    
    Return value:
		area(r): circle area
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Return perimeter of given circle.
    
    Arguments:
		r (float): circle radius
    
    Return value:
		perimeter(r): circle perimeter
    '''
    return 2 * math.pi * r
