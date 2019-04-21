test = {
  'name': 'primitive-expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 3
          3
          >>> 2 + 3
          5
          >>> -16 - -16
          0
          >>> 3 * 4 + 1
          13
          >>> 3 * (4 + 1)
          15
          >>> 2 ** 3
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> x = 4
          >>> 3 + x
          7
          >>> x + y
          Error
          >>> x, y = 1, 2
          >>> 3 + x
          4
          >>> x + y
          3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
