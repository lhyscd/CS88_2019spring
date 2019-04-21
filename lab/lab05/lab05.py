######################
# Required Questions #
######################

def bad_list_flattener(lst1, lst2):
    """
    Flattens both lst1 and lst2, and returns the 
    concatenation of the two flattened lists. Flattening 
    a list means to collapse the list into one 
    dimension (like np.flatten).
    >>> girls = [['Rachel', 'Green'], ['Phoebe', 'Buffay']]
    >>> boys = [['Ross', 'Geller'], ['Chandler', 'Bing']]
    >>> bad_list_flattener(girls, boys)
    ['Rachel', 'Green', 'Phoebe', 'Buffay', 'Ross', 'Geller', 'Chandler', 'Bing']
    >>> cats = [['Persian'], ['British', 'Shorthair']]
    >>> dogs = [['Golden', 'Retriever']]
    >>> bad_list_flattener(dogs, cats)
    ['Golden', 'Retriever', 'Persian', 'British', 'Shorthair']
    """
    newlist1 = []
    newlist2 = []
    for inner_lst in lst1:
        for item in inner_lst:
            newlist1.append(item)
    for inner_lst in lst2:
        for item in inner_lst:
            newlist2.append(item)
    return newlist1 + newlist2


def is_palindrome(lst):
    """ Returns True if the list is a palindrome. A palindrome is a list 
    that reads the same forwards as backwards
    >>> is_palindrome([1, 2, 3, 4, 5])
    False
    >>> is_palindrome(["p", "a", "l", "i", "n", "d", "r", "o", "m", "e"])
    False
    >>> is_palindrome([True, False, True])
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome(["racecar", "racecar"])
    True
    >>> is_palindrome(["r", "a", "c", "e", "c", "a", "r"])
    True
    """
    "*** YOUR CODE HERE ***"
    if len(lst)<=1:
        return True
    elif lst[0] == lst[-1]:
        return is_palindrome(lst[1:-1])
    else:
        return False


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if b <= 0:
        return c
    else:
        return a + ab_plus_c(a, b-1, c)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    upper = min([a,b])
    num = 1
    for i in range(1,upper+1):
        if a % i == 0 and b % i == 0:
            num = i
    return num



# Iterative solution, if you're curious
def gcd_iter(a, b):
    """Returns the greatest common divisor of a and b, using iteration.

    >>> gcd_iter(34, 19)
    1
    >>> gcd_iter(39, 91)
    13
    >>> gcd_iter(20, 30)
    10
    >>> gcd_iter(40, 40)
    40
    """
    if a < b:
        a, b = b, a
    while a > b and not a % b == 0:
        a, b = b, a % b
    return b



def first(s):
    """Return the first element in a sequence."""
    return s[0]

def rest(s):
    """Return all elements in a sequence after the first"""
    return s[1:]

def remove(x, s):
    """Remove first element equal to x from sequence s.

    >>> remove(1,[])
    []
    >>> remove(1,[1])
    []
    >>> remove(1,[1,1])
    [1]
    >>> remove(1,[2,1])
    [2]
    >>> remove(1,[3,1,2])
    [3, 2]
    >>> remove(1,[3,1,2,1])
    [3, 2, 1]
    >>> remove(5, [3, 5, 2, 5, 11])
    [3, 2, 5, 11]
    """
    "*** YOUR CODE HERE ***"
    for idx in range(len(s)):
        if s[idx] == x:
            return s[:idx] + s[idx+1:]
    return s


# Recursive Min Sort

# Helper function
def rmin(s):
    """Return the minimum value in a sequence."""
    if len(s) == 1:
        return first(s)
    else:
        return min(first(s), rmin(rest(s)))

def rsort(s):
    """Sort sequence s in ascending order.
    
    >>> rsort([])
    []
    >>> rsort([1])
    [1]
    >>> rsort([1, 1, 1])
    [1, 1, 1]
    >>> rsort([1, 2, 3])
    [1, 2, 3]
    >>> rsort([3, 2, 1])
    [1, 2, 3]
    >>> rsort([1, 2, 1])
    [1, 1, 2]
    >>> rsort([1,2,3, 2, 1])
    [1, 1, 2, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    if len(s)<=1:
        return s
    else:
        tmp_num = rmin(s)
        tmp_s = remove(tmp_num,s)
        return [tmp_num] + rsort(tmp_s)

