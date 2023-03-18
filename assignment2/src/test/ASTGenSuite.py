import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # Program test

    def test_program_vardecl(self):
        input = """x:integer;"""
        expect = """Program([\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_program_funcdecl(self):
        input = """main:function void (){}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_program_vardecl_funcdecl(self):
        input = """x:integer;main:function void (){}"""
        expect = """Program([\n\tVarDecl(x, IntegerType)\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_program_funcdecl_vardecl(self):
        input = """main:function void (){}x:integer;"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_program_multi_vardecl(self):
        input = """x:integer;x:integer;x:integer;x:integer;"""
        expect = """Program([\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_program_multi_funcdecl(self):
        input = """main:function void (){}main:function void (){}main:function void (){}main:function void (){}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_program_multi_funcdecl_vardecl(self):
        input = """main:function void (){}x:integer;x:integer;x:integer;main:function void (){}main:function void (){}x:integer;"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tVarDecl(x, IntegerType)\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tVarDecl(x, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 306))


    # Vardecl test

    def test_vardecl_atomic(self):
        input = """a:integer;b:float;c:string;d:boolean;"""
        expect = """Program([\n\tVarDecl(a, IntegerType)\n\tVarDecl(b, FloatType)\n\tVarDecl(c, StringType)\n\tVarDecl(d, BooleanType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_vardecl_auto(self):
        input = """a,b,c:integer;b,b,b,b:auto;c,abc,a123,_abs:string;d:auto;"""
        expect = """Program([\n\tVarDecl(a, IntegerType)\n\tVarDecl(b, IntegerType)\n\tVarDecl(c, IntegerType)\n\tVarDecl(b, AutoType)\n\tVarDecl(b, AutoType)\n\tVarDecl(b, AutoType)\n\tVarDecl(b, AutoType)\n\tVarDecl(c, StringType)\n\tVarDecl(abc, StringType)\n\tVarDecl(a123, StringType)\n\tVarDecl(_abs, StringType)\n\tVarDecl(d, AutoType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_vardecl_arraytype(self):
        input = """a,b,c:array[1]of integer;b,b,b:array[1,2]of float;c123:array[1,2,3]of string;d:array[4,1,3,4] of boolean;"""
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

    def test_expr_idx_op(self):
        input = """a:integer = a[1];"""
        expect = """Program([\n\tVarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_expr_idx_op_list(self):
        input = """a:integer = a[1,2.3,a,"a",true,a+1,-1,{a,1},a(1)];"""
        expect = """Program([\n\tVarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1), FloatLit(2.3), Id(a), StringLit(a), BooleanLit(True), BinExpr(+, Id(a), IntegerLit(1)), UnExpr(-, IntegerLit(1)), ArrayLit([Id(a), IntegerLit(1)]), FuncCall(a, [IntegerLit(1)])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_expr_idx_op_nested(self):
        input = """a:integer = a[a[a],a[a[a,a[a]]]];"""
        expect = """Program([\n\tVarDecl(a, IntegerType, ArrayCell(a, [ArrayCell(a, [Id(a)]), ArrayCell(a, [ArrayCell(a, [Id(a), ArrayCell(a, [Id(a)])])])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_expr_operand_const(self):
        input = """a:integer = 1; b: float = 2.3; c:string = "abc"; d:boolean = true;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, IntegerLit(1))\n\tVarDecl(b, FloatType, FloatLit(2.3))\n\tVarDecl(c, StringType, StringLit(abc))\n\tVarDecl(d, BooleanType, BooleanLit(True))\n])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_expr_operand_var(self):
        input = """a:integer = a;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, Id(a))\n])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_expr_operand_funccall(self):
        input = """a:integer = a(1);b:string = a(a,b,c,d,e,f,g,h,i,j,k);"""
        expect = """Program([\n\tVarDecl(a, IntegerType, FuncCall(a, [IntegerLit(1)]))\n\tVarDecl(b, StringType, FuncCall(a, [Id(a), Id(b), Id(c), Id(d), Id(e), Id(f), Id(g), Id(h), Id(i), Id(j), Id(k)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_expr_operand_funccall_nested(self):
        input = """c:float = a(a(a),a(a(a)),a(1));"""
        expect = """Program([\n\tVarDecl(c, FloatType, FuncCall(a, [FuncCall(a, [Id(a)]), FuncCall(a, [FuncCall(a, [Id(a)])]), FuncCall(a, [IntegerLit(1)])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_expr_operand_funccall_empmty(self):
        input = """c:float = a();"""
        expect = """Program([\n\tVarDecl(c, FloatType, FuncCall(a, []))\n])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_expr_operand_arraylit(self):
        input = """c:float = {a,b,c};"""
        expect = """Program([\n\tVarDecl(c, FloatType, ArrayLit([Id(a), Id(b), Id(c)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_expr_operand_arraylit_empty(self):
        input = """c:float = {};"""
        expect = """Program([\n\tVarDecl(c, FloatType, ArrayLit([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_expr_operand_arraylit_nested(self):
        input = """c:float = {a,{b,c,{d,{{{}}}}}};"""
        expect = """Program([\n\tVarDecl(c, FloatType, ArrayLit([Id(a), ArrayLit([Id(b), Id(c), ArrayLit([Id(d), ArrayLit([ArrayLit([ArrayLit([])])])])])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_expr_operand_bracket(self):
        input = """c:float = a*(a::b);"""
        expect = """Program([\n\tVarDecl(c, FloatType, BinExpr(*, Id(a), BinExpr(::, Id(a), Id(b))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_expr_operand_bracket_nested(self):
        input = """c:float = ((((a))))*(((((b)*((c))))));"""
        expect = """Program([\n\tVarDecl(c, FloatType, BinExpr(*, Id(a), BinExpr(*, Id(b), Id(c))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_expr_operand_bracket_multiple(self):
        input = """c:float = (-(!(((((a::b)==c)||d)+e)*f))); c:float = -!a::b==c||d+e*f;"""
        expect = """Program([\n\tVarDecl(c, FloatType, UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))))\n\tVarDecl(c, FloatType, BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_expr_operand_complex_1(self):
        input = """c:float = -(((---!-!--!---11+a::!1/5*9==1/((((123%2)>=1)<2)/{1,2,3}/abc(123)==!a[a,{a,true,{a[1],b[2::"true"]}}])&&!!a---!1-!1)+123)/999);"""
        expect = """Program([\n\tVarDecl(c, FloatType, UnExpr(-, BinExpr(/, BinExpr(+, BinExpr(::, BinExpr(+, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(!, UnExpr(-, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(11))))))))))))), Id(a)), BinExpr(==, BinExpr(*, BinExpr(/, UnExpr(!, IntegerLit(1)), IntegerLit(5)), IntegerLit(9)), BinExpr(&&, BinExpr(/, IntegerLit(1), BinExpr(==, BinExpr(/, BinExpr(/, BinExpr(<, BinExpr(>=, BinExpr(%, IntegerLit(123), IntegerLit(2)), IntegerLit(1)), IntegerLit(2)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), FuncCall(abc, [IntegerLit(123)])), UnExpr(!, ArrayCell(a, [Id(a), ArrayLit([Id(a), BooleanLit(True), ArrayLit([ArrayCell(a, [IntegerLit(1)]), ArrayCell(b, [BinExpr(::, IntegerLit(2), StringLit(true))])])])])))), BinExpr(-, BinExpr(-, UnExpr(!, UnExpr(!, Id(a))), UnExpr(-, UnExpr(-, UnExpr(!, IntegerLit(1))))), UnExpr(!, IntegerLit(1)))))), IntegerLit(123)), IntegerLit(999))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_expr_operand_complex_2(self):
        input = """a:integer = !(3 + 5 * -2 / 4 == 1 || 2 >= 3) && "Hello"::"World" == "HelloWorld" && foo({1, 2, 3}, bar(4, 5, 6)) != true;"""
        expect = """Program([\n\tVarDecl(a, IntegerType, BinExpr(::, BinExpr(&&, UnExpr(!, BinExpr(>=, BinExpr(==, BinExpr(+, IntegerLit(3), BinExpr(/, BinExpr(*, IntegerLit(5), UnExpr(-, IntegerLit(2))), IntegerLit(4))), BinExpr(||, IntegerLit(1), IntegerLit(2))), IntegerLit(3))), StringLit(Hello)), BinExpr(!=, BinExpr(==, StringLit(World), BinExpr(&&, StringLit(HelloWorld), FuncCall(foo, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), FuncCall(bar, [IntegerLit(4), IntegerLit(5), IntegerLit(6)])]))), BooleanLit(True))))\n])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test_expr_operand_complex_3(self):
        input = """b:boolean = (((((((1+2*3)%4)/5.0+6*7)-8)/9.0)*10)/11)-12.0 == -13.0 && !("Hello"::"World" == "HelloWorld" || a(1, 2, 3) != {4, 5, 6}) || !(a > b && c <= d) && e(f, g, h[i + 1]) == true;"""
        expect = """Program([\n\tVarDecl(b, BooleanType, BinExpr(==, BinExpr(==, BinExpr(-, BinExpr(/, BinExpr(*, BinExpr(/, BinExpr(-, BinExpr(+, BinExpr(/, BinExpr(%, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3))), IntegerLit(4)), FloatLit(5.0)), BinExpr(*, IntegerLit(6), IntegerLit(7))), IntegerLit(8)), FloatLit(9.0)), IntegerLit(10)), IntegerLit(11)), FloatLit(12.0)), BinExpr(&&, BinExpr(||, BinExpr(&&, UnExpr(-, FloatLit(13.0)), UnExpr(!, BinExpr(::, StringLit(Hello), BinExpr(!=, BinExpr(==, StringLit(World), BinExpr(||, StringLit(HelloWorld), FuncCall(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))))), UnExpr(!, BinExpr(<=, BinExpr(>, Id(a), BinExpr(&&, Id(b), Id(c))), Id(d)))), FuncCall(e, [Id(f), Id(g), ArrayCell(h, [BinExpr(+, Id(i), IntegerLit(1))])]))), BooleanLit(True)))\n])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    
    # Test statements

    def test_stmt_assignstmt(self):
        input = """a:function integer(){a=1;a[1]=1;a[1]=a[1];a=a;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(1)])), AssignStmt(Id(a), Id(a))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_stmt_assignstmt_complex_expr(self):
        input = """a:function integer(){a=(-(!(((((a::b)==c)||d)+e)*f))); b[1]=-!a::b==c||d+e*f;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f))))), AssignStmt(ArrayCell(b, [IntegerLit(1)]), BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_stmt_if_stmt(self):
        input = """a:function integer(){if(a==1)a=1;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_stmt_if_else_stmt(self):
        input = """a:function integer(){if(a==1)a=1; else a=2;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_stmt_if_stmt_nested(self):
        input = """a:function integer(){if(a==1) if(a==2) if(a==3) a=4;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), AssignStmt(Id(a), IntegerLit(4)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_stmt_if_else_stmt_nested(self):
        input = """a:function integer(){if(a==1) a=1; else if(a==2) if(a==3) a=3; else a=4;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), IntegerLit(4)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_stmt_if_else_stmt_blockstmt(self):
        input = """a:function integer(){if(a==1) {} if(a==2) {} else {} if (a==3) {a=4;} else {a=5;}}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([])), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([]), BlockStmt([])), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([AssignStmt(Id(a), IntegerLit(4))]), BlockStmt([AssignStmt(Id(a), IntegerLit(5))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_stmt_for_stmt_scalar(self):
        input = """a:function integer(){for (i=1, i<10, i+1) print(a);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, Id(a)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_stmt_for_stmt_idxop(self):
        input = """a:function integer(){for (a[i]=1, a[i]<10, a[i]+1) print(a);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(1)), BinExpr(<, ArrayCell(a, [Id(i)]), IntegerLit(10)), BinExpr(+, ArrayCell(a, [Id(i)]), IntegerLit(1)), CallStmt(print, Id(a)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_stmt_for_stmt_complex_expr(self):
        input = """a:function integer(){for (i=a*(a::b), (-(!(((((a::b)==c)||d)+e)*f))), -!a::b==c||d+e*f) print(a);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(*, Id(a), BinExpr(::, Id(a), Id(b)))), UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))), BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))))), CallStmt(print, Id(a)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_stmt_while_stmt(self):
        input = """a:function integer(){while (a>1) a=1;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(>, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_stmt_while_nested(self):
        input = """a:function integer(){while (a>1) while (a<1) while (a==1) a=1;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(>, Id(a), IntegerLit(1)), WhileStmt(BinExpr(<, Id(a), IntegerLit(1)), WhileStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_stmt_while_complex_expr(self):
        input = """a:function integer(){while (-!a::b==c||d+e*f)  a=1;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))))), AssignStmt(Id(a), IntegerLit(1)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_stmt_do_while(self):
        input = """a:function integer(){do {a=1;} while (a==1);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    
    def test_stmt_do_while_empty_block(self):
        input = """a:function integer(){do {} while (a==1);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_stmt_do_while_nested(self):
        input = """a:function integer(){do {do {do {} while (a==0);}while(a<=2); } while (a==1);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(<=, Id(a), IntegerLit(2)), BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([]))]))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_stmt_do_while_complex_expr(self):
        input = """a:function integer(){do {} while (-!a::b==c||d+e*f);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))))), BlockStmt([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_stmt_break_inside_loop(self):
        input = """a:function integer(){do {break;} while (a==1);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([BreakStmt()]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_stmt_break_outside_loop(self):
        input = """a:function integer(){break;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([BreakStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_stmt_continue_inside_loop(self):
        input = """a:function integer(){do {continue;} while (a==1);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_stmt_continue_outside_loop(self):
        input = """a:function integer(){continue;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([ContinueStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_stmt_return(self):
        input = """a:function integer(){return abc;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([ReturnStmt(Id(abc))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_stmt_return_empty(self):
        input = """a:function integer(){return      ;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([ReturnStmt()]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_stmt_return_inside_stmt(self):
        input = """a:function integer(){if (a==1) return a;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(Id(a)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_stmt_return_complex_expr(self):
        input = """a:function integer(){if (a==1) return -!a::b==c||d+e*f;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f))))))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_stmt_callstmt(self):
        input = """a:function integer(){print(a);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([CallStmt(print, Id(a))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_stmt_callstmt_inside(self):
        input = """a:function integer(){if (a==1) print(a);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), CallStmt(print, Id(a)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_stmt_blockstmt_nested(self):
        input = """a:function integer(){ {{{}{{}{}{{{}}}}}} }"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([]), BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([BlockStmt([])])])])])])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_stmt_blockstmt_body_vardecl(self):
        input = """a:function integer(){ a:integer = 1;}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_stmt_blockstmt_body_vardecls_stmts(self):
        input = """a:function integer(){ a:integer = 1; if (a==1) a=1; b:float; b=2.3; do{a=a+b;}while(b>1); c = a+b; print(c);}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1))), VarDecl(b, FloatType), AssignStmt(Id(b), FloatLit(2.3)), DoWhileStmt(BinExpr(>, Id(b), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(b)))])), AssignStmt(Id(c), BinExpr(+, Id(a), Id(b))), CallStmt(print, Id(c))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_stmt_complex_test(self):
        input = """a:function integer(){ a=1; if (a==1) {} else {while (a>=0) a=a+1;} for (i=a, i<=i, i+1) {} i(a,b,c); do{a=1;print(a);}while(b||a); break; for(i=!a-b*c--d==2, i+10-2%3||4&&!5||-6/!!!7, i+a-true=="abc"/abc(123)+{abc,"abc",true,false}) a[2]=a[56, 2==1]; break; if(b==1) {continue; break;} return a+b+c;{}}"""
        expect = """Program([\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([]), BlockStmt([WhileStmt(BinExpr(>=, Id(a), IntegerLit(0)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))])), ForStmt(AssignStmt(Id(i), Id(a)), BinExpr(<=, Id(i), Id(i)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), CallStmt(i, Id(a), Id(b), Id(c)), DoWhileStmt(BinExpr(||, Id(b), Id(a)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), CallStmt(print, Id(a))])), BreakStmt(), ForStmt(AssignStmt(Id(i), BinExpr(==, BinExpr(-, BinExpr(-, UnExpr(!, Id(a)), BinExpr(*, Id(b), Id(c))), UnExpr(-, Id(d))), IntegerLit(2))), BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(-, BinExpr(+, Id(i), IntegerLit(10)), BinExpr(%, IntegerLit(2), IntegerLit(3))), IntegerLit(4)), UnExpr(!, IntegerLit(5))), BinExpr(/, UnExpr(-, IntegerLit(6)), UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(7)))))), BinExpr(==, BinExpr(-, BinExpr(+, Id(i), Id(a)), BooleanLit(True)), BinExpr(+, BinExpr(/, StringLit(abc), FuncCall(abc, [IntegerLit(123)])), ArrayLit([Id(abc), StringLit(abc), BooleanLit(True), BooleanLit(False)]))), AssignStmt(ArrayCell(a, [IntegerLit(2)]), ArrayCell(a, [IntegerLit(56), BinExpr(==, IntegerLit(2), IntegerLit(1))]))), BreakStmt(), IfStmt(BinExpr(==, Id(b), IntegerLit(1)), BlockStmt([ContinueStmt(), BreakStmt()])), ReturnStmt(BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))), BlockStmt([])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_complex_test_1(self):
        input = """a:auto = -!a::b==c||d+e*f; a:function void(a:integer, inherit out ouet:float, inherit oute: string) {}a:function integer(){ a=1; if (a==1) {} else {while (a>=0) a=a+1;} for (i=a, i<=i, i+1) {} i(a,b,c); do{a=1;print(a);}while(b||a); break; for(i=!a-b*c--d==2, i+10-2%3||4&&!5||-6/!!!7, i+a-true=="abc"/abc(123)+{abc,"abc",true,false}) a[2]=a[56, 2==1]; break; if(b==1) {continue; break;} return a+b+c;{}}"""
        expect = """Program([\n\tVarDecl(a, AutoType, BinExpr(::, UnExpr(-, UnExpr(!, Id(a))), BinExpr(==, Id(b), BinExpr(||, Id(c), BinExpr(+, Id(d), BinExpr(*, Id(e), Id(f)))))))\n\tFuncDecl(a, VoidType, [Param(a, IntegerType), InheritOutParam(ouet, FloatType), InheritParam(oute, StringType)], None, BlockStmt([]))\n\tFuncDecl(a, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([]), BlockStmt([WhileStmt(BinExpr(>=, Id(a), IntegerLit(0)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))])), ForStmt(AssignStmt(Id(i), Id(a)), BinExpr(<=, Id(i), Id(i)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), CallStmt(i, Id(a), Id(b), Id(c)), DoWhileStmt(BinExpr(||, Id(b), Id(a)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), CallStmt(print, Id(a))])), BreakStmt(), ForStmt(AssignStmt(Id(i), BinExpr(==, BinExpr(-, BinExpr(-, UnExpr(!, Id(a)), BinExpr(*, Id(b), Id(c))), UnExpr(-, Id(d))), IntegerLit(2))), BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(-, BinExpr(+, Id(i), IntegerLit(10)), BinExpr(%, IntegerLit(2), IntegerLit(3))), IntegerLit(4)), UnExpr(!, IntegerLit(5))), BinExpr(/, UnExpr(-, IntegerLit(6)), UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(7)))))), BinExpr(==, BinExpr(-, BinExpr(+, Id(i), Id(a)), BooleanLit(True)), BinExpr(+, BinExpr(/, StringLit(abc), FuncCall(abc, [IntegerLit(123)])), ArrayLit([Id(abc), StringLit(abc), BooleanLit(True), BooleanLit(False)]))), AssignStmt(ArrayCell(a, [IntegerLit(2)]), ArrayCell(a, [IntegerLit(56), BinExpr(==, IntegerLit(2), IntegerLit(1))]))), BreakStmt(), IfStmt(BinExpr(==, Id(b), IntegerLit(1)), BlockStmt([ContinueStmt(), BreakStmt()])), ReturnStmt(BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))), BlockStmt([])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_complex_test_2(self):
        input = """ /*A complex text*/\n//The 100 test\nmain:function void(a:integer, inherit out a:integer){ for (abc = (-(!(((((a::b)==c)||d)+e)*f))), (-(!(((((a::b)==c)||d)+e)*f))), (-(!(((((a::b)==c)||d)+e)*f)))) while ((-(!(((((a::b)==c)||d)+e)*f)))) if ((-(!(((((a::b)==c)||d)+e)*f)))) break; else abc((-(!(((((a::b)==c)||d)+e)*f)))); do {continue;} while (-(!(((((a::b)==c)||d)+e)*f))); abc(-(!(((((a::b)==c)||d)+e)*f)));} """
        expect = """Program([\n\tFuncDecl(main, VoidType, [Param(a, IntegerType), InheritOutParam(a, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(abc), UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f))))), UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))), UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))), WhileStmt(UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))), IfStmt(UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))), BreakStmt(), CallStmt(abc, UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))))))), DoWhileStmt(UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))), BlockStmt([ContinueStmt()])), CallStmt(abc, UnExpr(-, UnExpr(!, BinExpr(*, BinExpr(+, BinExpr(||, BinExpr(==, BinExpr(::, Id(a), Id(b)), Id(c)), Id(d)), Id(e)), Id(f)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 399))
