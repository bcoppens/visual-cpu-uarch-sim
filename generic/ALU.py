from enum import Enum

""" A 32-bit ALU """

class Operation(Enum):
  ADD  = 0
  SUB  = 1
  RSUB = 2
  MUL  = 3
  DIV  = 4
  AND  = 5
  OR   = 6
  XOR  = 7
  SLL  = 8
  SRL  = 9
  SRA  = 10
  S1   = 11
  S2   = 12
  S2S1 = 13 # returns ( S2[15:0] << 16 ) | S1[15:0]

class ALU:
  def __init__(self, S1, S2):
    self.S1 = S1
    self.S2 = S2
    self.operation = None
    self.output = None

  def result(self):
    if   self.operation == Operation.ADD:
      return self.S1.result() + self.S2.result()
    elif self.operation == Operation.SUB:
      return self.S1.result() - self.S2.result()
    else:
      assert False
