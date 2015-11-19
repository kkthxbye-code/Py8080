from state import State
from instructions import Instruction

class i8080(object):
    def __init__(self):
        self._state = State()

    def load(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
            self._state.memory().write(0, list(ord(x) for x in data))

    def state(self):
        return self._state

    def next_instruction(self):
        opcode = self._state.memory().read_byte(self._state.registers().ip())

        try:
            instruction = Instruction(opcode)
        except NotImplementedError as e:
            print e
            self._state.dump_state()
            print "n: {}".format(self.c)
            import sys
            sys.exit()

        self._state.registers().increment_ip(instruction.length)

        instruction.operation(self._state)

        #self._state.dump_state()

    def run(self):
        self.c = 0
        while True:
            self.c += 1
            #raw_input()
            #if c > 1632:
            #    raw_input()
            self.next_instruction()


machine = i8080()
machine.load("invaders")
machine.run()

#print machine.state().ram().read(0, 100)