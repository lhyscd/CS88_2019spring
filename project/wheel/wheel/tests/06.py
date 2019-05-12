test = {
  'name': 'Problem 6',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c2.guess(b2) # Case 3.1
          'e'
          >>> b2.guess(c2.guess(b2)) # Case 3.1
          2
          >>> c2.guess(b2) # Case 3.2
          'h'
          >>> b2.guess(c2.guess(b2)) # Case 3.2
          1
          >>> c2.guess(b2) # Case 3.3
          'r'
          >>> b2.guess(c2.guess(b2)) # Case 3.3
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
