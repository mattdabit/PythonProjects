# Name: Matthew Dabit
# Login: cs61a-fg
# TA: Robert
# Section: 103
# Q1.

def divide_by_fact(dividend, n):
    """Recursively divide dividend by the factorial of n.

    >>> divide_by_fact(120, 4)
    5.0
    """
    if n <= 0:
    	return dividend
    return divide_by_fact(dividend / n, n - 1)

# Q2.

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a tuple of sequences, each
    corresponding to a group.
    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """
    num = len(seq)
    assert num >= 12
    new_tup = []
    def help_me(seq, new_tup, num):
        if num == 12:
            new_tup.append(seq[0:4])
            new_tup.append(seq[4:8])
            new_tup.append(seq[8:])
        elif num == 13:
            new_tup.append (seq[0:4]) 
            new_tup.append (seq[4:8]) 
            new_tup.append (seq[8:])
        elif num == 14:
            new_tup.append (seq[0:4]) 
            new_tup.append (seq[4:9])
            new_tup.append (seq[9:])
        elif num == 15:
            new_tup.append (seq[0:5]) 
            new_tup.append (seq[5:10])
            new_tup.append (seq[10:])
        else:
            new_tup.append(seq[0:4])
            return help_me(seq[4:], new_tup, num=len(seq[4:]))
        return tuple(new_tup)
    return help_me(seq, new_tup, num=len(seq))


"""

   ====
    ==
========== <--- spatula underneath this crust
 ========

    ||
    ||
   \||/
    \/

========== }
    ==     } flipped
   ====    }
 ========

"""

# Q3.

def partial_reverse(lst, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.
    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    for x in lst[start:]:
        lst.insert(start,x)
        lst.pop()

# Q4.

def index_largest(seq):
    """Return the index of the largest element in the sequence.

    >>> index_largest([8, 5, 7, 3 ,1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    x, greatest, index = len(seq), seq[0], 0
    for elem in range(1, x):
        if seq[elem] > greatest:
            greatest = seq[elem]
            index = elem
    return index

# Q5.

def pizza_sort(lst):
    """Perform an in-place pizza sort on the given list, resulting in
    elements in descending order.
    >>> a = [8, 5, 7, 3, 1, 9, 2]
    >>> pizza_sort(a)
    >>> a
    [9, 8, 7, 5, 3, 2, 1]
    """
    length = len(lst)
    def based_god_help_me(lst,index=0):
        if index == length - 1:
            return
        greatest = index_largest(lst[index:]) + index
        lst[greatest], lst[index] = lst[index], lst[greatest]
        based_god_help_me(lst,index+1)
    return based_god_help_me(lst)  

# Q6.

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.
    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    sum = []
    def accumulator(x):
        sum.append(x)
        total = 0
        for elem in sum:
            total += elem
        return total
    return accumulator

# Q7.

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    total = 0
    def akumalate(x):
        nonlocal total
        total = total + x      
        return total
    return akumalate
# Q8.

# Old version
def count_change(a, coins=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    elif a < 0 or len(coins)==0:
        return 0
    return count_change(a, coins[1:]) + count_change(a - coins[0], coins)

# Version 2.0
def make_count_change():
    """Return a function to efficiently count the number of ways to make
    change.

    >>> cc = make_count_change()
    >>> cc(500, (50, 25, 10, 5, 1))
    59576
    """
    "*** YOUR CODE HERE ***"

