test = {
  'name': 'Question 1.1',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab03 import *
          >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
          >>> tax(fruitCart, 10)
          [('apple', 0.55, 3), ('banana', 0.275, 4)]
          >>> calCart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
          >>> tax(calCart, 100)
          [('oski', 2000.0, 1), ('go', 2.5, 2), ('bears', 7.0, 2)]
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
