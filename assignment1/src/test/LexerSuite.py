import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    """Test empty"""
    def test_empty_program(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 100))

    """Test skip character"""
    def test_skip_chracter_tab(self):
        self.assertTrue(TestLexer.test("abc\t123", "abc,123,<EOF>", 101))
    def test_skip_chracter_space(self):
        self.assertTrue(TestLexer.test("abc              123", "abc,123,<EOF>", 102))
    def test_skip_chracter_carriage_return(self):
        self.assertTrue(TestLexer.test("abc\r123", "abc,123,<EOF>", 103))
    def test_skip_chracter_newline(self):
        self.assertTrue(TestLexer.test("abc\n123", "abc,123,<EOF>", 104))

    """Test comment block"""
    def test_comment_block(self):
        self.assertTrue(TestLexer.test("/*This code is inside a comment block*/", "<EOF>", 105))
    def test_comment_block_multiple_line(self):
        self.assertTrue(TestLexer.test("a = 5;/* This code is inside a comment block\n This is another line in block*/", "a,=,5,;,<EOF>", 106))
    def test_comment_block_between(self):
        self.assertTrue(TestLexer.test("a = 5;/* This code is inside a comment block*/b=10;", "a,=,5,;,b,=,10,;,<EOF>", 107))
    def test_comment_block_like(self):
        self.assertTrue(TestLexer.test("a=5;*/b=10;", "a,=,5,;,*,/,b,=,10,;,<EOF>", 108)) 
    def test_comment_block_unclosed(self):
        self.assertTrue(TestLexer.test("a = 5;/* This code is a unclosed comment block b=10;", "a,=,5,;,/,*,This,code,is,a,unclosed,comment,block,b,=,10,;,<EOF>", 109))
    def test_comment_block_nested(self):
        self.assertTrue(TestLexer.test("/* /*This code is inside a comment block */*/", "*,/,<EOF>", 110)) 
    def test_comment_block_complex_1(self):
        self.assertTrue(TestLexer.test("/*This code * is/ inside/*/ a comment block*/", "a,comment,block,*,/,<EOF>", 111))
    def test_comment_block_complex_2(self):
        self.assertTrue(TestLexer.test("/*************/", "<EOF>", 112))
    def test_comment_block_complex_3(self):
        self.assertTrue(TestLexer.test("/******/*******/", "*,*,*,*,*,*,*,/,<EOF>", 113))
    
    """Test inline comment"""
    def test_comment_line_before(self):
        self.assertTrue(TestLexer.test("// This code is inside a comment block // abc", "<EOF>", 114))
    def test_comment_line_after(self):
        self.assertTrue(TestLexer.test("a = 5;// This code is inside a comment block*/", "a,=,5,;,<EOF>", 115))
    def test_comment_line_duplicated(self):
        self.assertTrue(TestLexer.test("//////////////////", "<EOF>", 116))
    def test_comment_line_tab(self):
        self.assertTrue(TestLexer.test("//\tabc", "<EOF>", 117))
    def test_comment_line_carriage_return(self):
        self.assertTrue(TestLexer.test("//\rabc", "abc,<EOF>", 118))
    def test_comment_line_newline(self):
        self.assertTrue(TestLexer.test("//\nabc", "abc,<EOF>", 119))
    def test_comment_line_complex(self):
        self.assertTrue(TestLexer.test("a = 5;// This code is inside a comment block*/\nb=10;//This is another comment", "a,=,5,;,b,=,10,;,<EOF>", 120))
      
    """Test identifier"""
    def test_identifier_only_low_upper_letter(self):
        self.assertTrue(TestLexer.test("abcdef; ABCDEF", "abcdef,;,ABCDEF,<EOF>", 121)) 
    def test_identifier_mix_upper_lower_letter(self):
        self.assertTrue(TestLexer.test("aBcDeF;AbCdEf", "aBcDeF,;,AbCdEf,<EOF>", 122))
    def test_identifier_underscore(self):
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 123)) 
    def test_identifier_multiple_underscore(self):
        self.assertTrue(TestLexer.test("__a___b_____c", "__a___b_____c,<EOF>", 124)) 
    def test_identifier_digit(self):
        self.assertTrue(TestLexer.test("_123 _ab123", "_123,_ab123,<EOF>", 125)) 
    def test_failed_identifier_digit_begin(self):
        self.assertTrue(TestLexer.test("9abc", "9,abc,<EOF>", 126)) 
    def test_identifier_invalid_character(self):
        self.assertTrue(TestLexer.test("a.b-c!d)e(f", "a,.,b,-,c,!,d,),e,(,f,<EOF>", 127)) 
    def test_identifier_underscore_only(self):
        self.assertTrue(TestLexer.test("_ __ ___ ____", "_,__,___,____,<EOF>", 128))
    
    """Test operators"""
    def test_operator(self):
        self.assertTrue(TestLexer.test("+-*/%!&&||==!=<<=>>=::", "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>", 129))
    def test_not_operator_and(self):
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 130))
    def test_not_operator_or(self):
        self.assertTrue(TestLexer.test("|||", "||,Error Token |", 131))
    def test_operator_using(self):
        self.assertTrue(TestLexer.test("a+b-c*123/999%abc!0&&1||2==3!=4<5<=6>7>=8::9", "a,+,b,-,c,*,123,/,999,%,abc,!,0,&&,1,||,2,==,3,!=,4,<,5,<=,6,>,7,>=,8,::,9,<EOF>", 132))
    def test_comment_like_operator(self):
        self.assertTrue(TestLexer.test("/*", "/,*,<EOF>", 133))
    def test_operator_like_comment_block(self):
        self.assertTrue(TestLexer.test("/**/", "<EOF>", 134))
    def test_operator_like_comment_line(self):
        self.assertTrue(TestLexer.test("//", "<EOF>", 135))
    
    """Test seperators"""
    def test_seperator(self):
        self.assertTrue(TestLexer.test("()[].,;:{}=", "(,),[,],.,,,;,:,{,},=,<EOF>", 136))
    def test_seperator_spacing(self):
        self.assertTrue(TestLexer.test("( ) [ ] . , ; : { } = ", "(,),[,],.,,,;,:,{,},=,<EOF>", 137))
    def test_seperator_using(self):
        self.assertTrue(TestLexer.test("(123)[abc] a.1 1,f;a:2{1234}=789", "(,123,),[,abc,],a,.,1,1,,,f,;,a,:,2,{,1234,},=,789,<EOF>", 138))
    def test_seperator_like_operator(self):
        self.assertTrue(TestLexer.test(":: ==", "::,==,<EOF>", 139))
    def test_seperator_nested(self):
        self.assertTrue(TestLexer.test("([{.,;:=]})", "(,[,{,.,,,;,:,=,],},),<EOF>", 140))
    
    """Test integer literal"""
    def test_integer_literal_zero(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 141))
    def test_integer_literal_non_zero(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 142))
    def test_integer_literal_zero_precede(self):
        self.assertTrue(TestLexer.test("0123", "0,123,<EOF>", 143))
    def test_integer_literal_zero_precede_multiple(self):
        self.assertTrue(TestLexer.test("00001", "0,0,0,0,1,<EOF>", 144))
    def test_integer_literal_underscore(self):
        self.assertTrue(TestLexer.test("1_23_456_7890", "1234567890,<EOF>", 145))
    def test_integer_literal_underscore_failed(self):
        self.assertTrue(TestLexer.test("_1_2", "_1_2,<EOF>", 146))
    def test_integer_literal_underscore_adjacent(self):
        self.assertTrue(TestLexer.test("1_2__3___4", "12,__3___4,<EOF>", 147))
    def test_integer_literal_underscore_last(self):
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 148))
    def test_integer_literal_digit_between(self):
        self.assertTrue(TestLexer.test("123a456 123_0a_456 123_a_456", "123,a456,1230,a_456,123,_a_456,<EOF>", 149))
    def test_integer_literal_underscore_zero(self):
        self.assertTrue(TestLexer.test("0_1;1_0;01_23", "0,_1,;,10,;,0,123,<EOF>", 150))
    def test_integer_literal_length(self):
        self.assertTrue(TestLexer.test("123456789123456789123456789123456789", "123456789123456789123456789123456789,<EOF>", 151))
    
    """Test float literal"""
    def test_float_literal_integer_decimal(self):
        self.assertTrue(TestLexer.test("1.234 1_234.567 123.", "1.234,1234.567,123.,<EOF>", 152))
    def test_float_literal_integer_decimal_failed(self):
        self.assertTrue(TestLexer.test("1.23_4 0,123", "1.23,_4,0,,,123,<EOF>", 153))
    def test_float_literal_integer_decimal_zero(self):
        self.assertTrue(TestLexer.test("0.123 123.0 0.000123 0.000 00.123 0.", "0.123,123.0,0.000123,0.000,0,0.123,0.,<EOF>", 154))
    def test_float_literal_integer_exponent(self):
        self.assertTrue(TestLexer.test("123e123 123E123 123e-123 123e+123 123E-123 123e-123 ", "123e123,123E123,123e-123,123e+123,123E-123,123e-123,<EOF>", 155))
    def test_float_literal_integer_exponent_zero(self):
        self.assertTrue(TestLexer.test("0e0 0e-0 0E+0 0e0000", "0e0,0e-0,0E+0,0e0000,<EOF>", 156))
    def test_float_literal_integer_exponent_failed(self):
        self.assertTrue(TestLexer.test("123e+-123 123e-+123 123e1_23 123eE123", "123,e,+,-,123,123,e,-,+,123,123e1,_23,123,eE123,<EOF>", 157))
    def test_float_literal_decimal_exponent(self):
        self.assertTrue(TestLexer.test(".123e123 .123E+123 .123e-123 .e123", ".123e123,.123E+123,.123e-123,.e123,<EOF>", 158))
    def test_float_literal_decimal_exponent_zero(self):
        self.assertTrue(TestLexer.test(".000e000 .000e+000 .000E-000 .E000", ".000e000,.000e+000,.000E-000,.E000,<EOF>", 159))
    def test_float_literal_decimal_exponent_failed(self):
        self.assertTrue(TestLexer.test(".123e .123E+-123 .e--123 .E .E++123", ".,123,e,.,123,E,+,-,123,.,e,-,-,123,.,E,.,E,+,+,123,<EOF>", 160))
    def test_float_literal_integer_decimal_exponent(self):
        self.assertTrue(TestLexer.test("123.123e123 1_2_3.123E+123 123.E-123 123.e+00123 12300.123000e-123000", "123.123e123,123.123E+123,123.E-123,123.e+00123,12300.123000e-123000,<EOF>", 161))
    def test_float_literal_integer_decimal_exponent_zero(self):
        self.assertTrue(TestLexer.test("0.0000e+000 0.0001E0001 0.E-0", "0.0000e+000,0.0001E0001,0.E-0,<EOF>", 162))
    def test_float_literal_integer_decimal_exponent_failed(self):
        self.assertTrue(TestLexer.test("123._123e+_123", "123.,_123e,+,_123,<EOF>", 163))
    def test_float_literal_multiple_decimal(self):
        self.assertTrue(TestLexer.test("123.123.123 123.123.123.123", "123.123,.,123,123.123,.,123.123,<EOF>", 164))
    def test_float_literal_multiple_exponent(self):
        self.assertTrue(TestLexer.test("123e+123e-123 123.123e123-123e123e123E123", "123e+123,e,-,123,123.123e123,-,123e123,e123E123,<EOF>", 165))

    """Test boolean literal"""
    def test_boolean_literal(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 166))
    def test_boolean_literal_failed(self):
        self.assertTrue(TestLexer.test("truefalse atrue bfalse true123 false456", "truefalse,atrue,bfalse,true123,false456,<EOF>", 167))

    """Test string literal"""
    def test_string_literal_no_escape(self):
        self.assertTrue(TestLexer.test("\"abc 123 =+- ~!#\"", "abc 123 =+- ~!#,<EOF>", 168))
    def test_string_literal_between(self):
        self.assertTrue(TestLexer.test("123\"  abc  \"456", "123,  abc  ,456,<EOF>", 169))
    def test_string_literal_escape_backspace(self):
        self.assertTrue(TestLexer.test("\"This string contain backspace\\b\"", "This string contain backspace\\b,<EOF>", 170))
    def test_string_literal_escape_form_feed(self):
        self.assertTrue(TestLexer.test("\"This string contain form feed\\f\"", "This string contain form feed\\f,<EOF>", 171))
    def test_string_literal_escape_carriage_return(self):
        self.assertTrue(TestLexer.test("\"This string contain carriage return\\r\"", "This string contain carriage return\\r,<EOF>", 172))
    def test_string_literal_escape_newline(self):
        self.assertTrue(TestLexer.test("\"This string contain newline\\n\", \"And contain invalid newline\nand all this skipped\"", "This string contain newline\\n,,,Unclosed String: And contain invalid newline", 173))
    def test_string_literal_escape_horizontal_tab(self):
        self.assertTrue(TestLexer.test("\"This string contain horizontal tab\\t\"", "This string contain horizontal tab\\t,<EOF>", 174))
    def test_string_literal_escape_single_quote(self):
        self.assertTrue(TestLexer.test("\"This string contain single quote\\'\"", "This string contain single quote\\',<EOF>", 175))
    def test_string_literal_escape_backslash(self):
        self.assertTrue(TestLexer.test("\"This string contain backslash\\\\\"", "This string contain backslash\\\\,<EOF>", 176))
    def test_string_literal_escape_doublequote(self):
        self.assertTrue(TestLexer.test("\"He said: \\\"Hi! Is this valid?\\\"\"", "He said: \\\"Hi! Is this valid?\\\",<EOF>", 177))
    def test_string_literal_illegal_escape_case_sentive(self):
        self.assertTrue(TestLexer.test("\"abc\\N123\"", "Illegal Escape In String: abc\\N", 178))
    def test_string_literal_illegal_escape_number(self):
        self.assertTrue(TestLexer.test("\"abc\\3456\"", "Illegal Escape In String: abc\\3", 179))
    def test_string_literal_empty(self):
        self.assertTrue(TestLexer.test("\"\"", ",<EOF>", 180))
    def test_string_literal_unclosed(self):
        self.assertTrue(TestLexer.test("\"abc", "Unclosed String: abc", 181))
    def test_string_literal_unclosed_between(self):
        self.assertTrue(TestLexer.test("abc\"123", "abc,Unclosed String: 123", 182))
    def test_string_literal_unclosed_space(self):
        self.assertTrue(TestLexer.test("\"abc     ", "Unclosed String: abc     ", 183))
    def test_string_literal_unclosed_empty_space(self):
        self.assertTrue(TestLexer.test("\" ", "Unclosed String:  ", 184))
    def test_string_literal_unclosed_empty(self):
        self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 185))
    def test_string_literal_unclosed_escape(self):
        self.assertTrue(TestLexer.test("\"a\\bc", "Unclosed String: a\\bc", 186))
    def test_string_literal_multiple(self):
        self.assertTrue(TestLexer.test("\"abc\"    \"def\";  \"ghk", "abc,def,;,Unclosed String: ghk", 187))
    def test_string_literal_EOF(self):
        self.assertTrue(TestLexer.test("\"<EOF>\"<EOF>", "<EOF>,<,EOF,>,<EOF>", 188))
    def test_string_complex(self):
        self.assertTrue(TestLexer.test("\"The quick brown fox jumps over the lazy dog. The five boxing wizards jump quickly. 1234567890!@#$%^&*()_+{}|:\\\"<>?[];',./\"", "The quick brown fox jumps over the lazy dog. The five boxing wizards jump quickly. 1234567890!@#$%^&*()_+{}|:\\\"<>?[];',./,<EOF>", 189))

    """Test error token"""
    def test_error_token(self):
        self.assertTrue(TestLexer.test("abc`~", "abc,Error Token `", 190))
    def test_error_token_operator_like_and(self):
        self.assertTrue(TestLexer.test("abc&", "abc,Error Token &", 191))
    def test_error_token_operator_like_or(self):
        self.assertTrue(TestLexer.test("abc|", "abc,Error Token |", 192))
    def test_error_token_single_quote(self):
        self.assertTrue(TestLexer.test("abc'", "abc,Error Token '", 193))

    """Complex test"""
    def test_complex_1(self):
        self.assertTrue(TestLexer.test("grammar ComplexLexicalTest;\nexpression: INT PLUS INT;\nINT: DIGIT+;\nfragment DIGIT: [0-9];\nPLUS: '+';", "grammar,ComplexLexicalTest,;,expression,:,INT,PLUS,INT,;,INT,:,DIGIT,+,;,fragment,DIGIT,:,[,0,-,9,],;,PLUS,:,Error Token '", 194))
    def test_complex_2(self):
        self.assertTrue(TestLexer.test("ID(x) ASSIGN INT(42) SEMICOLON\nID(y) ASSIGN MINUS FLOAT(3.14) SEMICOLON\nID(z) ASSIGN SCIENTIFIC_FLOAT(1.23e-4) SEMICOLON\nID(result) ASSIGN ID(x) MULTIPLY ID(y) PLUS ID(z) DIVIDE INT(2) SEMICOLON\n", "ID,(,x,),ASSIGN,INT,(,42,),SEMICOLON,ID,(,y,),ASSIGN,MINUS,FLOAT,(,3.14,),SEMICOLON,ID,(,z,),ASSIGN,SCIENTIFIC_FLOAT,(,1.23e-4,),SEMICOLON,ID,(,result,),ASSIGN,ID,(,x,),MULTIPLY,ID,(,y,),PLUS,ID,(,z,),DIVIDE,INT,(,2,),SEMICOLON,<EOF>", 195))
    def test_complex_3(self):
        self.assertTrue(TestLexer.test("\"The quick brown fox jumps over the lazy dog. The five boxing wizards jump quickly. 1234567890!@#$%^&*()_+{}|:\"<>?[];',./\"", "The quick brown fox jumps over the lazy dog. The five boxing wizards jump quickly. 1234567890!@#$%^&*()_+{}|:,<,>,Error Token ?", 196))
    def test_complex_4(self):
        self.assertTrue(TestLexer.test("\"~^*#*%|}|<@=/(%)!&$;><?[}'_-+.,;:0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY\"", "~^*#*%|}|<@=/(%)!&$;><?[}'_-+.,;:0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY,<EOF>", 197))
    def test_complex_5(self):
        self.assertTrue(TestLexer.test("\"o[?%~U6a(YU1ki&uh3qM@Eon]D+_Z4wx{^H|\\2jF7*<#CgX)mS5yVR!t}#KdP^fL8b9cTspQ]B0z#N@O$vI&^AeG\"", "Illegal Escape In String: o[?%~U6a(YU1ki&uh3qM@Eon]D+_Z4wx{^H|\\2", 198))
    def test_complex_6(self):
        self.assertTrue(TestLexer.test("\"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~\"", "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~,<EOF>", 199))    