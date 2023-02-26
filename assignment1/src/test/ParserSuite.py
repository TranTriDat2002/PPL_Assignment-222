import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):


    """Test program structure"""
    def test_empty_program(self):
        input = """/*abc*/\n//"""
        expect = "Error on line 2 col 2: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_program_vardecl(self):
        input = """a:integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_program_funcdecl(self):
        input = """main: function void(){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_program_funcdecl_vardecl(self):
        input = """a:integer;\nmain: function void(){}\na:integer;\nmain: function void(){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_program_begin_with_statement(self):
        input = """a = 1;"""
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 204))
    

    """Test variable declaration"""
    def test_vardecl_shortform_single_ID(self):
        input = """a:boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_vardecl_shortform_ID_list(self):
        input = """a,b,c,ab,abc:boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_vardecl_shortform_ID_type(self):
        input = """a:boolean; b:integer; c:float; d: string; e: auto;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_vardecl_shortform_array_type_valid_element_type(self):
        input = """a:array[1] of integer; b:array[1,2] of float; c:array[1,2,3] of boolean; d:array[1,2,3,4]of string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_vardecl_shortform_array_type_invalid_element_type_array(self):
        input = """a:array[1] of array[1,2] of float;"""
        expect = "Error on line 1 col 14: array"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_vardecl_shortform_array_type_invalid_element_type_random(self):
        input = """a:array[1] of abc;"""
        expect = "Error on line 1 col 14: abc"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_vardecl_shortform_array_type_missing_dimension(self):
        input = """a:array[] of integer;"""
        expect = "Error on line 1 col 8: ]"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_vardecl_shortform_array_type_missing_elementtype(self):
        input = """a:array[1];"""
        expect = "Error on line 1 col 10: ;"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_vardecl_shortform_array_type_only(self):
        input = """array[1] of integer;"""
        expect = "Error on line 1 col 0: array"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_vardecl_shortform_array_type_invalid_dimension(self):
        input = """a:array[1+1] of integer;"""
        expect = "Error on line 1 col 9: +"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_vardecl_shortform_wrong_type(self):
        input = """a:123;"""
        expect = "Error on line 1 col 2: 123"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_vardecl_shortform_missing_type(self):
        input = """a;"""
        expect = "Error on line 1 col 1: ;"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_vardecl_shortform_missing_semicolon(self):
        input = """a:integer"""
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_vardecl_shortform_missing_id_list(self):
        input = """:integer;"""
        expect = "Error on line 1 col 0: :"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_vardecl_shortform_wrong_id_list(self):
        input = """123,456:integer;"""
        expect = "Error on line 1 col 0: 123"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_vardecl_shortform_multi_type(self):
        input = """a123,b456:integer,float;"""
        expect = "Error on line 1 col 17: ,"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_vardecl_fullform_single(self):
        input = """a:boolean = 123;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_vardecl_fullform_multiple(self):
        input = """a,b,c:boolean = 123,true,1.2e3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_vardecl_fullform_missing_expr(self):
        input = """a,b,c:boolean = ;"""
        expect = "Error on line 1 col 16: ;"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_vardecl_fullform_missing_equal_sign(self):
        input = """a,b,c:boolean 123,true,1.2e3;"""
        expect = "Error on line 1 col 14: 123"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_vardecl_fullform_missing_double_equal_sign(self):
        input = """a,b,c:boolean == 123,true,1.2e3;"""
        expect = "Error on line 1 col 14: =="
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_vardecl_fullform_unequal_IDlist_exprlist_1(self):
        input = """a,b:boolean = 123,true,1.2e3;"""
        expect = "Error on line 1 col 22: ,"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_vardecl_fullform_unequal_IDlist_exprlist_2(self):
        input = """a,b,c:boolean = 123,1.2e3;a,c:boolean = 123,1.2e3;"""
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_vardecl_complex_test(self):
        input = """a,a12__, A1, _: array [10,3,2] of integer = {a,"abc",true,1.3e19},{true},{},a(1,2,{123,2});"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))


    """Test function declaration"""
    def test_function_prototype_multi_ID(self):
        input = """a,b:function integer(){}"""
        expect = "Error on line 1 col 4: function"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_function_prototype_missing_colon(self):
        input = """a function integer(){}"""
        expect = "Error on line 1 col 2: function"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_function_prototype_missing_function(self):
        input = """a : integer(){}"""
        expect = "Error on line 1 col 11: ("
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_function_prototype_missing_return_type(self):
        input = """a : function(){}"""
        expect = "Error on line 1 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_function_prototype_missing_parameter(self):
        input = """a : function integer{}"""
        expect = "Error on line 1 col 20: {"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_function_prototype_return_type_atomin(self):
        input = """a : function integer(){}
                   b : function float(){}
                   c : function string(){}
                   d : function boolean(){}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_function_prototype_return_type_array_void_auto(self):
        input = """a : function array[1,2]of integer(){}
                   b : function void(){}
                   c : function auto(){}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_function_prototype_return_type_wrong(self):
        input = """b : function void(){}\na : function double(){}"""
        expect = "Error on line 2 col 13: double"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_function_prototype_multi_return_type(self):
        input = """a: function integer float (){}"""
        expect = "Error on line 1 col 20: float"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_function_prototype_multi_return_type(self):
        input = """a: function integer float (){}"""
        expect = "Error on line 1 col 20: float"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_function_prototype_multi_paralist(self):
        input = """a: function float()(){}"""
        expect = "Error on line 1 col 19: ("
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_function_prototype_para_simple(self):
        input = """a: function float(a:integer, b:boolean){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_function_prototype_para_inherit_out(self):
        input = """a: function float(inherit a:integer, out b:boolean, inherit out c: string){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_function_prototype_para_inherit_out_disorder(self):
        input = """a: function float(out inherit c: string){}"""
        expect = "Error on line 1 col 22: inherit"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_function_prototype_para_type(self):
        input = """a: function float(a:integer, b:float, c:string, d:boolean, e:auto, f:array [123] of integer){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_function_prototype_para_type_wrong(self):
        input = """a: function float(a:integer, b:Float){}"""
        expect = "Error on line 1 col 31: Float"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_function_prototype_para_type_init(self):
        input = """a: function float(a:integer, b:float=1.3e1){}"""
        expect = "Error on line 1 col 36: ="
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_function_prototype_inherit(self):
        input = """a: function float()inherit a{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_function_prototype_inherit_missing_fname(self):
        input = """a: function float()inherit{}"""
        expect = "Error on line 1 col 26: {"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_function_prototype_inherit_multi_fname(self):
        input = """a: function float()inherit a b{}"""
        expect = "Error on line 1 col 29: b"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_function_body_missing(self):
        input = """a: function float()"""
        expect = "Error on line 1 col 19: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_function_body_multi(self):
        input = """a: function float(){}{}"""
        expect = "Error on line 1 col 21: {"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_function_semicolon(self):
        input = """a: function float(){};"""
        expect = "Error on line 1 col 21: ;"
        self.assertTrue(TestParser.test(input, expect, 250))
        
    
    """Test expression"""
    def test_expr_operator_sign(self):
        input = """a:integer = -"abc";
                b:boolean = -1.2e-10;
                c:float = -true;
                d:string = -1_23_45;
                e:array [2] of integer = -abc;
                d:integer = -{-1,-2,-3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_expr_operator_sign_missing(self):
        input = """a:integer = -;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_expr_operator_arithmetic(self):
        input = """a:integer = 1 + "abc";
                b:boolean = 1.2e-10-10;
                c:float = false*{1,"true",true};
                d:string = 1_2/3_45;
                e:array [2] of boolean = 22%abc123;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_expr_operator_arithmetic_missing(self):
        input = """a:integer = false*;b:float;"""
        expect = "Error on line 1 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_expr_operator_negate(self):
        input = """a:integer = !"abc";
                b:boolean = !1.2e-10;
                c:float = !true;
                d:string = !1_23_45;
                e:array [2] of integer = !abc;
                d:integer = !{-1,-2,-3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_expr_operator_negate_missing(self):
        input = """a:integer = !;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_expr_operator_boolean(self):
        input = """a:integer = {a,b,c}&&"abc";
                b:boolean = abc||1.2e-10;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_expr_operator_boolean_missing(self):
        input = """a:integer = &&"abc";
                b:boolean = abc||;"""
        expect = "Error on line 1 col 12: &&"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_expr_operator_stringconcat(self):
        input = """a:integer = {a,b,c}::"abc";
                b:string = abc::1.2e-10;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_expr_operator_stringconcat_missing(self):
        input = """a:integer = ::"abc";
                b:boolean = abc::;"""
        expect = "Error on line 1 col 12: ::"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_expr_operator_relational(self):
        input = """a:integer = 1 == "abc";
                b:boolean = 1.2e-10!=10;
                c:float = false<{1,"true",true};
                d:string = 1_2>3_45;
                e:array [2] of boolean = 22>=bc123;
                f,g:array [3,4] of string = 3>1,3<1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_expr_operator_relational_missing(self):
        input = """a:integer = <="abc";
                b:boolean = abc>=;"""
        expect = "Error on line 1 col 12: <="
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_expr_index_operator(self):
        input = """a:integer = a[1];
                b:float = a[b[1],c[2,3],3];
                c:string=a[b[c[1]]];
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_expr_index_operator_missing_index(self):
        input = """a:integer = a[];b:integer=a[1];"""
        expect = "Error on line 1 col 14: ]"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_expr_index_operator_complex_index(self):
        input = """a:integer = a[abc];
                b:float = a[abc(123)];
                c:string= a[1.2e-10];
                d:boolean = a[true];
                e:string = a["abc"];
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_expr_index_operator_invalid_index(self):
        input = """a:integer = a[a:integer;];"""
        expect = "Error on line 1 col 15: :"
        self.assertTrue(TestParser.test(input, expect, 266))
    
    def test_expr_index_function_call(self):
        input = """a:integer = a(1,2,3); b:float = _("string",abc,a(2,3,4));"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_expr_index_function_call_empty_arg(self):
        input = """a:integer = a(); b:float = _();"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_expr_multi_mixing_arithmentic(self):
        input = """a:integer = a --{10} - func(1234,func(1)) -- 10;\nb:boolean = a--------10---10-10;\na:integer = 1 * 2 - 3- - 4 / 5 % 6;\nb:boolean = 1*-2*-3*4/-2/3/4/5+-2+3+4+6%3%-2%3--1--3;\nc:array[1] of integer = -{a,b}*a--/a;"""
        expect = "Error on line 5 col 34: /"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_expr_multi_mixing_boolean(self):
        input = """a:integer = !a||b&&!c&&abc(123); b:boolean = !!!!!!!!!!!!!true&&!!!!!!"abc";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_expr_multi_mixing_relational(self):
        input = """a:integer = a==1!="abc"; b:boolean = a<=1<true>1.3e10>="true"!={ab,c}==func(123,"TRUE");"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_expr_multi_mixing_indexop(self):
        input = """a:integer = a[a[a[a[a]]]]; b:float = a[abc,func(123),1+2+3,1.2e19+"true",{a,b}<=1<2,abc::a];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_expr_multi_mixing_funccall(self):
        input = """a:integer = a(a(a(a(a(a))))); b:float = a(abc,func[123],1+2+3,1.2e19+"true",1<=1<2,abc::a);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_expr_complex(self):
        input = """a:integer = a(1+1.2/3==1-!!!!(true==abc)*{abc,c}>func(123,e)<=func());"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_expr_arraylit_test(self):
        input = """a:integer = {a};b:float={a,b,c,123};c:boolean={};d:string={{{{{{abc},2}}},4,5}};d:array[2]of integer={1,2+3/4,1+1.2/3,1-!!!!true==abc,{abc,c}>func(123,e)<=func()};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    """Statement test"""
    def test_stmt_assignment(self):
        input = """f : function integer () {a=1; a[1,3,4] = "true";}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_stmt_assignment_incorrect_lhs(self):
        input = """f : function integer () {123=1; a[1,3,4] = "true";}"""
        expect = "Error on line 1 col 25: 123"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_stmt_assignment_multiple_expr(self):
        input = """f : function integer () {a[1,3,4] = "true","false";}"""
        expect = "Error on line 1 col 42: ,"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_stmt_if(self):
        input = """f : function integer () {
                            if(abc==1) a=1;
                            if(true::a(123)){
                                abc=1;
                                if(1)a=1;
                            }
                            else{
                                if(abc_==1.52e19) {}
                            }
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_stmt_if_missing_expr(self):
        input = """f : function integer () {if () a=1;}"""
        expect = "Error on line 1 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_stmt_if_missing_true_statament(self):
        input = """f : function integer () {if (a==1) else b=1;}"""
        expect = "Error on line 1 col 35: else"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_stmt_for(self):
        input = """f : function integer () {
                        for (i=1, i<10, i+1){
                        for (abc=abc(123), i=="true", "abc"::1.3e2){}
                        }
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_stmt_for_missing(self):
        input = """f : function integer () {for (i=10, i+1){}}"""
        expect = "Error on line 1 col 39: )"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_stmt_while(self):
        input = """f : function integer () {
                        while (a::abc){
                            while(1<3){}
                            abc = 1;
                        }
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_stmt_while_missing_expr(self):
        input = """f : function integer () {while (){}}"""
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_stmt_while_missing_statement(self):
        input = """f : function integer () {while (a==1)}"""
        expect = "Error on line 1 col 37: }"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_stmt_do_while(self):
        input = """f : function integer () {
                        do {
                            do {}
                            while (ab==cd);
                        }
                        while (a::abc);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_stmt_do_while_while(self):
        input = """f : function integer () {do {}while (a::abc){};}"""
        expect = "Error on line 1 col 44: {"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_stmt_do_while_blockstm(self):
        input = """f:function integer () {do a=1; while (a::abc);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_stmt_do_while_missing_expr(self):
        input = """f:function integer () {do {} while ();}"""
        expect = "Error on line 1 col 36: )"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_stmt_break(self):
        input = """f : function integer () {
                        break;
                        do {
                            break;
                        }
                        while (a::abc);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_stmt_continue(self):
        input = """f : function integer () {
                        continue;
                        do {
                            continue;
                        }
                        while (a::abc);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_stmt_return(self):
        input = """f : function integer () {
                        return a==b;
                        return abc[123];
                        do {
                            return true >= abc(123);
                            a:integer = 1;
                            return;
                        }
                        while (a::abc);
                        return;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_stmt_call(self):
        input = """f : function integer () {
                    abc();
                    abc(abc(123));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_stmt_block(self):
        input = """f : function integer () {
                    {
                        {}
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_stmt_block_function_inside(self):
        input = """f:function integer () {a: function integer(){}}"""
        expect = "Error on line 1 col 26: function"
        self.assertTrue(TestParser.test(input, expect, 296))
    
    """Comment test"""
    def test_comment_between_statement(self):
        input = """f:function /*bwt*/ integer(){abc = /*Between*/ 123;}/*bwt*/"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_comment_unclosed(self):
        input = """f:function /*bwt*/ integer(){abc = /*Between*/ 123;}/*"""
        expect = "Error on line 1 col 52: /"
        self.assertTrue(TestParser.test(input, expect, 298))
    
    """Simple program test"""
    def test_program(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

