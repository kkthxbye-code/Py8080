from memory import Memory
from stack import Stack
from registers import Registers
from flags import Flags
import pygame
import random

class State(object):
    def __init__(self, memory=Memory(32*1024), stack=Stack(32*1024), registers=Registers(), flags=Flags()):
        self._memory = memory
        self._stack = stack
        self._registers = registers
        self._flags = flags

        self.width = 224
        self.height = 256

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

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


    def draw_screen(self):
        video = []

        for x in self.memory()._memory[0x2400:0x4000]:
            for y in range(0, 8):
                if x & (1 << y):
                    video.append(1)
                else:
                    video.append(0)

        counter = 0
        for i in range(self.width):
            for j in reversed(range(self.height)):
                if video[counter]:
                    self.screen.set_at((i, j), (255, 255, 255))
                counter += 1

        pygame.display.flip()