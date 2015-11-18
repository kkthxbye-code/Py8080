from state import State


def nop(state):
    pass


def jmp(state):
    """
    :type state: State
    """
    address = state.ram().read_word(state.registers().ip()-2)

    state.registers().move_ip(address)


def mvi(state):
    """
    :type state: State
    """
    opcode = state.ram().read_byte(state.registers().ip()-2)
    dst = (opcode >> 3) & 0x07

    value = state.ram().read_byte(state.registers().ip()-1)
    state.registers().set_register(dst, value)


def lxi(state):
    """
    :type state: State
    """
    address = state.ram().read_word(state.registers().ip()-2)

    state.stack().set_position(address)


def lxi_w(state):
    """
    :type state: State
    """
    opcode = state.ram().read_byte(state.registers().ip()-3)
    dst = (opcode >> 4) & 0x3

    value = state.ram().read_word(state.registers().ip()-2)
    state.registers().set_register_word(dst, value)


def call(state):
    """
    :type state: State
    """
    address = state.ram().read_word(state.registers().ip()-2)
    state.stack().push(state.registers().ip())
    state.registers().move_ip(address)

def ldax(state):
    """
    :type state: State
    """
    opcode = state.ram().read_byte(state.registers().ip()-1)
    dst = 7
    src = (opcode >> 4) & 0x3

    address = state.registers().get_register_word(src)
    data = state.ram().read_byte(address)

    state.registers().set_register(dst, data)

def mov_to_addr(state):
    """
    :type state: State
    """
    opcode = state.ram().read_byte(state.registers().ip()-1)

    dst = 2
    address = state.registers().get_register_word(dst)

    src = (opcode & 0x7)
    value = state.registers().get_register_byte(src)

    state.ram().write_byte(address, value)

def inx_w(state):
    """
    :type state: State
    """
    opcode = state.ram().read_byte(state.registers().ip()-1)

    dst = (opcode >> 4) & 0x3
    value = state.registers().get_register_word(dst)

    value += 1

    state.registers().set_register_word(dst, value)


def dcr(state):
    # TODO: FLAGS
    """
    :type state: State
    """
    opcode = state.ram().read_byte(state.registers().ip()-1)
    dst = (opcode >> 3) & 0x07

    value = state.registers().get_register_byte(dst)
    print value
    value -= 2
    print value

    overflow = value & (1 << (7)) != 0
    state.flags().set_sign(overflow)
    print overflow
    if overflow:
        value = abs(abs(value) - (1 << 8))

    state.flags().set_parity(value)
    state.flags().set_zero(value == 0)
    state.flags().set_carry(value & 0x100)

    state.registers().set_register_byte(dst, value)
    print value

    import sys
    sys.exit()

def jnz(state):
    """
    :type state: State
    """
    if not state.flags().get_zero():
        address = state.ram().read_word(state.registers().ip()-2)
        state.registers().move_ip(address)

        #state.dump_state()


