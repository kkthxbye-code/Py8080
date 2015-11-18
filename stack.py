from memory import Memory

class Stack(object):
    def __init__(self, size):
        self._stack = Memory(size)
        self._sp = 0

    def push(self, word):
        self._sp -= 2
        self._stack.write_word(self._sp, word)

    def pop(self):
        self._sp += 2
        return self._stack.read_word(self._sp-2)

    def set_position(self, position):
        self._sp = position

    def position(self):
        return self._sp

    def __repr__(self):
        return str(self._stack)