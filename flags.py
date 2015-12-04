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

    def set_zero(self, value):
        zero = value == 0
        if zero:
            self._flags |= self.FLAG_ZERO
        else:
            self._flags &= ~self.FLAG_ZERO

    def set_acarry(self, original, intermediate):
        carry = ((1 ^ intermediate) ^ original) & 0x10

        if carry:
            self._flags |= self.FLAG_ACARRY
        else:
            self._flags &= ~self.FLAG_ACARRY

    def set_parity(self, value):
        parity = not sum([value & (1<<i) > 0 for i in range(8)]) % 2

        if parity:
            self._flags |= self.FLAG_PARITY
        else:
            self._flags &= ~self.FLAG_PARITY

    def set_carry(self, res, is_word=False):
        if is_word:
            carry = res > 0xffff
        else:
            carry = res > 0xff

        if carry:
            self._flags |= self.FLAG_CARRY
        else:
            self._flags &= ~self.FLAG_CARRY

    def set_carry_raw(self, value):
        if value:
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