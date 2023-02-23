grammar MT22;

// Name: Tran Tri Dat
// ID: 2052443

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls? EOF;
decls: decl decls | decl;
decl: vardecl | funcdecl;

////////// Declarations //////////

// Variable declaration
vardecl: (shortvardecl | fulvardecl | arraydecl) SEMICOLON;
shortvardecl: idlist COLON vartype;
fulvardecl: ID COLON vartype EQUAL expr | var COMMA fulvardecl COMMA expr;
arraydecl: idlist COLON ARRAYTYPE LSQB INTLIT RSQB 'of' vartype;		

idlist: ID COMMA idlist | ID;
exprlist: expr COMMA exprlist | expr; 

// Function declaration
funcdecl: funcproto funcbody;

funcproto: ID COLON FUNCKEYW returntype LB paralistdecl? RB (INHERIT ID)?;
funcbody: blockstmt;

returntype: vartype | VOIDTYPE | AUTOTYPE;
paralistdecl: paradecl COMMA paralistdecl | paradecl;
paradecl: INHERIT? OUT? ID COLON vartype;


////////// EXPRESSIONS //////////
expr: indexop | specialepxr;

// Index operator //
indexop: ID LSQB indexop COMMA sign RSQB | ID LSQB sign RSQB | sign;

// Sign minus//
sign: MINUSOP sign | MINUSOP logical_negate | logical_negate;

// Logical negate//
logical_negate: NEGATEOP logical_negate | NEGATEOP multiplying | multiplying; 

// Multiplying //
multiplying: multiplying (MULTIPLYOP|DIVIDEOP|MODULOOP) adding | adding;

// Adding //
adding: adding (PLUSOP|MINUSOP) logical_and_or | logical_and_or;

// Logical and or //
logical_and_or: logical_and_or (CONJUNCOP|DISJUNCOP) relational | relational;

// Relational //
relational: string RELATIONALOP string | string;

// String //
string: operand STRINGCONCAT operand | operand;

// Operand //
operand: const | var | funccall;

const: INTLIT | FLOATLIT | STRINGLIT;
var: ID;
funccall: ID LB arglist? RB;
arglist: arg COMMA arglist | arg;
arg: expr;

// Special expressions //
specialepxr: readint | readfloat | readbool | readstring;

readint: 'readInteger' LB RB;
readfloat: 'readFloat' LB RB;
readbool: 'readBoolean' LB RB;
readstring: 'readString' LB RB;


////////// STATEMENTS //////////

stmt: assignstmt SEMICOLON | ifstmt | forstmt | whilestmt | dowhilestmt SEMICOLON | breakstmt SEMICOLON 
	| continuestmt SEMICOLON | returnstmt SEMICOLON | callstmt SEMICOLON | specialstmt;

// Assign statment //
assignstmt: lhs EQUAL expr;

lhs: ID | indexop;

// If statement //
ifstmt: 'if' LB expr RB stmt ('else' stmt)?;

// For statement //
forstmt: 'for' LB ID EQUAL expr COMMA expr COMMA expr RB stmt;

// While statement //
whilestmt: 'while' LB expr RB stmt;

// Do-while statement //
dowhilestmt: 'do' blockstmt 'while' LB expr RB;	

// Break statement //
breakstmt: 'break';

// Continue statement //
continuestmt: 'continue';

// Return statement //
returnstmt: 'return' expr;

// Call statement //
callstmt: funccall;

// Block statement//
blockstmt: LCB blockBody? RCB;

blockBody: (stmt|vardecl) blockBody | (stmt|vardecl);

// Special statements //
specialstmt: (printint | writefloat | printbool | printstring | superfunc | preventdef) SEMICOLON;

printint: 'printInteger' LB (ID|INTLIT) RB;
writefloat: 'writeFloat' LB (ID|FLOATLIT) RB;
printbool: 'printBoolean' LB (ID|BOOLEANLIT) RB;
printstring: 'printString' LB (ID|STRINGLIT) RB;
superfunc: 'super' LB exprlist RB;
preventdef: 'preventDefault' LB RB;


////////// TYPES //////////
vartype: BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE;


////////// ARRAY!!! //////////
array: LCB exprlist RCB;

////////// TOKENS //////////

FUNCKEYW: 'function';

INHERIT: 'inherit';
OUT: 'out';

COMMA: ',';
COLON: ':';
SEMICOLON: ';';
EQUAL: '=';
DOT: '.';

OPENCMT: '/*' .*? '*/' -> skip;
LINECMT: '//' (~[\n\r])* -> skip;

PLUSOP: '+';
MINUSOP: '-';
MULTIPLYOP: '*';
DIVIDEOP: '/';
MODULOOP: '%';
NEGATEOP: '!';
CONJUNCOP: '&&';
DISJUNCOP: '||';
RELATIONALOP:  '==' | '!=' | '<' | '<=' | '>' | '>=' ;
STRINGCONCAT: '::';

LB: '(';
RB: ')';
LSQB: '[';
RSQB: ']';
LCB: '{';
RCB: '}';

BOOLTYPE: 'boolean';
INTTYPE: 'integer';
FLOATTYPE: 'float';
STRINGTYPE: 'string';
VOIDTYPE: 'void';
AUTOTYPE: 'auto';
ARRAYTYPE: 'array';

fragment NONZERODIGIT: [1-9];
INTLIT: '0'|NONZERODIGIT DIGIT* ('_' DIGIT|DIGIT)*{self.text = self.text.replace('_','')};

fragment DECIMAL: DOT DIGIT*;
fragment EXP: [eE] [+-]? DIGIT+;
FLOATLIT: INTLIT DECIMAL EXP {self.text = self.text.replace('_','')}
		| INTLIT DECIMAL {self.text = self.text.replace('_','')}
		| INTLIT EXP {self.text = self.text.replace('_','')}
		| DECIMAL EXP;

fragment TRUE: 'true';
fragment FALSE: 'false';
BOOLEANLIT: TRUE | FALSE;

STRINGLIT: '"' (~["\\]|'\\'[tbfrn'"\\])* '"' {self.text = self.text[1:-1];};

fragment LETTER: [A-Za-z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';
ID: (LETTER|UNDERSCORE) (LETTER|UNDERSCORE|DIGIT)*; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' (~["\\]|'\\'[tbfrn'"\\])* {
	self.text = self.text[1:];
	raise UncloseString(self.text)
};

ILLEGAL_ESCAPE: '"' (~["\\]|'\\'[tbfrn'"\\])*('\\'~[tbfrn'"\\]){
	self.text = self.text[1:];
	raise IllegalEscape(self.text)
};

ERROR_CHAR: . {
	raise ErrorToken(self.text)
};