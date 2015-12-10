from state import State
from instructions import instructions

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
            try:
                instruction = instructions[opcode]
            except:
                raise NotImplementedError("Instruction {} not implemented".format(hex(opcode)))

            self._state.registers().increment_ip(instruction["length"])
            instruction['operation'](self._state)
            return True
        except NotImplementedError as e:
            print "n: {}".format(self.c)
            self._state.dump_state()
            raw_input()
            raise NotImplementedError(e)
            return False

    def run(self):
        self.c = 0
        while True:
            #raw_input()
            self.process_interrupt()
            self.c += 1

            if not self.next_instruction():
                break

            if self.c == 1001:
                print self.state().cycle_count
                raw_input()


    def process_interrupt(self):
        if self.state().cycle_count > 16667:
            self.state().cycle_count -= 16667

            if self.state().last_interrupt == 0x10:
                self.state().last_interrupt = 0x08
                self.state().draw_screen()
            else:
                self.state().last_interrupt = 0x10

            if self.state().IE:
                self.state().cause_interrupt()

machine = i8080()
machine.load("invaders")
machine.run()
