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
            self._state.registers().increment_ip(instruction.length)
            instruction.operation(self._state)
        except NotImplementedError as e:
            print "n: {}".format(self.c)
            self._state.dump_state()
            self.state().draw_screen()
            raw_input()
            raise NotImplementedError(e)

    def run(self):
        self.c = 0
        while True:
            self.c += 1
            self.next_instruction()

            if self.c > 42044:
                print hex(self.state().registers().get_register_byte(7))
                #print hex(self.state().registers().ip())
            #    self.state().dump_state()
            #    raw_input()
            #if self.c % 2000 == 0:
            #    self.state().draw_screen()


machine = i8080()
machine.load("invaders")
machine.run()