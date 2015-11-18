class Flags(object):
    def __init__(self):
        self._flags = 0
        self.FLAG_SIGN = 1 << 7
        self.FLAG_ZERO = 1 << 6
        self.FLAG_ACARRY = 1 << 4
        self.FLAG_PARITY = 1 << 2
        self.FLAG_CARRY = 1 << 0

        self._flags |= 1 << 1

    def set_sign(self, on=True):
        if on:
            self._flags |= self.FLAG_SIGN
        else:
            self._flags &= ~self.FLAG_SIGN

    def set_zero(self, on=True):
        if on:
            self._flags |= self.FLAG_ZERO
        else:
            self._flags &= ~self.FLAG_ZERO


    def set_acarry(self, on=True):
        if on:
            self._flags |= self.FLAG_ACARRY
        else:
            self._flags &= ~self.FLAG_ACARRY

    def set_parity(self, value):
        self._flags |= not sum([value & (1<<i) > 0 for i in range(8)]) % 2

        """
        if on:
            self._flags |= self.FLAG_PARITY
        else:
            self._flags &= ~self.FLAG_PARITY"""


    def set_carry(self, on=True):
        if on:
            self._flags |= self.FLAG_CARRY
        else:
            self._flags &= ~self.FLAG_CARRY

    def get_sign(self):
        return bool(self._flags & self.FLAG_SIGN)

    def get_zero(self):
        return bool(self._flags & self.FLAG_ZERO)

    def get_acarry(self):
        return bool(self._flags & self.FLAG_ACARRY)

    def get_parity(self):
        return bool(self._flags & self.FLAG_PARITY)

    def get_carry(self):
        return bool(self._flags & self.FLAG_CARRY)

    def set_flag(self, value):
        self._flags = value

    def flags(self):
        return self._flags

    def __repr__(self):
        return bin(self._flags)