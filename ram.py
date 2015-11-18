class Ram(object):
    def __init__(self, size):
        self._ram = [0]*size

    def read_byte(self, position):
        return self._ram[position]

    def write_byte(self, position, byte):
        self._ram[position] = byte

    def write_word(self, position, word):
        self._ram[position] = word & 0x00ff
        self._ram[position+1] = (word & 0xff00) >> 8

    def read_word(self, position):
        lower = self._ram[position]
        upper = self._ram[position+1]
        return (upper<<8) | lower

    def read(self, start, l):
        return self._ram[start:start+l]

    def write(self, position, bytes):
        for idx, byte in enumerate(bytes):
            self.write_byte(position+idx, byte)

    def __repr__(self):
        return str(self._ram)