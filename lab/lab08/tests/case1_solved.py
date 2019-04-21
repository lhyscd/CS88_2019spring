test = {
  'name': 'Case 1 Solved',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]  
          >>> y = x[:]
          >>> y[0] = 5
          >>> y
          [5, 2, 3, 4]
          >>> x 
          [1, 2, 3, 4]
          >>> z = list(x) 
          >>> z[0] = 6
          >>> z
          [6, 2, 3, 4]
          >>> x 
          [1, 2, 3, 4]
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
