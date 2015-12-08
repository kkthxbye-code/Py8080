from state import State


def nop(state):
    pass


def jmp(state):
    """
    :type state: State
    """
    address = state.memory().read_word(state.registers().ip() - 2)

    state.registers().move_ip(address)


def mvi(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 2)
    dst = (opcode >> 3) & 0x07

    value = state.memory().read_byte(state.registers().ip() - 1)
    state.registers().set_register(dst, value)

def mvi_m(state):
    """
    :type state: State
    """
    dst = 2
    address = state.registers().get_register_word(dst)

    value = state.memory().read_byte(state.registers().ip() - 1)

    state.memory().write_byte(address, value)


def lxi(state):
    """
    :type state: State
    """
    address = state.memory().read_word(state.registers().ip() - 2)

    state.stack().set_position(address)


def lxi_w(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 3)
    dst = (opcode >> 4) & 0x3

    value = state.memory().read_word(state.registers().ip() - 2)
    state.registers().set_register_word(dst, value)


def call(state):
    """
    :type state: State
    """
    address = state.memory().read_word(state.registers().ip() - 2)
    state.stack().push(state.registers().ip())
    state.registers().move_ip(address)


def push(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)
    src = (opcode >> 4) & 3

    address = state.registers().get_register_word(src)
    state.stack().push(address)


def push_psw(state):
    """
    :type state: State
    """
    lower = state.registers().get_register_byte(7) #A
    upper = state.flags().flags() #F
    value = (upper << 8) | lower

    state.stack().push(value)


def pop_psw(state):
    """
    :type state: State
    """
    value = state.stack().pop()

    state.registers().set_register_byte(7, value & 0x00ff)
    state.flags().set_flag((value & 0xff00) >> 8)


def lda(state):
    """
    :type state: State
    """
    address = state.memory().read_word(state.registers().ip() - 2)
    value = state.memory().read_byte(address)
    state.registers().set_register_byte(7, value)


def pop(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)
    dst = (opcode >> 4) & 3

    value = state.stack().pop()
    state.registers().set_register_word(dst, value)


def ldax(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)
    dst = 7
    src = (opcode >> 4) & 0x3

    address = state.registers().get_register_word(src)
    data = state.memory().read_byte(address)

    state.registers().set_register(dst, data)


def mov(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)
    dst = (opcode >> 3) & 0x7
    src = opcode & 0x7
    value = state.registers().get_register_byte(src)

    state.registers().set_register_byte(dst, value)

def mov_to_addr(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)

    dst = 2
    address = state.registers().get_register_word(dst)

    src = (opcode & 0x7)
    value = state.registers().get_register_byte(src)

    state.memory().write_byte(address, value)


def mov_from_addr(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)

    dst = (opcode >> 3) & 0x7
    src = 2

    address = state.registers().get_register_word(src)
    value = state.memory().read_byte(address)

    state.registers().set_register_byte(dst, value)


def inx_w(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)

    dst = (opcode >> 4) & 0x3
    value = state.registers().get_register_word(dst)

    value += 1
    value &= 0xffff # Overflow

    state.registers().set_register_word(dst, value)


def dcr(state):
    # TODO: FLAGS
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)
    dst = (opcode >> 3) & 0x07

    value = state.registers().get_register_byte(dst)

    temp = value - 1
    state.flags().set_acarry(value, temp) #TODO: This is broken

    temp = (temp & 0xff)

    underflow = temp > value

    state.flags().set_sign(underflow)

    value = temp

    state.flags().set_parity(value)
    state.flags().set_zero(value)
    state.flags().set_carry(value & 0x100)

    state.registers().set_register_byte(dst, value)


def jnz(state):
    """
    :type state: State
    """
    if not state.flags().get_zero():
        address = state.memory().read_word(state.registers().ip() - 2)
        state.registers().move_ip(address)


def ret(state):
    """
    :type state: State
    """
    address = state.stack().pop()
    state.registers().move_ip(address)


def cpi(state):
    """
    :type state: State
    """
    value = state.memory().read_byte(state.registers().ip() - 1)
    dst = state.registers().get_register_by_name("a")
    dst_value = state.registers().get_register_byte(dst)

    temp = dst_value - value
    temp = (temp & 0xff)

    underflow = temp > value

    state.flags().set_sign(underflow)
    value = temp

    state.flags().set_parity(value)
    state.flags().set_zero(value)
    state.flags().set_carry(value & 0x100)

def dad(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)
    reg = (opcode >> 4) & 0x3

    value = state.registers().get_register_word(reg)
    hl = state.registers().get_register_word(2)

    res = hl + value
    state.flags().set_carry(res, is_word=True)

    res = res & 0xffff

    state.registers().set_register_word(2, res)

def xchg(state):
    """
    :type state: State
    """
    de = state.registers().get_register_word(1)
    hl = state.registers().get_register_word(2)

    state.registers().set_register_word(1, hl)
    state.registers().set_register_word(2, de)

def out(state):
    """
    :type state: State
    """
    #TODO: Figure out what is needed regardning audio and shift registers
    value = state.memory().read_byte(state.registers().ip() - 1)

def rp(state):
    """
    :type state: State
    """
    if state.flags().get_parity():
        ret(state)

def rrc(state):
    """
    :type state: State
    """

    h = (state.registers().get_register_byte(7) & 1) << 7
    if h:
        state.flags().set_carry_raw(True)
    else:
        state.flags().set_carry_raw(False)

    state.registers().set_register_byte(7, state.registers().get_register_byte(7) & 0xFE >> 1 | h)

def ani(state):
    """
    :type state: State
    """
    value = state.memory().read_byte(state.registers().ip() - 1)
    orig = state.registers().get_register_byte(7)
    res = orig & value


    underflow = orig > res

    state.flags().set_sign(underflow)

    state.flags().set_zero(res)
    state.flags().set_carry(res)
    state.flags().set_acarry(orig, res)
    state.flags().set_parity(res)

    state.registers().set_register_byte(7, res)


def adi(state):
    """
    :type state: State
    """
    value = state.memory().read_byte(state.registers().ip() - 1)
    orig = state.registers().get_register_byte(7)
    res = orig + value


    underflow = orig > res

    state.flags().set_sign(underflow)

    state.flags().set_zero(res)
    state.flags().set_carry(res)
    state.flags().set_acarry(orig, res)
    state.flags().set_parity(res)

    state.registers().set_register_byte(7, res)


def rst(state):
    #TODO: This is wrong, fix it
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 2)
    address = ((opcode >> 3) & 0x7) << 3

    state.stack().push(state.registers().ip())
    state.registers().move_ip(address)


def sta_m(state):
    """
    :type state: State
    """
    address = state.memory().read_word(state.registers().ip() - 2)
    value = state.registers().get_register_byte(7)

    state.memory().write_byte(address, value)


def xra(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)

    dst = 7 #A
    src = opcode & 0x7

    reg1 = state.registers().get_register_byte(dst)
    reg2 = state.registers().get_register_byte(src)

    orig = reg1
    res = reg1 ^ reg2

    underflow = False

    state.flags().set_sign(underflow)

    state.flags().set_zero(res)
    state.flags().set_carry(res)
    state.flags().set_acarry(orig, res)
    state.flags().set_parity(res)

    state.registers().set_register_byte(dst, res)


def ana(state):
    """
    :type state: State
    """
    opcode = state.memory().read_byte(state.registers().ip() - 1)

    dst = 7 #A
    src = opcode & 0x7

    reg1 = state.registers().get_register_byte(dst)
    reg2 = state.registers().get_register_byte(src)
    orig = reg1

    res = reg1 & reg2

    underflow = False

    state.flags().set_sign(underflow)

    state.flags().set_zero(res)
    state.flags().set_carry(res)
    state.flags().set_acarry(orig, res)
    state.flags().set_parity(res)

    state.registers().set_register_byte(dst, res)



def fb(state):
    """
    :type state: State
    """
    #TODO: ENABLE INTERRUPTS
    pass