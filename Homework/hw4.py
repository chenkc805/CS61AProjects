# CS 61A Fall 2014
# Name: Kevin L. Chen
# Login: cs61a-sj

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    if type(a) != int or type(b) != int:
        return [a,b]
    return range(a,b+1)

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[-1]

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert 0 not in y , "y cannot span 0"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    lower = lower_bound(x) - lower_bound(y)
    lower1 = upper_bound(x) - lower_bound(y)
    lower2 = lower_bound(x) - upper_bound(y)
    lower3 = upper_bound(x) - upper_bound(y)
    lower = min(lower, lower1, lower2, lower3)
    upper = max(lower, lower1, lower2, lower3)
    return interval(lower, upper)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
r1 = interval(499,501)
r2 = interval(498,502)

def multiple_references_explanation():
    return """The mulitple reference problem says that if the same interval is called many times,
            then there will be more error than if you called the interval fewer times. The error 
            from the interval compounds when the interval is called multiple times. This is why 
            par2 is more accurate than par1."""

from math import sqrt 
def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    extreme = b*b/(4*a) + c - b*b/(2*a)
    if a > 0:
        if (-b + sqrt(b*b - 4*a*(c-extreme)))/(2*a) < lower_bound(x) or (-b - sqrt(b*b - 4*a*(c-extreme)))/(2*a) < lower_bound(x): 
            t = lower_bound(x)
            return interval(a*t*t+b*t+c,max(a*t*t+b*t+c for t in x))
        else:
            return interval(b*b/(4*a) + c - b*b/(2*a), max(a*t*t+b*t+c for t in x))
    else:
        if (-b + sqrt(b*b - 4*a*(c-extreme)))/(2*a) > upper_bound(x) or (-b - sqrt(b*b - 4*a*(c-extreme)))/(2*a) > upper_bound(x):
            t = upper_bound(x)
            return interval(min(a*t*t+b*t+c for t in x),a*t*t+b*t+c) 
        else: 
            return interval(min(a*t*t+b*t+c for t in x),b*b/(4*a) + c - b*b/(2*a))
# def polynomial(x, c):
#     """Return the interval that is the range of the polynomial defined by
#     coefficients c, for domain interval x.

#     >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
#     '-3 to 0.125'
#     >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
#     '0 to 10'
#     >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
#     '18.0 to 23.0'
#     """
#     "*** YOUR CODE HERE ***"



