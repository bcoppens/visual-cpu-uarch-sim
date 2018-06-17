from generic.abstractcomponents import Mux
from generic.ALU import ALU
import pipelined.gui

if __name__ == '__main__':
    mux_s1 = Mux([], None)
    mux_s2 = Mux([], None)
    alu    = ALU(mux_s1, mux_s2)
    models = [mux_s1, mux_s2, alu]
    print(pipelined.gui.mapModelsToViews(models))

    pipelined.gui.GUI()
