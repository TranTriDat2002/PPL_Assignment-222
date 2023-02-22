import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """main: function void()"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 202))
    
