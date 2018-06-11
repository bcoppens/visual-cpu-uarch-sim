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

class Instruction(Enum): # RV32I for now
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
  
  print (bin(opcode_bits))

  return opcodes[opcode_bits]

def get_rd(bits):
  return (bits >> 7) & 0b1111

def decode_lui(bits):
  pass

def decode_auipc(bits):
  pass

def decode_jal(bits):
  pass

def decode_jalr(bits):
  pass

def decode_branch(bits):
  pass

def decode_load(bits):
  pass

def decode_store(bits):
  pass

def decode_op_imm(bits):
  pass

def decode_op(bits):
  print("OP")
  pass

def decode_miscmem(bits):
  pass

def decode_system(bits):
  pass

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

  decoders[opcode](bits)

decode(0b00000000010000100000010110011)
