class Line:
  pass

class HardcodedValueLine(Line):
  def __init__(self, value):
    self.value = value

  def result(self):
    return self.value

class ConnectionLine(Line):
  def __init__(self, input):
    self.input = Input

  def result(self):
    return self.input.result()

class Port:
  def __init__(self, input, port):
    self.input = input
    self.port = port

  def result(self):
    return self.input.result(self.port)

class RegisterFile:
  def __init__(self, nr_regs, nr_outputs):
    self.nr_regs = nr_regs
    self.nr_outputs = nr_outputs
    self.regs = [0] * nr_regs
    self.dest_reg = None

  def result(self, output):
    assert output < self.nr_outputs
    return self.regs[output]

  def nr_ports(self):
    return self.nr_outputs

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

