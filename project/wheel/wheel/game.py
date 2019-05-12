from secret import SecretWord
from board import Board

class Game:
    """Run an entire game.

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess currect letters
       - returns final board
    winner returns the player who picked the last letter.
    """
    def __init__(self, picker, guessers):
        # BEGIN
        "*** YOUR CODE HERE ***"
        self.picker = picker
        self.guessers = guessers
        self.winner = None
        # self.secret_word = SecretWord(picker.pick_word())
        # END

    def play(self, verbose=True):
        # BEGIN
        "*** YOUR CODE HERE ***"
        secret_word = SecretWord(self.picker.pick_word())
        board = Board(secret_word)

        g_idx = 0
        while not board.done():
            guess_char = self.guessers[g_idx].guess(board)
            correct_num = board.guess(guess_char)
            if not correct_num:
                g_idx += 1
                if g_idx == len(self.guessers):
                    g_idx = 0

        self.winner = self.guessers[g_idx]
        return board
        # END

    def winner(self):
        # BEGIN
        "*** YOUR CODE HERE ***"
        return self.winner.name
        # END
