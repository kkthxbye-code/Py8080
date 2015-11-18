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
        print "Instruction Pointer: {}".format(hex(self.registers().ip()))
        print "Stack Pointer: {}".format(hex(self.stack().position()))

        for idx, value in enumerate(self._registers.registers()):
            if value is not None:
                print "Register {}: {}".format(idx, hex(value))

        print "Flags {}".format(format(self.flags().flags(), '#010b'))