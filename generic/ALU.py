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
