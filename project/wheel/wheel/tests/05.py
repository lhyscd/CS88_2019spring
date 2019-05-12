test = {
  'name': 'Problem 5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> w = WordMunch("one two, Two. tHree")
          >>> w.words()
          ['one', 'three', 'two']
          >>> w.frequency()['o']
          2
          >>> key_of_max(w.frequency())
          'e'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> w = WordMunch("one two, Two. tHree")
          >>> w.words()
          ['one', 'three', 'two']
          >>> w.frequency()['o']
          2
          >>> key_of_max(w.frequency())
          'e'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c0.guess(b0) # Case 1.1
          'o'
          >>> b0.guess(c0.guess(b0)) # Case 1.1
          0
          >>> c0.guess(b0) # Case 1.2
          'e'
          >>> b0.guess(c0.guess(b0)) # Case 1.2
          2
          >>> c0.guess(b0) # Case 1.3
          'l'
          >>> b0.guess(c0.guess(b0)) # Case 1.3
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c1.guess(b1) # Case 2.1
          'e'
          >>> b1.guess(c1.guess(b1)) # Case 2.1
          2
          >>> c1.guess(b1) # Case 2.2
          'l'
          >>> b1.guess(c1.guess(b1)) # Case 2.2
          0
          >>> c1.guess(b1) # Case 2.3
          'h'
          >>> b1.guess(c1.guess(b1)) # Case 2.3
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c0.guess(b0) # Case 1.1
          'o'
          >>> b0.guess(c0.guess(b0)) # Case 1.1
          0
          >>> c0.guess(b0) # Case 1.2
          'e'
          >>> b0.guess(c0.guess(b0)) # Case 1.2
          2
          >>> c0.guess(b0) # Case 1.3
          'l'
          >>> b0.guess(c0.guess(b0)) # Case 1.3
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c1.guess(b1) # Case 2.1
          'e'
          >>> b1.guess(c1.guess(b1)) # Case 2.1
          2
          >>> c1.guess(b1) # Case 2.2
          'l'
          >>> b1.guess(c1.guess(b1)) # Case 2.2
          0
          >>> c1.guess(b1) # Case 2.3
          'h'
          >>> b1.guess(c1.guess(b1)) # Case 2.3
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from wordset import WordMunch
      >>> from wordset import WordSet
      >>> from board import Board
      >>> from secret import SecretWord
      >>> from utils import key_of_max
      >>> from player import ComputerPlayer
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
