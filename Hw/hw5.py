# Name: Matthew Dabit
# Login: cs61a-fg
# TA: Robert
# Section: 103
# Q1.

empty_rlist = None

def rlist(first, rest):
    """Construct a recursive list from its first element and the
    rest."""
    return (first, rest)

def first(s):
    """Return the first element of a recursive list s."""
    return s[0]

def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]


def reverse_rlist_iterative(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_iterative(primes)
    (7, (5, (3, (2, None))))
    """
    new_list = (first(s), empty_rlist)
    while rest(s) != empty_rlist:
        s = rest(s)
        new_list = rlist(first(s), new_list)
    return new_list

def reverse_rlist_recursive(s):
    """Return a reversed version of a recursive list s.
    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_recursive(primes)
    (7, (5, (3, (2, None))))
    """
    initial_list = (empty_rlist)
    def god_help_me_func(s, newer_list):
        if rest(s) == empty_rlist:
            return rlist(first(s), newer_list)
        else:
            newer_list = rlist(first(s), newer_list)
            return god_help_me_func(rest(s), newer_list)
    return god_help_me_func(s, initial_list)
# Q2.

def interleave_recursive(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_recursive(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_recursive(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_recursive(odds, odds)
    (1, (1, (3, (3, None))))
    """
    new_list = empty_rlist
    def halp(s0, s1, new_list):
        if s1 == empty_rlist and s0 == empty_rlist:
            return new_list
        if s0 == empty_rlist:
            return halp(s1, s0, new_list)
        else:
            new_list = rlist(first(s0), new_list)
            return halp(s1, rest(s0), new_list)
    return reverse_rlist_recursive(halp(s0, s1, new_list))

def interleave_iterative(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_iterative(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_iterative(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_iterative(odds, odds)
    (1, (1, (3, (3, None))))
    """
    a = 0
    new_list = empty_rlist
    while s0 != empty_rlist or s1 != empty_rlist:
        if a == 0 and s0 != empty_rlist:
            new_list = rlist(first(s0), new_list)
            s0 = rest(s0)
        elif a == 1 and s1 != empty_rlist:   
            new_list = rlist(first(s1), new_list)
            s1 = rest(s1)
        if a == 0:
            a += 1
        else:
            a -= 1
    return reverse_rlist_recursive(new_list)

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


# Q3.

def interval(a, b):
    """Construct an interval from a to b."""
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

# Q4.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x
    divided by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert (lower_bound(y)!=0)
    assert (upper_bound(y)!=0)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q5.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.
    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'"""
    return interval((lower_bound(x)-upper_bound(y)), ((upper_bound(x)-lower_bound(y))))
# Q6.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    return make_center_width(c,abs(c*p/100))

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    return (width(x)/center(x))*100

# Q7.

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b,
    and c, for domain interval x.

    This is the less accurate version which treats each instance of t as a
    different value from the interval. See the extra for experts question for
    exploring why this is not _really_ correct and to write a more precise
    version.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-9 to 5'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '-6 to 16'
    """
    t = mul_interval(x,x)
    lower_a_bound, upper_a_bound = min(a*lower_bound(t),a*upper_bound(t)), max(a*lower_bound(t),a*upper_bound(t))
    lower_b_bound, upper_b_bound = min(b*lower_bound(x),b*upper_bound(x)), max(b*lower_bound(x),b*upper_bound(x))
    a_tt, b_t = interval(lower_a_bound,upper_a_bound), interval(lower_b_bound,upper_b_bound)
    a_plus_b = add_interval(a_tt, b_t)
    quad = interval(lower_bound(a_plus_b)+c,upper_bound(a_plus_b)+c)
    return quad

# Q8.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"

# Q9.

def multiple_reference_explanation():
  return """The multiple reference problem..."""

# Q10.

def accurate_quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b,
    and c, for domain interval x.

    >>> str_interval(accurate_quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(accurate_quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
