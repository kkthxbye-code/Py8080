class Memory(object):
    def __init__(self, size):
        self._memory = [0]*size

    def read_byte(self, position):
        return self._memory[position]

    def write_byte(self, position, byte):
        self._memory[position] = byte

    def write_word(self, position, word):
        self._memory[position] = word & 0x00ff
        self._memory[position+1] = (word & 0xff00) >> 8

    def read_word(self, position):
        lower = self._memory[position]
        upper = self._memory[position+1]
        return (upper<<8) | lower

    def read(self, start, l):
        return self._memory[start:start+l]

    def write(self, position, bytes):
        for idx, byte in enumerate(bytes):
            self.write_byte(position+idx, byte)

    def get_memory(self):
        return self._memory

    def __repr__(self):
        return str(self._memory)