import unittest
from instructions import instructions
import state as emulator_state
class TestOperations(unittest.TestCase):
    def setUp(self):
        reload(emulator_state)
        self.state = emulator_state.State()

    def tearDown(self):
        del(self.state)

    def execute_next(self, instruction):
        self.state.registers().increment_ip(instruction["length"])
        instruction['operation'](self.state)

    def test_nop(self):
        old_memory = self.state.memory().get_memory()[:]
        self.execute_next(instructions[0x00])
        self.assertEqual(old_memory, self.state.memory().get_memory())

    def test_jmp(self):
        self.state.memory().write(0, [0xc3, 1, 0])
        self.execute_next(instructions[0xc3])
        self.assertEqual(1, self.state.registers().ip())

    def test_mvi_3e(self):
        self.state.memory().write(0, [0x3e, 10])
        self.execute_next(instructions[0x3e])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("A"))

    def test_mvi_06(self):
        self.state.memory().write(0, [0x06, 10])
        self.execute_next(instructions[0x06])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("B"))

    def test_mvi_0e(self):
        self.state.memory().write(0, [0x0e, 10])
        self.execute_next(instructions[0x0e])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("C"))

    def test_mvi_16(self):
        self.state.memory().write(0, [0x16, 10])
        self.execute_next(instructions[0x16])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("D"))

    def test_mvi_1e(self):
        self.state.memory().write(0, [0x1e, 10])
        self.execute_next(instructions[0x1e])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("E"))

    def test_mvi_26(self):
        self.state.memory().write(0, [0x26, 10])
        self.execute_next(instructions[0x26])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("H"))

    def test_mvi_2e(self):
        self.state.memory().write(0, [0x2e, 10])
        self.execute_next(instructions[0x2e])
        self.assertEqual(10, self.state.registers().get_register_byte_by_name("L"))

    def test_mvi_m(self):
        self.state.memory().write(0, [0x36, 5])
        self.state.registers().set_register_word(2, 15)

        self.execute_next(instructions[0x36])
        self.assertEqual(5, self.state.memory().read_byte(15))

    def test_lxi_01(self):
        self.state.memory().write(0, [0x01, 1, 1])
        self.execute_next(instructions[0x01])

        self.assertEqual(257, self.state.registers().get_register_word(0))


    def test_lxi_11(self):
        self.state.memory().write(0, [0x11, 1, 1])
        self.execute_next(instructions[0x11])

        self.assertEqual(257, self.state.registers().get_register_word(1))

    def test_lxi_21(self):
        self.state.memory().write(0, [0x21, 1, 1])
        self.execute_next(instructions[0x21])

        self.assertEqual(257, self.state.registers().get_register_word(2))

    def test_lxi_m(self):
        self.state.memory().write(0, [0x31, 1, 1])

        self.execute_next(instructions[0x31])
        self.assertEqual(257, self.state.stack().position())

    def test_call(self):
        self.state.memory().write(0, [0xcd, 1, 1])

        self.execute_next(instructions[0xcd])

        self.assertEqual(3, self.state.stack().pop())
        self.assertEqual(257, self.state.registers().ip())

    def test_push_c5(self):
        self.state.memory().write(0, [0xc5])
        self.state.registers().set_register_word(0, 257)
        self.execute_next(instructions[0xc5])

        self.assertEqual(257, self.state.stack().pop())

    def test_push_d5(self):
        self.state.memory().write(0, [0xd5])
        self.state.registers().set_register_word(1, 257)
        self.execute_next(instructions[0xd5])

        self.assertEqual(257, self.state.stack().pop())

    def test_push_e5(self):
        self.state.memory().write(0, [0xe5])
        self.state.registers().set_register_word(2, 257)
        self.execute_next(instructions[0xe5])

        self.assertEqual(257, self.state.stack().pop())


