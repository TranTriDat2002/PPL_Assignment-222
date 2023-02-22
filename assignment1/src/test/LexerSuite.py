import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_comment_block(self):
        self.assertTrue(TestLexer.test("/*This code is inside a comment block*/abc", "abc,<EOF>", 101))

    def test_comment_line(self):
        self.assertTrue(TestLexer.test("// This code is inside a comment block*/ \n abc", "abc,<EOF>", 102))
    
    
        
