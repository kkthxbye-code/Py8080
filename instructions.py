from operations import *


class Instruction(object):
    def __init__(self, opcode):
        self._instructions = {
            0x00: {"length": 1, "operation": nop},
            0x01: {"length": 3, "operation": lxi_w},
            0x05: {"length": 1, "operation": dcr},
            0x06: {"length": 2, "operation": mvi},
            0x09: {"length": 1, "operation": dad},
            0x0d: {"length": 1, "operation": dcr},
            0x0e: {"length": 2, "operation": mvi},
            0x11: {"length": 3, "operation": lxi_w},
            0x13: {"length": 1, "operation": inx_w},
            0x16: {"length": 2, "operation": mvi},
            0x3e: {"length": 2, "operation": mvi},
            0x19: {"length": 1, "operation": dad},
            0x1A: {"length": 1, "operation": ldax},
            0x3a: {"length": 3, "operation": lda},
            0x1e: {"length": 2, "operation": mvi},
            0x21: {"length": 3, "operation": lxi_w},
            0x23: {"length": 1, "operation": inx_w},
            0x26: {"length": 2, "operation": mvi},
            0x29: {"length": 1, "operation": dad},
            0x2e: {"length": 2, "operation": mvi},
            0x31: {"length": 3, "operation": lxi},
            0x36: {"length": 2, "operation": mvi_m},
            0x56: {"length": 1, "operation": mov_from_addr},
            0x5e: {"length": 1, "operation": mov_from_addr},
            0x66: {"length": 1, "operation": mov_from_addr},
            0x6f: {"length": 1, "operation": mov},
            0x77: {"length": 1, "operation": mov_to_addr},
            0x7a: {"length": 1, "operation": mov},
            0x7c: {"length": 1, "operation": mov},
            0x7e: {"length": 1, "operation": mov_from_addr},
            0x7b: {"length": 1, "operation": mov_from_addr},
            0xc1: {"length": 1, "operation": pop},
            0xc2: {"length": 3, "operation": jnz},
            0xC3: {"length": 3, "operation": jmp},
            0xc5: {"length": 1, "operation": push},
            0xc9: {"length": 1, "operation": ret},
            0xcd: {"length": 3, "operation": call},
            0xd1: {"length": 1, "operation": pop},
            0xd3: {"length": 2, "operation": out},
            0xd5: {"length": 1, "operation": push},
            0xe1: {"length": 1, "operation": pop},
            0xe5: {"length": 1, "operation": push},
            0xeb: {"length": 1, "operation": xchg},
            0xfe: {"length": 2, "operation": cpi},
            0xf5: {"length": 1, "operation": push_psw},
            0x0f: {"length": 1, "operation": rrc},
            0xe6: {"length": 2, "operation": ani},
            0xc6: {"length": 2, "operation": adi},
            0xf1: {"length": 1, "operation": pop_psw},
            0x32: {"length": 3, "operation": sta_m},
            0xaf: {"length": 1, "operation": xra},
            0xfb: {"length": 1, "operation": ei},
            0xf3: {"length": 1, "operation": di}
            0xa7: {"length": 1, "operation": ana},

           # 0xc6: {"length": 1, "operation": rst}
            # 0xf0: {"length": 1, "operation": rp},

        }

        if opcode not in self._instructions:
            raise NotImplementedError("Instruction {} not implemented".format(hex(opcode)))

        self.opcode = opcode
        self.length = self._instructions[opcode]['length']
        self.operation = self._instructions[opcode]['operation']

