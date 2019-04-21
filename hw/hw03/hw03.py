######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 10)  # 4 * 3 * 2 * 1 # Only n times!!
    24
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    if k > n:
        k = n
    num = 1
    for _ in range(k):
        num *= n
        n -= 1
    return num


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    "*** YOUR CODE HERE ***"
    for i in lst:
        if i != 0:
            return i
    return


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
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
    "*** YOUR CODE HERE ***"
    len_num = 1
    print(n)
    while n != 1:
        if n%2 == 0: 
            n /= 2 
        else: 
            n = n*3+1
        len_num += 1
        print(int(n))
    return len_num


def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    "*** YOUR CODE HERE ***"
    return 'even' if x%2 == 0 else 'odd'


def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    "*** YOUR CODE HERE ***"
    return [odd_even(item) for item in s]


def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    "*** YOUR CODE HERE ***"
    string = ''
    if pair[0] == 0:
        string += 'Male '
    else:
        string += 'Female '
    if pair[1] == 10:
        string += '100+'
    else:
        string = string + str(pair[1]*10) + '-' + str(pair[1]*10+9)
    return string
    

def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """ 
    "*** YOUR CODE HERE ***"
    tmp = []
    for pair in list_of_sex_age_pairs:
        tmp.append(decode_helper(pair))
    return tmp

