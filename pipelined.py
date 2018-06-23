from generic.abstractcomponents import Mux, Port, RegisterFile, ConnectionLine, HardcodedValueLine
from generic.ALU import ALU
import pipelined.gui

if __name__ == '__main__':
    registers = RegisterFile(32, nr_outputs=2)

    p1 = Port(registers, 0)
    p2 = Port(registers, 1)
    hardcoded0 = HardcodedValueLine(0)
    hardcoded4 = HardcodedValueLine(4)

    mux_s1 = Mux([p1, hardcoded0], None)
    mux_s2 = Mux([p2, hardcoded4], None)

    alu    = ALU(mux_s1, mux_s2)

    models = [registers, mux_s1, mux_s2, alu, p1, p2, hardcoded0, hardcoded4]

    pipelined.gui.GUI(models)
