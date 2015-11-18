from ram import Ram
from stack import Stack
from registers import Registers

class State(object):
    def __init__(self, ram=Ram(32*1024), stack=Stack(32*1024), registers=Registers()):
        self._ram = ram
        self._stack = stack
        self._registers = registers

    def ram(self):
        return self._ram

    def stack(self):
        return self._stack

    def registers(self):
        return self._registers

    def dump_state(self):
        print "Instruction Pointer: {}".format(hex(self.registers().ip()))
        print "Stack Pointer: {}".format(hex(self.stack().position()))

        for idx, value in enumerate(self._registers.registers()):
            if value is not None:
                print "Register {}: {}".format(idx, hex(value))