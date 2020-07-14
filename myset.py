class Set:
  def __init__(self):
    self.data = {}

  def add(self, value):
    self.data[value] = True

  def in_set(self, value):
    return value in self.data