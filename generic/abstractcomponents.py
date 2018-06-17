class RegisterFile:
  pass

class Memory:
  pass

class Mux:
  def __init__(self, inputs, selector):
    self.inputs = inputs
    self.selector = selector
    self.output = None

  def result(self):
    assert self.selector.result() < len(self.inputs)

    return self.inputs[self.selector.result()]

class Adder:
  pass

