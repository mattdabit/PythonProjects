# Name:Matthew Dabit
# Login: cs61a-fg
# TA: Robert
# Section:103
# Q1.

def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x-dx) + f(x) + f(x+dx))/3

def repeated(f, n):
    def h(x):
        b, a = f(x), 1
        while a<n:
            b, a = (f(b)), a +1
        else: 
            return b
    return h
        

def n_fold_smooth(f, dx, n0):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    return repeated(lambda smoother:(smooth(smoother, dx),n))(f)

# Q2.

def iterative_continued_frac (n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(iterative_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(iterative_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    total, t = 0, k
    while t>0:
        n = n_term(t)
        d = d_term(t)
        total = n/(d+total)
        t -= 1
    return total


def recursive_continued_frac(n_term, d_term, k):
    """Returns the k-term continued fraction with numerators defined by n_term
    and denominators defined by d_term.

    >>> # golden ratio
    ... round(recursive_continued_frac(lambda x: 1, lambda x: 1, 8), 3)
    0.618
    >>> # 1 / (1 + (2 / (2 + (3 / (3 + (4 / 4))))))
    ... round(recursive_continued_frac(lambda x: x, lambda x: x, 4), 6)
    0.578947
    """
    def help_func(x):
        if x==1:
            return n_term(k)/d_term(k)
        else:
            return n_term(k-x+1)/(d_term(k-x+1)+help_func(x-1))
    return help_func(k)

# Q3.

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
    if n<=3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)
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
    if n<=3:
        return n
    else:
        g1, g2, g3, i = 3, 2, 1 , n-3
        while i > 0:
            g1, g2, g3 = g1+2*g2+3*g3, g1, g2
            i -= 1
        return g1
# Q4.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return YOUR_EXPRESSION_HERE

0