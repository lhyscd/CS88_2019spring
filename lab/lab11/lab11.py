#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start
        self.num = start
        self.end = end

    def __next__(self):
        "*** YOUR CODE HERE ***"
        rtmp = self.num
        self.num += 1
        if self.num > self.end + 1:
            self.num = self.start
            raise StopIteration
        return rtmp

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        return self


# Q3
class Str:
    "*** YOUR CODE HERE ***"
    def __init__(self, string):
        self.string = string
        self.idx = 0

    def __next__(self):
        idx = self.idx
        self.idx += 1
        try:
            return self.string[idx]
        except:
            raise StopIteration

    def __iter__(self):
        return self

##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n > -1:
        yield n
        n -= 1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        while self.n > -1:
            yield self.n
            self.n -= 1

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield int(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        yield int(n)