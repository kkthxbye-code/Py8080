from operations import *


class Instruction(object):
    def __init__(self, opcode):
        self._instructions = {
            0x0: {"length": 1, "operation": nop},
            0x05: {"length": 1, "operation": dcr},
            0x06: {"length": 2, "operation": mvi},
            0x0e: {"length": 2, "operation": mvi},
            0x11: {"length": 3, "operation": lxi_w},
            0x13: {"length": 1, "operation": inx_w},
            0x21: {"length": 3, "operation": lxi_w},
            0x16: {"length": 2, "operation": mvi},
            0x1A: {"length": 1, "operation": ldax},
            0x1e: {"length": 2, "operation": mvi},
            0x23: {"length": 1, "operation": inx_w},
            0x26: {"length": 2, "operation": mvi},
            0xc2: {"length": 3, "operation": jnz},
            0x2e: {"length": 2, "operation": mvi},
            0x77: {"length": 1, "operation": mov_to_addr},
            0xC3: {"length": 3, "operation": jmp},
            0xCD: {"length": 3, "operation": call},
            0x31: {"length": 3, "operation": lxi},
        }

        if opcode not in self._instructions:
            raise NotImplementedError("Instruction {} not implemented".format(hex(opcode)))

        self.opcode = opcode
        self.length = self._instructions[opcode]['length']
        self.operation = self._instructions[opcode]['operation']

