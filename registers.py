class Registers(object):
    def __init__(self):
        self._registers = [0] * 8
        self._ip = 0
        self._register_names = [
            "b",
            "c",
            "d",
            "e",
            "h",
            "l",
            None,
            "a"
        ]

    def sp(self):
        return self.get_register_byte(4)

    def ip(self):
        return self._ip

    def increment_ip(self, amount):
        self._ip += amount

    def move_ip(self, position):
        self._ip = position

    def get_register_byte(self, index):
        return self._registers[index]

    def set_register_byte(self, index, value):
        self._registers[index] = value

    def get_register_word(self, index):
        # TODO: This is way too hacky
        index *= 2

        lower = self._registers[index+1]
        upper = self._registers[index]
        return (upper << 8) | lower

    def set_register_word(self, index, value):
        # TODO: This is way too hacky
        index *= 2

        self._registers[index+1] = value & 0x00ff
        self._registers[index] = (value & 0xff00) >> 8

    def get_register_by_name(self, name):
        try:
            return self._register_names.index(name.lower())
        except ValueError:
            raise ValueError("Trying to look-up non-existant register")

    def get_register(self, index, is_word=False):
        if is_word:
            self.get_register_word(index)
        else:
            self.get_register_byte(index)

    def set_register(self, index, value, is_word=False):
        if is_word:
            self.set_register_word(index, value)
        else:
            self.set_register_byte(index, value)

    def registers(self):
        return self._registers