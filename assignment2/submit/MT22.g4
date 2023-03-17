grammar MT22;

// Name: Tran Tri Dat
// ID: 2052443

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls EOF;
decls: decl decls | decl;
decl: vardecl | funcdecl;

////////// Declarations //////////

// Variable declaration
vardecl: (shortvardecl | fulvardecl) SEMICOLON;
shortvardecl: idlist COLON vartype;
fulvardecl: ID COLON vartype EQUAL expr | ID COMMA fulvardecl COMMA expr;

arraydecl: ARRAYTYPE LSQB intlitlist RSQB 'of' eletype;
eletype: atomictype;

vartype: atomictype | AUTOTYPE |  arraydecl;

intlitlist: INTLIT COMMA intlitlist | INTLIT;

idlist: ID COMMA idlist | ID;
exprlist: expr COMMA exprlist | expr; 

// Function declaration
funcdecl: funcproto funcbody;

funcproto: ID COLON FUNCKEYW returntype LB paralistdecl? RB (INHERIT ID)?;
funcbody: blockstmt;

returntype: atomictype | VOIDTYPE | AUTOTYPE | arraydecl;
paralistdecl: paradecl COMMA paralistdecl | paradecl;
paradecl: INHERIT? OUT? ID COLON vartype;


////////// EXPRESSIONS //////////
expr: stringexpr;

// String //
stringexpr: stringexpr STRINGCONCAT relationalexpr | relationalexpr;

// Relational //
relationalexpr: relationalexpr RELATIONALOP logical_and_orexpr | logical_and_orexpr;

// Logical and or //
logical_and_orexpr: logical_and_orexpr (CONJUNCOP|DISJUNCOP) addingexpr | addingexpr;

// Adding //
addingexpr: addingexpr (PLUSOP|MINUSOP) multiplyingexpr | multiplyingexpr;

// Multiplying //
multiplyingexpr: multiplyingexpr (MULTIPLYOP|DIVIDEOP|MODULOOP) logical_negateexpr | logical_negateexpr;

// Logical negate//
logical_negateexpr: NEGATEOP logical_negateexpr | signexpr; 

// Sign minus//
signexpr: MINUSOP signexpr | indexopexpr;

// Index operator //
indexopexpr: indexop | operand;

// Operand //
operand: const | var | funccall | arraylit | bracket;

bracket: LB expr RB;

const: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT;
var: ID;
funccall: ID LB arglist? RB;
arglist: arg COMMA arglist | arg;
arg: expr;

////////// ARRAY LITERRAL //////////
arraylit: LCB exprlist? RCB;


// Special expressions //
// specialepxr: readint | readfloat | readbool | readstring;

// readint: 'readInteger' LB RB;
// readfloat: 'readFloat' LB RB;
// readbool: 'readBoolean' LB RB;
// readstring: 'readString' LB RB;


////////// STATEMENTS //////////

stmt: assignstmt SEMICOLON | ifstmt | forstmt | whilestmt | dowhilestmt SEMICOLON | breakstmt SEMICOLON 
	| continuestmt SEMICOLON | returnstmt SEMICOLON | callstmt SEMICOLON | blockstmt ;

// Assign statment //
assignstmt: lhs EQUAL expr;

lhs: ID | indexop;
indexop:ID LSQB exprlist RSQB;

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
returnstmt: 'return' expr?;

// Call statement //
callstmt: funccall;

// Block statement//
blockstmt: LCB blockBody? RCB;

blockBody: (stmt|vardecl) blockBody | (stmt|vardecl);

// Special statements //
// specialstmt: (printint | writefloat | printbool | printstring | superfunc | preventdef) SEMICOLON;

// printint: 'printInteger' LB (ID|INTLIT) RB;
// writefloat: 'writeFloat' LB (ID|FLOATLIT) RB;
// printbool: 'printBoolean' LB (ID|BOOLEANLIT) RB;
// printstring: 'printString' LB (ID|STRINGLIT) RB;
// superfunc: 'super' LB exprlist RB;
// preventdef: 'preventDefault' LB RB;


////////// TYPES //////////
atomictype: BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE;

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

STRINGLIT: '"' (~[\n\r"\\]|'\\'[tbfrn'"\\])* '"' {self.text = self.text[1:-1];};

fragment LETTER: [A-Za-z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';
ID: (LETTER|UNDERSCORE) (LETTER|UNDERSCORE|DIGIT)*; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' (~[\n\r"\\]|'\\'[tbfrn'"\\])* {
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