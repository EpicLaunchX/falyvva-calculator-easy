import unittest

from models import Operands


class TestOperands(unittest.TestCase):
    def test_operand_type(self):
        operands = Operands(2, 3)
        self.assertIsInstance(operands.first_operand,int)
        self.assertIsInstance(operands.second_operand,int)


if __name__ == '__main__':
    unittest.main()