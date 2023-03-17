import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # Program test

    # def test_program_vardecl(self):
    #     input = "x:integer;"
    #     expect = """Program([\n\tVarDecl(x, IntegerType)\n])"""
    #     self.assertTrue(TestAST.test(input, expect, 300))

    def test_program_funcdecl(self):
        input = "main:function void (){}"
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_program_vardecl_funcdecl(self):
        input = "x:integer;main:function void (){}"
        expect = """Program([\n\tVarDecl(x, IntegerType)\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_program_funcdecl_vardecl(self):
        input = "main:function void (){}x:integer;"
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_program_multi_vardecl(self):
        input = "x:integer;x:integer;x:integer;x:integer;"
        expect = """Program([\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_program_multi_funcdecl(self):
        input = "main:function void (){}main:function void (){}main:function void (){}main:function void (){}"
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_program_multi_funcdecl_vardecl(self):
        input = "main:function void (){}x:integer;x:integer;x:integer;main:function void (){}main:function void (){}x:integer;"
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 306))


    # Vardecl test

    def test_vardecl_atomic(self):
        input = "a:integer;b:float;c:string;d:boolean;"
        expect = """Program([\n\tVarDecl(a, IntegerType)\n\tVarDecl(b, FloatType)\n\tVarDecl(c, StringType)\n\tVarDecl(d, BooleanType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_vardecl_auto(self):
        input = "a,b,c:integer;b,b,b,b:auto;c,abc,a123,_abs:string;d:auto;"
        expect = """Program([\n\tVarDecl(a, IntegerType)\n\tVarDecl(b, IntegerType)\n\tVarDecl(c, IntegerType)\n\tVarDecl(b, AutoType)\n\tVarDecl(b, AutoType)\n\tVarDecl(b, AutoType)\n\tVarDecl(b, AutoType)\n\tVarDecl(c, StringType)\n\tVarDecl(abc, StringType)\n\tVarDecl(a123, StringType)\n\tVarDecl(_abs, StringType)\n\tVarDecl(d, AutoType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_vardecl_arraytype(self):
        input = "a,b,c:array[1]of integer;b,b,b:array[1,2]of float;c123:array[1,2,3]of string;d:array[4,1,3,4] of boolean;"
        expect = """Program([\n\tVarDecl(a, ArrayType([1], IntegerType))\n\tVarDecl(b, ArrayType([1], IntegerType))\n\tVarDecl(c, ArrayType([1], IntegerType))\n\tVarDecl(b, ArrayType([1, 2], FloatType))\n\tVarDecl(b, ArrayType([1, 2], FloatType))\n\tVarDecl(b, ArrayType([1, 2], FloatType))\n\tVarDecl(c123, ArrayType([1, 2, 3], StringType))\n\tVarDecl(d, ArrayType([4, 1, 3, 4], BooleanType))\n])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_full_vardecl_atomic(self):
        input = """x, y, z: integer = 1, 2, 3; a,a,c:float = 1.3, true, "abc";"""
        expect = """Program([\n\tVarDecl(x, IntegerType, IntegerLit(1))\n\tVarDecl(y, IntegerType, IntegerLit(2))\n\tVarDecl(z, IntegerType, IntegerLit(3))\n\tVarDecl(a, FloatType, FloatLit(1.3))\n\tVarDecl(a, FloatType, BooleanLit(True))\n\tVarDecl(c, FloatType, StringLit(abc))\n])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_full_vardecl_auto(self):
        input = """a:auto=1; """
        expect = """Program([\n\tVarDecl(a, AutoType, IntegerLit(1))\n])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_full_vardecl_array(self):
        input = """a:array[999,1000] of string = {1,2,3};b,c:array[9] of boolean = {},1; """
        expect = """Program([\n\tVarDecl(a, ArrayType([999, 1000], StringType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))\n\tVarDecl(b, ArrayType([9], BooleanType), ArrayLit([]))\n\tVarDecl(c, ArrayType([9], BooleanType), IntegerLit(1))\n])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;\n\n\na, b: float;"""
        expect = """Program([\n\tVarDecl(x, IntegerType, IntegerLit(1))\n\tVarDecl(y, IntegerType, IntegerLit(2))\n\tVarDecl(z, IntegerType, IntegerLit(3))\n\tVarDecl(a, FloatType)\n\tVarDecl(b, FloatType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    
    # Array declaration

    def test_array_declarations(self):
        input = """a:array[1] of integer; b:array[1,2,3,4,5,6,7,8,9,10] of string;"""
        expect = """Program([\n\tVarDecl(a, ArrayType([1], IntegerType))\n\tVarDecl(b, ArrayType([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], StringType))\n])"""
        self.assertTrue(TestAST.test(input, expect, 314))


    # Function declarations

    def test_funcdecl_no_para_no_inherit(self):
        input = """a:function boolean(){}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_funcdecl_inherit(self):
        input = """a:function boolean() inherit a123{}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [], a123, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_funcdecl_para_atomic(self):
        input = """a:function boolean(a:integer, b:float, c:string, d:boolean){}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [Param(a, IntegerType), Param(b, FloatType), Param(c, StringType), Param(d, BooleanType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_funcdecl_para_auto(self):
        input = """a:function boolean(a:auto,a:auto,a:auto,a:auto){}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [Param(a, AutoType), Param(a, AutoType), Param(a, AutoType), Param(a, AutoType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_funcdecl_para_array(self):
        input = """a:function boolean(a:array[1]of integer,a:array[1,2,3,4] of float){}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [Param(a, ArrayType([1], IntegerType)), Param(a, ArrayType([1, 2, 3, 4], FloatType))], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_funcdecl_para_inherit_out(self):
        input = """a:function boolean(a:integer, inherit b:float, out c:string, inherit out d:boolean){}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [Param(a, IntegerType), InheritParam(b, FloatType), OutParam(c, StringType), InheritOutParam(d, BooleanType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test_funcdecl_inherit_para_inherit(self):
        input = """a:function boolean(inherit a:integer) inherit a{}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [InheritParam(a, IntegerType)], a, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_funcdecl_return_atomic(self):
        input = """a:function boolean(){}a:function string(){}a:function float(){}a:function integer(){}"""
        expect = """Program([\n\tFuncDecl(a, BooleanType, [], None, BlockStmt([]))\n\tFuncDecl(a, StringType, [], None, BlockStmt([]))\n\tFuncDecl(a, FloatType, [], None, BlockStmt([]))\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_funcdecl_return_void(self):
        input = """a:function void(){}"""
        expect = """Program([\n\tFuncDecl(a, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_funcdecl_return_auto(self):
        input = """a:function auto (){}"""
        expect = """Program([\n\tFuncDecl(a, AutoType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_funcdecl_return_array(self):
        input = """a:function array[1,2,3] of integer (){}arr:function array[1] of integer (a:array[1] of integer){}"""
        expect = """Program([\n\tFuncDecl(a, ArrayType([1, 2, 3], IntegerType), [], None, BlockStmt([]))\n\tFuncDecl(arr, ArrayType([1], IntegerType), [Param(a, ArrayType([1], IntegerType))], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_funcdecl_body_non_empty(self):
        input = """a:function auto (){a=1;a=1;}"""
        expect = """Program([\n\tFuncDecl(a, AutoType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 326))


    # Expressions

    def test_expr_string(self):
        input = """a:integer = "a"::"b";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(::, StringLit(a), StringLit(b)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_expr_string_nested(self):
        input = """a:integer = "a"::"b"::"c"::"d"; b:integer = "a"::"b"::"c";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(::, BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d)))\n\tVarDecl(b, IntegerType, BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_expr_string_different_types(self):
        input = """a:integer = a::a[1]::a==1::-1::1::2.3::"a"::true::{}::a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, Id(a), ArrayCell(a, [IntegerLit(1)])), BinExpr(==, Id(a), IntegerLit(1))), UnExpr(-, IntegerLit(1))), IntegerLit(1)), FloatLit(2.3)), StringLit(a)), BooleanLit(True)), ArrayLit([])), FuncCall(a, [IntegerLit(1)])))\n])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_expr_relational(self):
        input = """a:integer = 1>2;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(>, IntegerLit(1), IntegerLit(2)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_expr_relational_nested_3(self):
        input = """a:integer = "a"!="b"=="c";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(==, BinExpr(!=, StringLit(a), StringLit(b)), StringLit(c)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_expr_relational_nested_4(self):
        input = """a:integer = "a"!="b"=="c"<"d";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(<, BinExpr(==, BinExpr(!=, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_expr_relational_different_types(self):
        input = """a:integer = a==a[1]!=a||1>-1<1>=2.3<="a"==true!={}>a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(>, BinExpr(!=, BinExpr(==, BinExpr(<=, BinExpr(>=, BinExpr(<, BinExpr(>, BinExpr(!=, BinExpr(==, Id(a), ArrayCell(a, [IntegerLit(1)])), BinExpr(||, Id(a), IntegerLit(1))), UnExpr(-, IntegerLit(1))), IntegerLit(1)), FloatLit(2.3)), StringLit(a)), BooleanLit(True)), ArrayLit([])), FuncCall(a, [IntegerLit(1)])))\n])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_expr_logic_and_or(self):
        input = """a,b:integer = 1||2,1&&2;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(||, IntegerLit(1), IntegerLit(2)))\n\tVarDecl(b, IntegerType, BinExpr(&&, IntegerLit(1), IntegerLit(2)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_expr_logic_and_or_nested_3(self):
        input = """a:integer = "a"&&"b"||"c";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(||, BinExpr(&&, StringLit(a), StringLit(b)), StringLit(c)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_expr_logic_and_or_nested_4(self):
        input = """a:integer = "a"||"b"||"c"&&"d";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(&&, BinExpr(||, BinExpr(||, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_expr_logic_and_or_different_types(self):
        input = """a:integer = a&&a[1]||a+1&&-1||1&&2.3||"a"&&true||{}&&a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(a), ArrayCell(a, [IntegerLit(1)])), BinExpr(+, Id(a), IntegerLit(1))), UnExpr(-, IntegerLit(1))), IntegerLit(1)), FloatLit(2.3)), StringLit(a)), BooleanLit(True)), ArrayLit([])), FuncCall(a, [IntegerLit(1)])))\n])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_expr_add_minus(self):
        input = """a,b:integer = 1+2,1-2;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(2)))\n\tVarDecl(b, IntegerType, BinExpr(-, IntegerLit(1), IntegerLit(2)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_expr_add_minus_nested_3(self):
        input = """a:integer = "a"+"b"-"c";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(-, BinExpr(+, StringLit(a), StringLit(b)), StringLit(c)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_expr_add_minus_nested_4(self):
        input = """a:integer = "a"-"b"+"c"-"d";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(-, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_expr_add_minus_different_types(self):
        input = """a:integer = a-a[1]+a*1--1+1-2.3+"a"-true+{}-a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(-, Id(a), ArrayCell(a, [IntegerLit(1)])), BinExpr(*, Id(a), IntegerLit(1))), UnExpr(-, IntegerLit(1))), IntegerLit(1)), FloatLit(2.3)), StringLit(a)), BooleanLit(True)), ArrayLit([])), FuncCall(a, [IntegerLit(1)])))\n])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_expr_multiplying(self):
        input = """a,b,c:integer = 1*2,1/2,1%2;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))\n\tVarDecl(b, IntegerType, BinExpr(/, IntegerLit(1), IntegerLit(2)))\n\tVarDecl(c, IntegerType, BinExpr(%, IntegerLit(1), IntegerLit(2)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_expr_multiplying_nested_3(self):
        input = """a:integer = "a"*"b"/"c";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(/, BinExpr(*, StringLit(a), StringLit(b)), StringLit(c)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_expr_multiplying_nested_4(self):
        input = """a:integer = "a"*"b"/"c"%"d";"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(%, BinExpr(/, BinExpr(*, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_expr_multiplying_different_types(self):
        input = """a:integer = a*a[1]/a::1%-1*1/2.3%"a"*true/{}%a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(::, BinExpr(/, BinExpr(*, Id(a), ArrayCell(a, [IntegerLit(1)])), Id(a)), BinExpr(%, BinExpr(/, BinExpr(*, BinExpr(%, BinExpr(/, BinExpr(*, BinExpr(%, IntegerLit(1), UnExpr(-, IntegerLit(1))), IntegerLit(1)), FloatLit(2.3)), StringLit(a)), BooleanLit(True)), ArrayLit([])), FuncCall(a, [IntegerLit(1)]))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_expr_negate(self):
        input = """a,a,a,a,a,a,a,a,a,a:integer = !a,!a[1],!(a::1),!-1,!1,!2.3,!"a",!true,!{},!a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, UnExpr(!, Id(a)))\n\tVarDecl(a, IntegerType, UnExpr(!, ArrayCell(a, [IntegerLit(1)])))\n\tVarDecl(a, IntegerType, UnExpr(!, BinExpr(::, Id(a), IntegerLit(1))))\n\tVarDecl(a, IntegerType, UnExpr(!, UnExpr(-, IntegerLit(1))))\n\tVarDecl(a, IntegerType, UnExpr(!, IntegerLit(1)))\n\tVarDecl(a, IntegerType, UnExpr(!, FloatLit(2.3)))\n\tVarDecl(a, IntegerType, UnExpr(!, StringLit(a)))\n\tVarDecl(a, IntegerType, UnExpr(!, BooleanLit(True)))\n\tVarDecl(a, IntegerType, UnExpr(!, ArrayLit([])))\n\tVarDecl(a, IntegerType, UnExpr(!, FuncCall(a, [IntegerLit(1)])))\n])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_expr_negate_nested(self):
        input = """a:integer = !!!!!a;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, Id(a)))))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_expr_sign(self):
        input = """a,a,a,a,a,a,a,a,a,a:integer = -a,-a[1],-(a::1),--1,-1,-2.3,-"a",-true,-{},-a(1);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, UnExpr(-, Id(a)))\n\tVarDecl(a, IntegerType, UnExpr(-, ArrayCell(a, [IntegerLit(1)])))\n\tVarDecl(a, IntegerType, UnExpr(-, BinExpr(::, Id(a), IntegerLit(1))))\n\tVarDecl(a, IntegerType, UnExpr(-, UnExpr(-, IntegerLit(1))))\n\tVarDecl(a, IntegerType, UnExpr(-, IntegerLit(1)))\n\tVarDecl(a, IntegerType, UnExpr(-, FloatLit(2.3)))\n\tVarDecl(a, IntegerType, UnExpr(-, StringLit(a)))\n\tVarDecl(a, IntegerType, UnExpr(-, BooleanLit(True)))\n\tVarDecl(a, IntegerType, UnExpr(-, ArrayLit([])))\n\tVarDecl(a, IntegerType, UnExpr(-, FuncCall(a, [IntegerLit(1)])))\n])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_expr_sign_nested(self):
        input = """a:integer = -----a;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, Id(a)))))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 349))

#     def test_simple_program(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """Program([\n
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([\n
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))

