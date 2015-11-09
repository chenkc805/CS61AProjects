# CS 61A Fall 2014
# Name: Kevin L. Chen
# Login: cs61a-sj


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    assert type(a)== int, 'The variable a must be an integer.'
    assert type(b)== int, 'The variable b must be an integer.'
    assert type(c)== int, 'The variable c must be an integer.'
    if a == b == c:
        return False
    elif a==b or b==c or a==c:
        return True
    return False

def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    assert type(a)== int, 'The variable a must be an integer.'
    assert type(b)== int, 'The variable b must be an integer.'
    def members(x,y):
        while x > 1:
            if x % 2== 0:
                x = x//2
            else:
                x = 3*x+1
            if y == x:
                return True
    n = members(a,b)
    m = members(b,a)
    return n or m or False


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19
    >>> near_golden(18)
    3
    >>> near_golden(20)
    4
    >>> near_golden(22)
    4
    >>> near_golden(24)
    5
    >>> near_golden(26)
    5
    >>> near_golden(28)
    5
    >>> near_golden(30)
    6
    >>> near_golden(32)
    6
    >>> near_golden(34)
    7
    >>> near_golden(36)
    7
    >>> near_golden(38)
    7
    >>> near_golden(40)
    8
    """
    "*** YOUR CODE HERE ***"
    from math import sqrt
    assert type(perimeter) == int, 'The PERIMETER must be an integer.'
    assert perimeter % 2 == 0, 'The PERIMETER must be an even number.'
    assert perimeter > 3, 'The PERIMETER must be greater than 3.'
    a = (perimeter/ (3 + sqrt(5)))
    a = round(a)
    return a








    