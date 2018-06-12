from enum import Enum

class Opcode(Enum): # RV32I for now
  LUI     = 0
  AUIPC   = 1
  JAL     = 2
  JALR    = 3
  BRANCH  = 4

  LOAD    = 10

  STORE   = 15

  OP_IMM  = 18

  OP      = 27

  MISCMEM = 37

  SYSTEM  = 39

class InstructionType(Enum): # RV32I for now
  LUI     = 0
  AUIPC   = 1
  JAL     = 2
  JALR    = 3
  BEQ     = 4
  BNE     = 5
  BLT     = 6
  BGE     = 7
  BLTU    = 8
  BGEU    = 9
  LB      = 10
  LH      = 11
  LW      = 12
  LBU     = 13
  LHU     = 14
  SB      = 15
  SH      = 16
  SW      = 17
  ADDI    = 18
  SLTI    = 19
  SLTIU   = 20
  XORI    = 21
  ORI     = 22
  ANDI    = 23
  SLLI    = 24
  SRLI    = 25
  SRAI    = 26
  ADD     = 27
  SUB     = 28
  SLL     = 29
  SLT     = 30
  SLTU    = 31
  XOR     = 32
  SRL     = 33
  SRA     = 34
  OR      = 35
  AND     = 36
  FENCE   = 37
  FENCE_I = 38
  ECALL   = 39
  EBREAK  = 40
  CSRRW   = 41
  CSRRS   = 42
  CSRRC   = 43
  CSRRWI  = 44
  CSRRSI  = 45
  CSRRCI  = 46

class Instruction:
  def __init__(self, opcode, type):
    self.opcode = opcode
    self.type = type
  def __str__(self):
    return str(self.type)

class LUI(Instruction):
  def __init__(self):
    super().__init__(Opcode.LUI, InstructionType.LUI)

class AUIPC(Instruction):
  def __init__(self):
    super().__init__(Opcode.AUIPC, InstructionType.AUIPC)

class JAL(Instruction):
  def __init__(self):
    super().__init__(Opcode.JAL, InstructionType.JAL)

class JALR(Instruction):
  def __init__(self):
    super().__init__(Opcode.JALR, InstructionType.JALR)

class BRANCH(Instruction):
  def __init__(self):
    super().__init__(Opcode.BRANCH, None)

class LOAD(Instruction):
  def __init__(self):
    super().__init__(Opcode.LOAD, None)

class STORE(Instruction):
  def __init__(self):
    super().__init__(Opcode.STORE, None)

class OP_IMM(Instruction):
  def __init__(self, type, rd, rs1, imm):
    super().__init__(Opcode.OP_IMM, type)
    self.rd = rd
    self.rs1 = rs1
    self.imm = imm

  def __str__(self):
    return "%s r%s, r%s, %s"  % (self.type, self.rd, self.rs1, self.imm)

class OP(Instruction):
  def __init__(self):
    super().__init__(Opcode.OP, None)

class MISCMEM(Instruction):
  def __init__(self):
    super().__init__(Opcode.MISCMEM, None)

class SYSTEM(Instruction):
  def __init__(self):
    super().__init__(Opcode.SYSTEM, None)


def get_opcode(bits):
  opcodes = {
    0b0110111: Opcode.LUI,
    0b0010111: Opcode.AUIPC,
    0b1101111: Opcode.JAL,
    0b1100111: Opcode.JALR,
    0b1100011: Opcode.BRANCH,
    0b0000011: Opcode.LOAD,
    0b0100011: Opcode.STORE,
    0b0010011: Opcode.OP_IMM,
    0b0110011: Opcode.OP,
    0b0001111: Opcode.MISCMEM,
    0b1110011: Opcode.SYSTEM,
  }

  opcode_bits = bits & 0b1111111
  
  return opcodes[opcode_bits]

def get_rd(bits):
  return (bits >> 7) & 0b11111

def get_func3(bits):
  return (bits >> 12) & 0b111

def get_rs1(bits):
  return (bits >> 15) & 0b11111

def get_rs2(bits):
  return (bits >> 20) & 0b11111

def decode_lui(bits):
  return LUI()

def decode_auipc(bits):
  return AUIPC()

def decode_jal(bits):
  return JAL()

def decode_jalr(bits):
  return JALR()

def decode_branch(bits):
  return BRANCH()

def decode_load(bits):
  return LOAD()

def decode_store(bits):
  return STORE()

def decode_op_imm(bits):
  types = {
    0b000: InstructionType.ADDI,
    0b010: InstructionType.SLTI,
    0b011: InstructionType.SLTIU,
    0b100: InstructionType.XORI,
    0b110: InstructionType.ORI,
    0b111: InstructionType.ANDI,
    0b001: InstructionType.SLLI,
    0b101: InstructionType.SRLI,
    0b101: InstructionType.SRAI
  }

  type = types[get_func3(bits)]
  imm = (bits >> 20) & 0b111111111111

  return OP_IMM( type, get_rd(bits), get_rs1(bits), imm )

def decode_op(bits):
  return OP()

def decode_miscmem(bits):
  return MISCMEM()

def decode_system(bits):
  return SYSTEM()

def decode(bits):
  opcode = get_opcode(bits)

  decoders = {
    Opcode.LUI: decode_lui,
    Opcode.AUIPC: decode_auipc,
    Opcode.JAL: decode_jal,
    Opcode.JALR: decode_jalr,
    Opcode.BRANCH: decode_branch,
    Opcode.LOAD: decode_load,
    Opcode.STORE: decode_store,
    Opcode.OP_IMM: decode_op_imm,
    Opcode.OP: decode_op,
    Opcode.MISCMEM: decode_miscmem,
    Opcode.SYSTEM: decode_system
  }

  #print(opcode)

  return decoders[opcode](bits)
