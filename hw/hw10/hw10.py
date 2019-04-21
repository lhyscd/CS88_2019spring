################
#### Person ####
################

class Person(object):
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __init__(self, name):
        self.name = name
        "*** YOUR CODE HERE ***"
        self.last_word = "hhh"

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        self.last_word = stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        "*** YOUR CODE HERE ***"
        return self.last_word


##############
#### Errors ####  
##############


class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    'error.py:12'

    """
    def __init__(self, line, file):
        "*** YOUR CODE HERE ***"
        self.file = file
        self.line = line

    def write(self):
        return self.file + ':' + str(self.line)

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "HW10.py")
    >>> err1.write()
    HW10.py:17 SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "HW10.py", 4)
    >>> err2.write()
    HW10.py:18 SyntaxError : EOL while scanning string literal

    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        "*** YOUR CODE HERE ***"
        Error.__init__(self, line, file)
        self.type = SyntaxError.type
        self.message = SyntaxError.msgs[code]

    def write(self):
        end = self.type + ' : ' + self.message
        "*** YOUR CODE HERE ***"
        print(self.file + ':' + str(self.line) + ' ' + end)

    def add_code(self, code, msg):
        "*** YOUR CODE HERE ***"
        SyntaxError.msgs[code] = msg

class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "HW10.py")
    >>> err1.write()
    HW10.py:273 ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        "*** YOUR CODE HERE ***"
        Error.__init__(self, line, file)
        self.type = ZeroDivisionError.type
        self.message = message

    def write(self):
        end = self.type + ' : ' + self.message
        "*** YOUR CODE HERE ***"
        print(self.file + ':' + str(self.line) + ' ' + end)

