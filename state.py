from memory import Memory
from stack import Stack
from registers import Registers
from flags import Flags

class State(object):
    def __init__(self, memory=Memory(32*1024), stack=Stack(32*1024), registers=Registers(), flags=Flags()):
        self._memory = memory
        self._stack = stack
        self._registers = registers
        self._flags = flags

    def memory(self):
        return self._memory

    def stack(self):
        return self._stack

    def registers(self):
        return self._registers

    def flags(self):
        return self._flags

    def dump_state(self):
        #TODO: Make this prettier/better
        print "Instruction Pointer: {}".format(hex(self.registers().ip()))
        print "Stack Pointer: {}".format(hex(self.stack().position()))

        regs = self._registers.registers()
        print "A: {}".format(hex(regs[7]))
        print "F: {}".format(hex(self.flags().flags()))

        print "B: {}".format(hex(regs[0]))
        print "C: {}".format(hex(regs[1]))
        print "D: {}".format(hex(regs[2]))
        print "E: {}".format(hex(regs[3]))
        print "H: {}".format(hex(regs[4]))
        print "L: {}".format(hex(regs[5]))

        print "=======FLAGS========"
        print "Zero: {}".format(int(self.flags().get_zero()))
        print "Sign: {}".format(int(self.flags().get_sign()))
        print "Parity: {}".format(int(self.flags().get_parity()))
        print "Carry: {}".format(int(self.flags().get_carry()))
        print "Half-Carry: {}".format(int(self.flags().get_acarry()))

        #print len(self.memory()._memory[0x2400:0x3fff])
