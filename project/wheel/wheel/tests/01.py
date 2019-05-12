test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = SecretWord('whodoneit')
          >>> len(s)
          9
          >>> s.match('o')
          [2, 4]
          >>> s.match('x')
          []
          >>> s
          <secret word>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> s = SecretWord('whodoneit')
          >>> len(s)
          9
          >>> s.match('o')
          [2, 4]
          >>> s.match('x')
          []
          >>> s
          <secret word>
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from secret import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
