test = {
  'name': 'Restart',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class IteratorA:
          ...    def __init__(self):
          ...        self.start = 10
          ...    def __next__(self):
          ...        if self.start > 100:
          ...            raise StopIteration
          ...        self.start += 20
          ...        return self.start
          ...    def __iter__(self):
          ...        return self
          >>> iterator = IteratorA()
          >>> [num for num in iterator]
          [30, 50, 70, 90, 110]
          >>> [num for num in iterator]
          []
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
