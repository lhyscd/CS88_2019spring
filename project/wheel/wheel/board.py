"""Board class for Wheel of Fortune game."""

class Board:
    """Board for Wheel of Fortune with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        "*** YOUR CODE HERE ***"
        self.secret_object = secret
        self.secret_list = [str(char) for char in secret.word]
        self.guesses_list = []
        self.word_list = ['_'] * len(self.secret_list)
        self.hits_list = []
        self.misses_list = []
        # END

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(self.secret_list)
        # END

    def word(self):
        """Return the current state of guessing the word as a list of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        "*** YOUR CODE HERE ***"
        return self.word_list
        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        "*** YOUR CODE HERE ***"
        return self.guesses_list
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        "*** YOUR CODE HERE ***"
        return self.hits_list
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        "*** YOUR CODE HERE ***"
        return self.misses_list
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        # BEGIN
        "*** YOUR CODE HERE ***"
        self.guesses_list.append(char)
        if char in self.secret_list:
            self.hits_list.append(char)
            correct_list = self.secret_object.match(char)
            for idx in correct_list:
                self.word_list[idx] = char
            return len(correct_list)
        else:
            self.misses_list.append(char)
            return 0
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        "*** YOUR CODE HERE ***"
        if self.secret_list == self.word_list:
            return True
        else:
            return False
        # END

    def display(self):
        print(self.word())
        print("Guessed chars: ", self.guesses())
