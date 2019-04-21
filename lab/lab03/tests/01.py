test = {
  'name': 'Question 1.2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab03 import *
          >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
          >>> taxedFruit = tax(fruitCart, 10)
          >>> cartSum(taxedFruit)
          2.75
          >>> calCart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
          >>> taxedCal = tax(calCart, 100)
          >>> cartSum(taxedCal)
          2019.0
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
