# CS 61A Fall 2014
# Name: Kevin L Chen
# Login: cs61a-sj

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    assert n > 0, "n must be a positive number"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    assert n > 0, "n must be a positive number"
    if n <= 3:
        return n
    else:
        k = 4 
        result_minus_one = 3
        result_minus_two = 2
        result_minus_three = 1
        while k <= n  :
            result_minus_one_placeholder = result_minus_one
            result_minus_two_placeholder = result_minus_two
            result = result_minus_one + 2 * result_minus_two + 3 * result_minus_three
            result_minus_one = result
            result_minus_two = result_minus_one_placeholder
            result_minus_three = result_minus_two_placeholder
            k += 1
        return result



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k == 0:
        return False
    else:
        return has_seven(k//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    return countup(1,1,n)

##########################################
#    START PING PONG HELPER FUNCTIONS    #
##########################################
def countup(actual_number,i,n):
    if i == n:
        return actual_number
    elif i % 7 == 0 or has_seven(i):
        return countdown(actual_number-1,i+1,n)
    elif i <= n:
        return countup(actual_number+1,i+1,n)
def countdown(actual_number,i,n):
    if i == n:
        return actual_number
    if i % 7 == 0 or has_seven(i):
        return countup(actual_number+1,i+1,n)
    elif i <= n:
        return countdown(actual_number-1,i+1,n)
##########################################
#     END PING PONG HELPER FUNCTIONS     #
##########################################

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    return count_partitions(amount, find_highest_power(amount))

##########################################
#  START COUNT CHANGE HELPER FUNCTIONS   #
##########################################

def find_highest_power(amount):
    k = 0
    while pow(2,k+1) < amount:
        k += 1
    return pow(2,k)

def count_partitions(amount, m): 
    if amount == 0: 
        return 1
    elif amount < 0: 
        return 0
    elif m == 0: 
        return 0
    else:
        with_m = count_partitions(amount-m, m ) 
        without_m = count_partitions(amount, m//2)
        return with_m + without_m

##########################################
#   END COUNT CHANGE HELPER FUNCTIONS    #
##########################################


def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    offset = 6 - start - end
    if n == 1:
        move_disk(start,end)
    else: 
        towers_of_hanoi(n-1,start,offset)
        move_disk(start,end)
        towers_of_hanoi(n-1,offset,end)

def move_disk(start, end):
    print("Move the top disk from rod", start, "to rod", end)



# from operator import sub, mul

# def make_anonymous_factorial():
#     """Return the value of an expression that computes factorial.

#     >>> make_anonymous_factorial()(5)
#     120
#     """
#     return YOUR_EXPRESSION_HERE

