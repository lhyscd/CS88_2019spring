test = {
  'name': 'Case 2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> y = x[:]
          >>> y[0][1] = 'z'
          >>> y
          [[0, 'z'], [1, 'b'], [2, 'c']]
          >>> x
          [[0, 'z'], [1, 'b'], [2, 'c']]
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> z = list(x)
          >>> z[0][1] = 'z'
          >>> z
          [[0, 'z'], [1, 'b'], [2, 'c']]
          >>> x
          [[0, 'z'], [1, 'b'], [2, 'c']]
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
