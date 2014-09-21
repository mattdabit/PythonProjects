# Name:Matthew Dabit    
# Login:cs61a-fg
# TA:Robert Huang
# Section:103
# Q1.

def stone_age():
    """Returns the year in which Steven and Eric took CS 61A."""
    return  2009

# Q2.

def favorite_player():
    """Returns Steven's favorite basketball player."""
    return  'Tim Duncan'

# Q3.

def favorite_number():
    """Returns Eric's favorite number."""
    return  42

# Q4.

from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

# Q5.

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max((pow(a,2) + pow(b, 2)), (pow(b, 2) + pow(c, 2)), (pow(a, 2) + pow(c, 2)))

# Q6.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
	return True
def t():
	return 1

def f():
	return somethings_wrong

# Q7.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
def hailstone(n) :
	t = 1	
	while n != 1 :
		print ("n")
		if n%2 == 0:
			n = n//2
			t = t + 1
		else:
			n = n*3 + 1
			t = t + 1
		print ('n')
	return t		


