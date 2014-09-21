# Name: Matthew Dabit
# Login: cs61a-fg
# TA: Robert
# Section: 103
# Q1.

# Mutable rlist
def mutable_rlist():
    """A mutable rlist that supports push, pop, and setitem operations.

    >>> a = mutable_rlist()
    >>> a('push', 3)
    >>> a('push', 2)
    >>> a('push', 1)
    >>> a('setitem', 1, 4)
    >>> a('str')
    '<rlist (1, 4, 3)>'
    """
    contents = empty_rlist
    def setitem(index, value):
        if index == 0:
            dispatch('pop')
            dispatch('push', value)
        else:
            num = dispatch('pop')
            setitem(index-1, value)
            dispatch('push', num)

    def dispatch(message, index=None, value=None):
        nonlocal contents
        if message == 'first':
            return first(contents)
        if message == 'rest':
            return rest(contents)
        if message == 'len':
            return len_rlist(contents)
        if message == 'getitem':
            return getitem_rlist(contents, value)
        if message == 'str':
            return str_rlist(contents)
        if message == 'pop':
            item = first(contents)
            contents = rest(contents)
            return item
        if message == 'push':
            contents = rlist(value, contents)
        if message == 'setitem':
            return setitem(index, value)
        return dispatch

def pair(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch

empty_rlist = None

def rlist(first, rest):
    return pair(first, rest)

def first(s):
    return s(0)

def rest(s):
    return s(1)

def len_rlist(s):
    if s == empty_rlist:
        return 0
    return 1 + len_rlist(rest(s))

def getitem_rlist(s, k):
    if k == 0:
        return first(s)
    return getitem_rlist(rest(s), k - 1)

def rlist_to_tuple(s):
    if s == empty_rlist:
        return ()
    return (first(s),) + rlist_to_tuple(rest(s))

def str_rlist(s):
    return '<rlist ' + str(rlist_to_tuple(s)) + '>'


# Q2.

class VendingMachine(object):
    """A vending machine that vends some product for some cost.

    >>> v = VendingMachine('crab', 10) ### 2 args??
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current crab stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your crab and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your crab.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    balance = 0
    stock = 0
    cost = None
    item = None
    def __init__(self, item, cost):
        VendingMachine.item = item
        VendingMachine.cost = cost
    def vend(self):
        if VendingMachine.stock == 0:
            return 'Machine is out of stock.'
        elif VendingMachine.cost > VendingMachine.balance:
            difference = VendingMachine.cost - VendingMachine.balance
            return 'You must deposit $%(diff)s more.' % dict(diff=difference)
        elif VendingMachine.balance > VendingMachine.cost:
            change = VendingMachine.balance - VendingMachine.cost
            VendingMachine.balance = 0
            VendingMachine.stock -= 1
            return 'Here is your %(obj)s and $%(change)s change.' % dict(obj=VendingMachine.item, change=change)
        elif VendingMachine.balance == VendingMachine.cost:
            VendingMachine.balance = 0
            VendingMachine.stock -= 1
            return 'Here is your %(obj)s.' % dict(obj=VendingMachine.item)
    def restock(self, restock):
        VendingMachine.stock += restock
        return 'Current %(item)s stock: %(stock)s.' % dict(item=VendingMachine.item, stock=VendingMachine.stock) 
    def deposit(self, money):
        if VendingMachine.stock == 0:
            return 'Machine is out of stock. Here is your $%(money)s.' % dict(money=money)
        else:
            VendingMachine.balance += money
            return 'Current balance: $%(balance)s.' % dict(balance=VendingMachine.balance)
# Q3.

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please.'
    >>> m.ask('please give up a teaspoon')
    'Thanks for asking, but I know not how to give up a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    def __init__(self, v):
        self.v = v
    
    def ask(self, *args):
        if len(args) == 1:
            said=args[0]
            if said == "please vend":
                return self.v.vend()
            elif said[0:6]== "please":
                return "Thanks for asking, but I know not how to" + what_you_said[6:]
            else:
                return "You must learn to say please."
        elif len(args) ==2:
            said=args[0]
            money=args[1]
            return self.v.deposit(money)

# Q4.

class Account(object):
    """A bank balance that allows deposits and withdrawals.

    >>> john = balance('John')
    >>> jack = balance('Jack')
    >>> john.deposit(10)
    10
    >>> john.deposit(5)
    15
    >>> john.interest
    0.02
    >>> jack.deposit(7)
    7
    >>> jack.deposit(5)
    12
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the balance balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the balance balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class SecureAccount(Account):
    def __init__(self, account_holder, password):
        self.balance = 0
        self.holder = account_holder
        self.password = password
    def password(self, *args):
        password = args
    def deposit(self, amount):
        Account.deposit(self, amount)
    def secure_withdraw(self, amount, password):
        i = 3
        if args == None:
             return 'This Account requires a password to withdraw'
        if i == 0:
            return 'This Account is locked'        
        elif i > 0 and password is not args :
            i -= 1
            return 'Incorrect Password'
        elif password is args and i > 0:
            i = 3
            return Account.withdraw(self, amount)        

import unittest

class SecureAccountTest(unittest.TestCase):
    """Test the Securebalance class."""

    def setUp(self):
        self.Account = SecureAccount('Alyssa P. Hacker', 'p4ssw0rd')

    def test_secure(self):
        acc = self.Account
        acc.deposit(1000)
        self.assertEqual(acc.Account, 1000, 'Bank error! Incorrect Account')
        self.assertEqual(acc.withdraw(100),
                         'This Account requires a password to withdraw')
        self.assertEqual(acc.secure_withdraw(100, 'p4ssw0rd'), 900,
                         "Didn't withdraw 100")
        self.assertEqual(acc.secure_withdraw(100, 'h4x0r'), 'Incorrect password')
        self.assertEqual(acc.secure_withdraw(100, 'n00b'), 'Incorrect password')
        self.assertEqual(acc.secure_withdraw(100, '1337'), 'Incorrect password')
        self.assertEqual(acc.Account, 900, 'Withdrew with bad password')
        self.assertEqual(acc.secure_withdraw(100, 'p4ssw0rd'),
                         'This Account is locked')
        self.assertEqual(acc.Account, 900, 'Withdrew from locked Account')

# Q5.

"*** YOUR CODE HERE ***"

class MoreSecureAccountTest(SecureAccountTest):
    """Test the MoreSecureAccount class."""

    def setUp(self):
        self.Account = MoreSecureAccount('Alyssa P. Hacker', 'p4ssw0rd')
