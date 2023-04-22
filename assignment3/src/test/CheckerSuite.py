import unittest
from TestUtils import TestChecker
from AST import *

from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """a: integer;
        b: integer;
        a:integer;
        main: function void () {
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 400))