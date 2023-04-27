import unittest
from TestUtils import TestChecker
from AST import *

from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):

    # Program test
    def test_no_main_function(self):
        input = """
            a: integer;
            b: integer;
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_program_main_not_correct_form_not_void(self):
        input = """
            a: integer;
            b: integer;
            main: function integer (){ }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_program_main_not_correct_form_have_para(self):
        input = """
            a: integer;
            b: integer;
            main: function void (a:integer){ }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_program_redeclared_var(self):
        input = """
            main: function void (){ }
            a:function integer (){}
            a:float;
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_program_redeclared_function(self):
        input = """
            main: function void (){ }
            a: integer;
            a: function float (){}
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_program_redeclared_before_main(self):
        input = """
            a: integer;
            a: function float (){}
            main: function void (){ }        
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 405))


    # Test vardecl

    def test_vardecl_redeclared_inside(self):
        input = """
            main: function void (){ 
                a:integer;
                a:float;
            }        
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_vardecl_redeclared_outside_inside(self):
        input = """
            a:integer;
            main: function void (){ 
                a:float;
            }        
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_vardecl_redeclared_same_funcname(self):
        input = """
            a:integer;
            main: function void (){
            }        
            foo: function float(){
                foo: integer;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_vardecl_type_auto_no_init(self):
        input = """
            a:auto;
            main: function void (){}
        """
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_vardecl_type_auto_init(self):
        input = """
            a:auto = {  {   {1},{2}   }, {   {3},{4}  }   };
            main: function void (){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_vardecl_init_auto(self):
        input = """
            main: function void (){}
            foo: function void(a:auto){
                b:float = a;
                c:string = foo1();
            }
            foo1: function auto(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_vardecl_init_diffent_type_coerce(self):
        input = """
            main: function void (){}
            a:float = 1;
            b:integer = 2;
            c:float = b;
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_vardecl_init_diffent_type_dims(self):
        input = """
            main: function void (){}
            a:array[1,2] of integer = {{1},{2}};
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_vardecl_init_diffent_type_typ(self):
        input = """
            main: function void (){}
            a:array[1,2] of float = {{1,1}};
            b: array[1,2] of integer = a;
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, ArrayType([1, 2], IntegerType), Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_vardecl_init_same_type(self):
        input = """
            main: function void (){}
            a:integer = 1;
            b:float = 2.3;
            c:boolean = true;
            d:string = "abc";
            e:array[1,2,3] of integer = {{{1,2,3},{4,5,6}}};
            f:array[1,2,3] of float = e;
            h:string = i();
            i: function string (){}
            k:integer = k;  
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_vardecl_no_init(self):
        input = """
            main: function void (){}
            a:integer;
            a2 : integer = a;
            b:float;
            b2: float = a2;
            c:boolean;
            c2:boolean = c;
            d:string;
            d2:string = d;
            e:array[1,2,3] of integer ;
            f:array[1,2,3] of float = e;
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    # FuncDecl

    def test_function_inherit_empty_body(self):
        input = """
            main: function void(){}
            foo: function boolean(){}
            foo1: function integer () inherit foo{}
            foo2: function float (a:integer){}
            foo3: function string () inherit foo2{} 
        """
        expect = """Invalid statement in function: foo3"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_function_inherit_no_super_body_not_stmt(self):
        input = """
            main: function void(){}
            foo: function boolean(){}
            foo1: function integer () inherit foo{x:integer;}
            foo2: function float (a:integer){a=1;}
            foo3: function string () inherit foo2{z:integer;} 
        """
        expect = """Invalid statement in function: foo3"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_function_inherit_parent_not_exist(self):
        input = """
            main: function void(){}
            foo: function boolean(){}
            foo1: function integer () inherit foo5{x:integer;}
        """
        expect = """Undeclared Function: foo5"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_function_inherit_parent_not_func(self):
        input = """
            main: function void(){}
            foo: function boolean(){}
            foo5 : integer = 1;
            foo1: function integer () inherit foo5{}
        """
        expect = """Undeclared Function: foo5"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_function_inherit_parent_inherit_not_exist(self):
        input = """
            main: function void(){}
            foo: function boolean(){}
            foo5 : function string()inherit foo100{}
            foo1: function integer () inherit foo5{}
            foo100: function auto () inherit foo999{}
        """
        expect = """Undeclared Function: foo999"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_function_inherit_parent_inherit_para_error(self):
        input = """
            main: function void(){}
            foo: function boolean(){}
            foo1: function integer () inherit foo5{}
            foo5 : function string()inherit foo100{super(1,2);}
            foo100: function auto (a:integer, inherit a:float){}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_function_inherit_parent_multiple_inherit(self):
        input = """
            main: function void(){}
            foo2: function void() inherit main{}
            foo1: function boolean() inherit foo9{}
            foo6: function integer () inherit foo5{}
            foo3 : function string () inherit foo2{}
            foo9: function auto () inherit foo6{}
            foo5: function string () inherit foo3 {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_function_inherit_one_prevent(self):
        input = """
            main: function void(){}
            foo2: function void() inherit main{}
            foo1: function boolean() inherit foo9{}
            foo6: function integer () inherit foo5{preventDefault();}
            foo3 : function string () inherit foo2{}
            foo9: function auto () inherit foo6{}
            foo5: function string () inherit foo3 {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_function_inherit_same_paraname_not_inherit(self):
        input = """
            main: function void(){}
            foo1: function boolean(a:integer) inherit foo9{super(1);}
            foo6: function integer (a:integer) {}
            foo9: function auto (a:integer) inherit foo6{super(1);}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_function_inherit_same_paraname_inherited_near(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer) inherit foo6{super(1);}
            foo6: function integer (inherit a:integer) {}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_function_inherit_same_paraname_inherited_far(self):
        input = """
            main: function void(){}
            foo9: function string (inherit a:integer) inherit main{}
            foo1: function boolean(a:integer) inherit foo4{}
            foo4: function float() inherit foo7{}
            foo7: function auto () inherit foo6{}
            foo6: function integer () inherit foo9{super(1);}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_function_no_super_recall_super_preventDefault(self):
        input = """
            main: function void(){}
            foo1: function integer(){}
            foo9: function string (inherit a:integer) inherit foo1{
                x :float = super();
                super();
                preventDefault();
                super();
                y: integer;
                y = super();
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_function_no_super_recall_super_incorrect(self):
        input = """
            main: function void(){}
            foo9: function string (inherit a:integer) inherit main{
                x :integer;
                super();
                preventDefault();
                super(1);
            }
        """
        expect = """Type mismatch in statement: CallStmt(super, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_function_no_super_recall_preventDefault_incorrect(self):
        input = """
            main: function void(){}
            foo9: function string (inherit a:integer) inherit main{
                x :integer;
                super();
                preventDefault(1);
            }
        """
        expect = """Type mismatch in statement: CallStmt(preventDefault, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_function_no_super_recall_super_use_as_expr_incorrect(self):
        input = """
            main: function void(){}
            foo9: function string (inherit a:integer) inherit main{
                x :integer;
                super();
                preventDefault();
                x = super();
            }
        """
        expect = """Type mismatch in expression: FuncCall(super, [])"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_function_no_super_recall_preventDefault_use_as_expr_incorrect(self):
        input = """
            main: function void(){}
            foo9: function string (inherit a:integer) inherit main{
                x :integer;
                super();
                x=preventDefault();
            }
        """
        expect = """Type mismatch in expression: FuncCall(preventDefault, [])"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_function_super_compare_para_arg_missing(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float, g:integer){}
            foo9: function string () inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
        """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_function_super_compare_para_arg_redundance(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string () inherit foo1{
                super(1152,2.3,true,"abc",false,{{1},{2}},1,2,3,4,5);
                e = false;
            }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_function_super_compare_para_arg_para_auto(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:auto, inherit b: auto, c: auto, d:auto, e:auto){}
            foo9: function string () inherit foo1{
                super(1152,2.3,true,"abc",{{1,2}});
                a = "abc";
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_function_super_compare_para_arg_arg_auto(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:auto, inherit b: auto, c: integer, d:float, e:string){}
            foo9: function string (c:auto, d:auto, e:auto) inherit foo1{
                super(1152,2.3,c,d,e);
                c = 1;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_function_super_compare_para_arg_types_correct(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float() inherit foo9{
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_function_super_compare_para_arg_types_incorrect(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string () inherit foo1{
                super(1152.3,2,true,"abc",false,{{1,2}});
                e = false;
            }
        """
        expect = """Type mismatch in expression: FloatLit(1152.3)"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_function_super_compare_para_arg_types_arraytype_not_match(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string () inherit foo1{
                super(1152,2,true,"abc",false,{{"a"},{"b"}});
                e = false;
            }
        """
        expect = """Type mismatch in expression: ArrayLit([ArrayLit([StringLit(a)]), ArrayLit([StringLit(b)])])"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_function_super_inherit_para_cannot_use_yet_near(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{a},{2}});
                e = false;
            }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_function_super_inherit_para_cannot_use_yet_far(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float() inherit foo9{
                super({1},{a,b},{{"a","b","c"},{"1","2","3"}});
            }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_function_super_recall_super_preventDefault(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float() inherit foo9{
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
                preventDefault();
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
                preventDefault();
                super({4},{7,8},{{"a1","b2","c3"},{"1a","2b","3c"}});
                preventDefault();
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_function_super_recall_super_incorrect(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float() inherit foo9{
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
                preventDefault();
                super({1},{2,3});
                preventDefault();
            }
        """
        expect = """Type mismatch in statement: CallStmt(super, ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_function_super_recall_preventDefault_incorrect(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float() inherit foo9{
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
                preventDefault();
                preventDefault(1);
            }
        """
        expect = """Type mismatch in statement: CallStmt(preventDefault, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_function_super_recall_super_use_as_expr_incorrect(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float(z:float) inherit foo9{
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
                preventDefault();
                z = super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(z), FuncCall(super, [ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(3)]), ArrayLit([ArrayLit([StringLit(a), StringLit(b), StringLit(c)]), ArrayLit([StringLit(1), StringLit(2), StringLit(3)])])]))"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_function_super_recall_preventDefault_use_as_expr_incorrect(self):
        input = """
            main: function void(){}
            foo1: function boolean(inherit a:integer, inherit b: float, c: boolean, d:string, inherit e: auto, f:array[1,2] of float){}
            foo9: function string (g:array[1] of integer, h:array[2]of float, i:array[2,3]of string) inherit foo1{
                super(1152,2.3,true,"abc",false,{{1,2}});
                e = false;
            }
            foo10: function float(z:float) inherit foo9{
                super({1},{2,3},{{"a","b","c"},{"1","2","3"}});
                z=preventDefault();
            }
        """
        expect = """Type mismatch in expression: FuncCall(preventDefault, [])"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_function_preventDefault_inherit_error(self):
        input = """
            main: function void(){}
            foo: function void() inherit fadslkfjasd{preventDefault();}
            foo1: function void(inherit c:integer, b:auto) inherit foo2{preventDefault();}
            foo2: function void(a:integer, a:float){}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_function_preventDefault_inherit(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo1: function void(inherit a:integer, b:auto) inherit foo{preventDefault();}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_function_preventDefault_then_inherit_para(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo1: function void(inherit a:integer, b:auto) inherit foo{preventDefault();}
            foo2: function void() inherit foo1{super(1,2);}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_function_preventDefault_then_inherit_name(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit asdfadsf{preventDefault();}
            foo1: function void() inherit foo{preventDefault();}
            foo2: function void() inherit foo1{}
        """
        expect = """Undeclared Function: asdfadsf"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_function_preventDefault_call_super(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit asdfadsf{preventDefault();}
            foo1: function void() inherit foo{preventDefault(); super(1,2.3);}
            foo2: function void() inherit foo1{}
        """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_function_preventDefault_recall_preventDefault(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo1: function void() inherit foo{preventDefault(); preventDefault();preventDefault();}
            foo2: function void() inherit foo1{}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_function_preventDefault_recall_preventDefault_error(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo1: function void() inherit foo{preventDefault(); preventDefault(1);preventDefault();}
            foo2: function void() inherit foo1{}
        """
        expect = """Type mismatch in statement: CallStmt(preventDefault, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_function_no_inherit_call_super(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo2: function void(){super(1,2.3);}
        """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_function_no_inherit_call_preventDefault(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo2: function void(){preventDefault();}
        """
        expect = """Undeclared Function: preventDefault"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_function_redeclared_para_before_invalid(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo2: function void(a:integer, a:integer) inherit foo{super(1,2.3);}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_function_prevented_invalid_in_ancestor(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo1: function void(b:float) inherit foo{preventDefault(); preventDefault();preventDefault();}
            foo2: function void(c:integer) inherit foo1{super(2.3);}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_function_invalid_in_ancestor_before_redeclared(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float) inherit main{preventDefault();}
            foo1: function void(inherit b:float) inherit foo{preventDefault(); preventDefault();preventDefault();}
            foo2: function void(c:integer, c:integer) inherit foo1{super(2.3);}
        """
        expect = """Redeclared Parameter: c"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_inherit_invalid_before_invalid_stmt(self):
        input = """
            main: function void(){}
            M: function void(a:integer) inherit N {}
            N: function void (inherit a: integer) {}

        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_function_body_use_params(self):
        input = """
            main: function void(){}
            foo: function void(inherit a:integer, inherit b:float){}
            foo1: function void(inherit c:float) inherit foo{super(1,2.3);}
            foo2: function void(d:integer, e:integer) inherit foo1{
                super(4.5);
                a = 1; b = 2.3; c = 5.6; d = 7; e = 8;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_return_multiple_same_type(self):
        input = """
            main: function void(){
                return;
                return;
                return;
                return;
            }
            foo: function string(){
                return "a";
                return "b";
                return "c";
                return "d";
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_return_multiple_different_type(self):
        input = """
            main: function void(){
                return;
                return 1;
                return true;
                return "abc";
            }
            foo: function string(){
                return;
                return "1";
                return 1;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_return_multiple_expression_error(self):
        input = """
            main: function void(){
                return;
                return abc();
                return 1::3;
                return x+y-z/3;
            }
            foo: function string(){
                return "abc";
                return;
                return 1::8&&3/{1,2,3};
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_return_for_void(self):
        input = """
            main: function void(){return 1;}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_return_and_after_that(self):
        input = """
            main: function void(){
                return;
                return abc();
                x :integer;
                x = true;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_return_auto(self):
        input = """
            main: function void(){
                return;
            }
            foo: function integer (x:auto){
                return x;
                x = 1;
                x = "abc";
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_return_auto_function(self):
        input = """
            main: function void(){
                return;
            }
            foox: function auto(){}
            foo: function float (x:integer, y:float){
                return foox();
                x = foox();
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), FuncCall(foox, []))"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_return_auto_changed(self):
        input = """
            main: function void(){
                return;
            }
            foo: function auto (x:integer, y:float){
                y = foo(1,2);
                return foo(1,2);
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_return_coerce(self):
        input = """
            main: function void(){
                return;
            }
            foo2: function array[1,2,3] of float (x:array[3]of integer,y:array[3]of integer){
               return {{x,y}};
               z:array[1,2,3] of integer = {{y,x}};
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_vardecl_same(self):
        input = """
            main: function void(){
                return;
            }
            foo1: function void(foo1:integer) { }
            foo2: function array[1,2,3] of float() inherit foo1{
                super(1);
               foo1: integer;
               foo2: float;
            }
            foo3: function integer(foo1:integer, foo3:float) inherit foo1{
                super(1);
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 470))    

    def test_outside_function(self):
        input = """
            main: function void(){
                return;
            }
            foo1: function void(foo1:integer) { }
            foo2: function array[1,2,3] of float() inherit foo1{
                super(1);
               foo1: integer;
               foo2: float;
            }
            x : float = foo2();
            foo3: function integer(foo1:integer, foo3:float) inherit foo1{
                super(1);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, FloatType, FuncCall(foo2, []))"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    # Test expressions

    def test_id_different_type(self):
        input = """
            main: function void(){
                return;
            }
            foo1: function void(){}
            foo2: function void(){
                a : integer = foo1;
            }
        """
        expect = """Type mismatch in expression: Id(foo1)"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_array_cell_redundan_length(self):
        input = """
            main: function void(){
                return;
            }
            a:array[1,2,3] of integer;
            x:integer = a[99,99,99,99];
        """
        expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(99), IntegerLit(99), IntegerLit(99), IntegerLit(99)])"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_array_cell_missing_length(self):
        input = """
            main: function void(){
                return;
            }
            foo: function void(h:auto){
            a:array[1,2,3] of integer;
            x:array[3]of float = a[99,99];
            y:array[2,3] of integer = a[-1];
            z:integer = a[0,0,0];
            a1 : auto = a[0,0];
            a2 : auto = a[0];
            a3: auto = a[0,0,0];
            a3 = z;
            b:integer = a[h,0,0];
            h = "abc";
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(h), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_binop_infer(self):
        input = """
            main: function void(){
                return;
            }
            foo: function void(){
                a: integer = 1;
                b: float = 2.3;
                c:auto = a+a;
                d:auto = b/b;
                e:auto = a-b;
                f:auto = b*a;
                //c = d;
            }
            foo1: function void(){
                x: string = "abc";
                y: auto = x::"123";
            }
            foo2: function void(){
                a : boolean = true;
                b : boolean = false;
                c: auto = a||b;
                d: auto = c&&a&&b;
            }
            foo5: function void(a:auto, b:auto, c:auto, d:auto, e:auto, f:auto){
                x:integer;
                y:float;
                a = x < x;
                c = b <= x;
                d = y > x;
                f = y >= e;
                g: integer = b;
                h: float = e;
                //d = f;
                //a = c;
            }
            foo3: function void(inherit a:auto, inherit z:auto){
                b: integer;
                c: boolean;
                d: auto = a == b;
                y: auto = z != b;
                d = y;
            }
            foo6: function void(b:auto, c:auto){
                a:integer;
                b = a%c;
            }
            foo4: function void() inherit foo3{
                super(true, false);
            }
            
        """
        expect = """Type mismatch in expression: BooleanLit(True)"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_unnop_infer(self):
        input = """
            main: function void(){
                return;
            }
            foo:function void(a:auto, b:auto){
                b = !b;
                a = -1;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_arraylit_illegal(self):
        input = """
            main: function void(){
                return;
            }
            foo:function void(){
                a : auto = {{1,1},{2,3}};
                b : auto = {{{{{1}}}}};
                c : auto = {{{{"123","456"},{"abc","def"}},{{"123","456"},{"abc","def"}}},{{{"123","456"},{"abc","def"}},{{"123","456"},{"abc","def"}}}};
                d : auto = {{1,2},{4,5.6}};
            }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(4), FloatLit(5.6)])])"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_funccall_special_name(self):
        input = """
            main: function void(){
                return;
            }
            foo:function void(){
                a:integer = readInteger();
                b:boolean = readBoolean();
                c:float = readFloat();
                d:string = readString();
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    # Test Statements

    def test_assignStmt_array(self):
        input = """
            main: function void(){
                
            }
            a: array[1,2,3] of integer;
            foo: function void(){
                a[99,99,99] = 1;
                a[11,2] = {1,2,3};
            }
        """
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(11), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_blockStmt_outside_scope(self):
        input = """
            main: function void(){
                
            }
            a: array[1,2,3] of integer;
            foo: function integer(){
                {
                    {}
                    {}{}{{}{{}{{}}}}
                    return 2;
                    {
                        return 1;
                        x:integer = 1;
                    }
                    return x;
                }
            }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_ifStmt(self):
        input = """
            main: function void(){
                return;
            }
            a: array[1,2,3] of integer;
            
            foo: function integer(h:auto){
                
                if (h == "1"){ 
                    h = false;}
                
                b : boolean = foo1();
            }
        """
        expect = """Type mismatch in expression: BinExpr(==, Id(h), StringLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_forStmt(self):
        input = """
            main: function void(){
                return;
            }
            a: array[1,2,3] of integer;
            
            foo: function integer(h:auto){
                for (h=1, h<10, h=h+1)
                {
                    return 1;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_whileStmt(self):
        input = """
            main: function void(){
                return;
            }
            a: array[1,2,3] of integer;
            x:integer = 1;
            while (x<10)
            {
                b: float;
                return b;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_doWhile(self):
        input = """
            main: function void(){
                return;
            }
            a: array[1,2,3] of integer;
            x:integer = 1;
            
            do
            {
                b: float;
                return b;
            }
            while (x<10);
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_break(self):
        input = """
            main: function void(){
                return;
            }
            a: array[1,2,3] of integer;
            x:integer = 1;
            
            break;
        """
        expect = """Must in loop: break"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_continue(self):
        input = """
            main: function void(){
                return;
            }
            a: array[1,2,3] of integer;
            x:integer = 1;
            
            continue;
        """
        expect = """Must in loop: continue"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_complex1(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x == "1") x = 1;            
        }
        foo: function float(){}"""
        expect = "Type mismatch in expression: BinExpr(==, Id(x), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_complex2(self):
        input = """
        foo: function void (inherit a: auto, inherit out b: auto) inherit bar {}
        bar: function void(){}
        main: function void () inherit foo {
            super(1, 1.2);
            printInteger(4);
            foo(true,false);
            if (a == b){
                printBoolean(a);
            }
        }"""
        expect = "Type mismatch in statement: CallStmt(foo, BooleanLit(True), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_complex3(self):
        input = """
            main: function void(){}
            e: function integer() inherit d{preventDefault();}
            d: function integer (dvar: integer) inherit c{super(1); avar = bvar;}
            c: function integer (inherit cvar: integer) inherit b{super(1);}
            b: function integer(inherit bvar: integer) inherit a{super(1);}
            a: function integer(inherit avar: integer){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_complex4(self):
        input = """
            main: function void(){}
            c: function integer () inherit notExist {
                preventDefault();
                super(1,2,3);
            }
        """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    
    
    def test_complex5(self):
        input = """
            main: function void(){}
            a: function integer(){
                return 1;
                return "abc"; // Don't check with int
                return zzz(); // A not exist => Error?
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 492))


    def test_complex6(self):
        input = """
            main: function void(){}
            a: function integer (inherit a: integer) inherit a {super(1);}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_complex7(self):
        input = """
            main: function void(){}
            c: function integer (a:auto){
                a = a<1.2;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_complex8(self):
        input = """
            main: function void(){}
            e: function integer() inherit d{preventDefault();}
            d: function integer (dvar: integer) inherit c{super(1); avar = bvar;}
            c: function integer (inherit cvar: integer) inherit b{super(1);}
            b: function integer(inherit bvar: integer) inherit a{super(1);}
            a: function integer(inherit avar: integer){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_complex9(self):
        input = """
            main: function void(){}
            c: function integer () inherit notExist {
                preventDefault();
                super(1,2,3);
            }
        """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    
    
    def test_complex10(self):
        input = """
            main: function void(){}
            a: function integer(){
                return 1;
                return "abc"; // Don't check with int
                return zzz(); // A not exist => Error?
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 497))


    def test_complex11(self):
        input = """
            main: function void(){}
            a: function integer (inherit a: integer) inherit a {super(1);}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_complex12(self):
        input = """
            main: function void(){}
            c: function integer (a:auto){
                a = a<1.2;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 499))