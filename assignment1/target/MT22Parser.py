# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01e4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\5")
        buf.write("\2v\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3~\n\3\3\4\3\4\5\4\u0082")
        buf.write("\n\4\3\5\3\5\3\5\5\5\u0087\n\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u009b")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u00aa\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00b1\n\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00bc\n\f\3\f\3")
        buf.write("\f\3\f\5\f\u00c1\n\f\3\r\3\r\3\16\3\16\3\16\5\16\u00c8")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00cf\n\17\3\20\5")
        buf.write("\20\u00d2\n\20\3\20\5\20\u00d5\n\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\5\21\u00dd\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ec\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u00f3\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00fa\n\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u0102\n\25\f\25\16\25\u0105\13\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u010d\n\26\f\26\16\26\u0110")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0118\n\27\f")
        buf.write("\27\16\27\u011b\13\27\3\30\3\30\3\30\3\30\3\30\5\30\u0122")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u0129\n\31\3\32\3")
        buf.write("\32\3\32\5\32\u012e\n\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\5\35\u0137\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u0140\n\36\3\37\3\37\3 \3 \3 \3 \5 \u0148\n ")
        buf.write("\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\5%\u0170\n%\3&\3&\3&\3&\3\'\3\'\5\'\u0178\n")
        buf.write("\'\3(\3(\3(\3(\3(\3(\3(\5(\u0181\n(\3)\3)\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\5\60\u01a7\n")
        buf.write("\60\3\60\3\60\3\61\3\61\5\61\u01ad\n\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u01b3\n\61\5\61\u01b5\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u01bd\n\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\3:\3:\3:\3:\3:\2\5(*,;\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\13\3\2!#\3\2\37 \3\2%&\4")
        buf.write("\289<<\4\288==\4\299==\4\2::==\3\2<=\3\2\60\63\2\u01e0")
        buf.write("\2u\3\2\2\2\4}\3\2\2\2\6\u0081\3\2\2\2\b\u0086\3\2\2\2")
        buf.write("\n\u008a\3\2\2\2\f\u009a\3\2\2\2\16\u009c\3\2\2\2\20\u00a9")
        buf.write("\3\2\2\2\22\u00b0\3\2\2\2\24\u00b2\3\2\2\2\26\u00b5\3")
        buf.write("\2\2\2\30\u00c2\3\2\2\2\32\u00c7\3\2\2\2\34\u00ce\3\2")
        buf.write("\2\2\36\u00d1\3\2\2\2 \u00dc\3\2\2\2\"\u00eb\3\2\2\2$")
        buf.write("\u00f2\3\2\2\2&\u00f9\3\2\2\2(\u00fb\3\2\2\2*\u0106\3")
        buf.write("\2\2\2,\u0111\3\2\2\2.\u0121\3\2\2\2\60\u0128\3\2\2\2")
        buf.write("\62\u012d\3\2\2\2\64\u012f\3\2\2\2\66\u0131\3\2\2\28\u0133")
        buf.write("\3\2\2\2:\u013f\3\2\2\2<\u0141\3\2\2\2>\u0147\3\2\2\2")
        buf.write("@\u0149\3\2\2\2B\u014d\3\2\2\2D\u0151\3\2\2\2F\u0155\3")
        buf.write("\2\2\2H\u016f\3\2\2\2J\u0171\3\2\2\2L\u0177\3\2\2\2N\u0179")
        buf.write("\3\2\2\2P\u0182\3\2\2\2R\u018e\3\2\2\2T\u0194\3\2\2\2")
        buf.write("V\u019b\3\2\2\2X\u019d\3\2\2\2Z\u019f\3\2\2\2\\\u01a2")
        buf.write("\3\2\2\2^\u01a4\3\2\2\2`\u01b4\3\2\2\2b\u01bc\3\2\2\2")
        buf.write("d\u01c0\3\2\2\2f\u01c5\3\2\2\2h\u01ca\3\2\2\2j\u01cf\3")
        buf.write("\2\2\2l\u01d4\3\2\2\2n\u01d9\3\2\2\2p\u01dd\3\2\2\2r\u01df")
        buf.write("\3\2\2\2tv\5\4\3\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2wx\7\2")
        buf.write("\2\3x\3\3\2\2\2yz\5\6\4\2z{\5\4\3\2{~\3\2\2\2|~\5\6\4")
        buf.write("\2}y\3\2\2\2}|\3\2\2\2~\5\3\2\2\2\177\u0082\5\b\5\2\u0080")
        buf.write("\u0082\5\24\13\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2")
        buf.write("\u0082\7\3\2\2\2\u0083\u0087\5\n\6\2\u0084\u0087\5\f\7")
        buf.write("\2\u0085\u0087\5\16\b\2\u0086\u0083\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\7\33\2\2\u0089\t\3\2\2\2\u008a\u008b\5\20\t\2\u008b")
        buf.write("\u008c\7\32\2\2\u008c\u008d\5p9\2\u008d\13\3\2\2\2\u008e")
        buf.write("\u008f\7=\2\2\u008f\u0090\7\32\2\2\u0090\u0091\5p9\2\u0091")
        buf.write("\u0092\7\34\2\2\u0092\u0093\5 \21\2\u0093\u009b\3\2\2")
        buf.write("\2\u0094\u0095\5\66\34\2\u0095\u0096\7\31\2\2\u0096\u0097")
        buf.write("\5\f\7\2\u0097\u0098\7\31\2\2\u0098\u0099\5 \21\2\u0099")
        buf.write("\u009b\3\2\2\2\u009a\u008e\3\2\2\2\u009a\u0094\3\2\2\2")
        buf.write("\u009b\r\3\2\2\2\u009c\u009d\5\20\t\2\u009d\u009e\7\32")
        buf.write("\2\2\u009e\u009f\7\66\2\2\u009f\u00a0\7+\2\2\u00a0\u00a1")
        buf.write("\78\2\2\u00a1\u00a2\7,\2\2\u00a2\u00a3\7\3\2\2\u00a3\u00a4")
        buf.write("\5p9\2\u00a4\17\3\2\2\2\u00a5\u00a6\7=\2\2\u00a6\u00a7")
        buf.write("\7\31\2\2\u00a7\u00aa\5\20\t\2\u00a8\u00aa\7=\2\2\u00a9")
        buf.write("\u00a5\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\21\3\2\2\2\u00ab")
        buf.write("\u00ac\5 \21\2\u00ac\u00ad\7\31\2\2\u00ad\u00ae\5\22\n")
        buf.write("\2\u00ae\u00b1\3\2\2\2\u00af\u00b1\5 \21\2\u00b0\u00ab")
        buf.write("\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\23\3\2\2\2\u00b2\u00b3")
        buf.write("\5\26\f\2\u00b3\u00b4\5\30\r\2\u00b4\25\3\2\2\2\u00b5")
        buf.write("\u00b6\7=\2\2\u00b6\u00b7\7\32\2\2\u00b7\u00b8\7\26\2")
        buf.write("\2\u00b8\u00b9\5\32\16\2\u00b9\u00bb\7)\2\2\u00ba\u00bc")
        buf.write("\5\34\17\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00c0\7*\2\2\u00be\u00bf\7\27\2\2")
        buf.write("\u00bf\u00c1\7=\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\27\3\2\2\2\u00c2\u00c3\5^\60\2\u00c3\31\3")
        buf.write("\2\2\2\u00c4\u00c8\5p9\2\u00c5\u00c8\7\64\2\2\u00c6\u00c8")
        buf.write("\7\65\2\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\33\3\2\2\2\u00c9\u00ca\5\36\20\2")
        buf.write("\u00ca\u00cb\7\31\2\2\u00cb\u00cc\5\34\17\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cf\5\36\20\2\u00ce\u00c9\3\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\35\3\2\2\2\u00d0\u00d2\7\27\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2")
        buf.write("\u00d3\u00d5\7\30\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7=\2\2\u00d7")
        buf.write("\u00d8\7\32\2\2\u00d8\u00d9\5p9\2\u00d9\37\3\2\2\2\u00da")
        buf.write("\u00dd\5\"\22\2\u00db\u00dd\5> \2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dc\u00db\3\2\2\2\u00dd!\3\2\2\2\u00de\u00df\7=\2\2")
        buf.write("\u00df\u00e0\7+\2\2\u00e0\u00e1\5\"\22\2\u00e1\u00e2\7")
        buf.write("\31\2\2\u00e2\u00e3\5$\23\2\u00e3\u00e4\7,\2\2\u00e4\u00ec")
        buf.write("\3\2\2\2\u00e5\u00e6\7=\2\2\u00e6\u00e7\7+\2\2\u00e7\u00e8")
        buf.write("\5$\23\2\u00e8\u00e9\7,\2\2\u00e9\u00ec\3\2\2\2\u00ea")
        buf.write("\u00ec\5$\23\2\u00eb\u00de\3\2\2\2\u00eb\u00e5\3\2\2\2")
        buf.write("\u00eb\u00ea\3\2\2\2\u00ec#\3\2\2\2\u00ed\u00ee\7 \2\2")
        buf.write("\u00ee\u00f3\5$\23\2\u00ef\u00f0\7 \2\2\u00f0\u00f3\5")
        buf.write("&\24\2\u00f1\u00f3\5&\24\2\u00f2\u00ed\3\2\2\2\u00f2\u00ef")
        buf.write("\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3%\3\2\2\2\u00f4\u00f5")
        buf.write("\7$\2\2\u00f5\u00fa\5&\24\2\u00f6\u00f7\7$\2\2\u00f7\u00fa")
        buf.write("\5(\25\2\u00f8\u00fa\5(\25\2\u00f9\u00f4\3\2\2\2\u00f9")
        buf.write("\u00f6\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\'\3\2\2\2\u00fb")
        buf.write("\u00fc\b\25\1\2\u00fc\u00fd\5*\26\2\u00fd\u0103\3\2\2")
        buf.write("\2\u00fe\u00ff\f\4\2\2\u00ff\u0100\t\2\2\2\u0100\u0102")
        buf.write("\5*\26\2\u0101\u00fe\3\2\2\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104)\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u0107\b\26\1\2\u0107\u0108\5,\27")
        buf.write("\2\u0108\u010e\3\2\2\2\u0109\u010a\f\4\2\2\u010a\u010b")
        buf.write("\t\3\2\2\u010b\u010d\5,\27\2\u010c\u0109\3\2\2\2\u010d")
        buf.write("\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f+\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\b\27\1")
        buf.write("\2\u0112\u0113\5.\30\2\u0113\u0119\3\2\2\2\u0114\u0115")
        buf.write("\f\4\2\2\u0115\u0116\t\4\2\2\u0116\u0118\5.\30\2\u0117")
        buf.write("\u0114\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u0119\u011a\3\2\2\2\u011a-\3\2\2\2\u011b\u0119\3\2\2")
        buf.write("\2\u011c\u011d\5\60\31\2\u011d\u011e\7\'\2\2\u011e\u011f")
        buf.write("\5\60\31\2\u011f\u0122\3\2\2\2\u0120\u0122\5\60\31\2\u0121")
        buf.write("\u011c\3\2\2\2\u0121\u0120\3\2\2\2\u0122/\3\2\2\2\u0123")
        buf.write("\u0124\5\62\32\2\u0124\u0125\7(\2\2\u0125\u0126\5\62\32")
        buf.write("\2\u0126\u0129\3\2\2\2\u0127\u0129\5\62\32\2\u0128\u0123")
        buf.write("\3\2\2\2\u0128\u0127\3\2\2\2\u0129\61\3\2\2\2\u012a\u012e")
        buf.write("\5\64\33\2\u012b\u012e\5\66\34\2\u012c\u012e\58\35\2\u012d")
        buf.write("\u012a\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012c\3\2\2\2")
        buf.write("\u012e\63\3\2\2\2\u012f\u0130\t\5\2\2\u0130\65\3\2\2\2")
        buf.write("\u0131\u0132\7=\2\2\u0132\67\3\2\2\2\u0133\u0134\7=\2")
        buf.write("\2\u0134\u0136\7)\2\2\u0135\u0137\5:\36\2\u0136\u0135")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0139\7*\2\2\u01399\3\2\2\2\u013a\u013b\5<\37\2\u013b")
        buf.write("\u013c\7\31\2\2\u013c\u013d\5:\36\2\u013d\u0140\3\2\2")
        buf.write("\2\u013e\u0140\5<\37\2\u013f\u013a\3\2\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140;\3\2\2\2\u0141\u0142\5 \21\2\u0142=\3\2")
        buf.write("\2\2\u0143\u0148\5@!\2\u0144\u0148\5B\"\2\u0145\u0148")
        buf.write("\5D#\2\u0146\u0148\5F$\2\u0147\u0143\3\2\2\2\u0147\u0144")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("?\3\2\2\2\u0149\u014a\7\4\2\2\u014a\u014b\7)\2\2\u014b")
        buf.write("\u014c\7*\2\2\u014cA\3\2\2\2\u014d\u014e\7\5\2\2\u014e")
        buf.write("\u014f\7)\2\2\u014f\u0150\7*\2\2\u0150C\3\2\2\2\u0151")
        buf.write("\u0152\7\6\2\2\u0152\u0153\7)\2\2\u0153\u0154\7*\2\2\u0154")
        buf.write("E\3\2\2\2\u0155\u0156\7\7\2\2\u0156\u0157\7)\2\2\u0157")
        buf.write("\u0158\7*\2\2\u0158G\3\2\2\2\u0159\u015a\5J&\2\u015a\u015b")
        buf.write("\7\33\2\2\u015b\u0170\3\2\2\2\u015c\u0170\5N(\2\u015d")
        buf.write("\u0170\5P)\2\u015e\u0170\5R*\2\u015f\u0160\5T+\2\u0160")
        buf.write("\u0161\7\33\2\2\u0161\u0170\3\2\2\2\u0162\u0163\5V,\2")
        buf.write("\u0163\u0164\7\33\2\2\u0164\u0170\3\2\2\2\u0165\u0166")
        buf.write("\5X-\2\u0166\u0167\7\33\2\2\u0167\u0170\3\2\2\2\u0168")
        buf.write("\u0169\5Z.\2\u0169\u016a\7\33\2\2\u016a\u0170\3\2\2\2")
        buf.write("\u016b\u016c\5\\/\2\u016c\u016d\7\33\2\2\u016d\u0170\3")
        buf.write("\2\2\2\u016e\u0170\5b\62\2\u016f\u0159\3\2\2\2\u016f\u015c")
        buf.write("\3\2\2\2\u016f\u015d\3\2\2\2\u016f\u015e\3\2\2\2\u016f")
        buf.write("\u015f\3\2\2\2\u016f\u0162\3\2\2\2\u016f\u0165\3\2\2\2")
        buf.write("\u016f\u0168\3\2\2\2\u016f\u016b\3\2\2\2\u016f\u016e\3")
        buf.write("\2\2\2\u0170I\3\2\2\2\u0171\u0172\5L\'\2\u0172\u0173\7")
        buf.write("\34\2\2\u0173\u0174\5 \21\2\u0174K\3\2\2\2\u0175\u0178")
        buf.write("\7=\2\2\u0176\u0178\5\"\22\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178M\3\2\2\2\u0179\u017a\7\b\2\2\u017a")
        buf.write("\u017b\7)\2\2\u017b\u017c\5 \21\2\u017c\u017d\7*\2\2\u017d")
        buf.write("\u0180\5H%\2\u017e\u017f\7\t\2\2\u017f\u0181\5H%\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181O\3\2\2\2\u0182")
        buf.write("\u0183\7\n\2\2\u0183\u0184\7)\2\2\u0184\u0185\7=\2\2\u0185")
        buf.write("\u0186\7\34\2\2\u0186\u0187\5 \21\2\u0187\u0188\7\31\2")
        buf.write("\2\u0188\u0189\5 \21\2\u0189\u018a\7\31\2\2\u018a\u018b")
        buf.write("\5 \21\2\u018b\u018c\7*\2\2\u018c\u018d\5H%\2\u018dQ\3")
        buf.write("\2\2\2\u018e\u018f\7\13\2\2\u018f\u0190\7)\2\2\u0190\u0191")
        buf.write("\5 \21\2\u0191\u0192\7*\2\2\u0192\u0193\5H%\2\u0193S\3")
        buf.write("\2\2\2\u0194\u0195\7\f\2\2\u0195\u0196\5^\60\2\u0196\u0197")
        buf.write("\7\13\2\2\u0197\u0198\7)\2\2\u0198\u0199\5 \21\2\u0199")
        buf.write("\u019a\7*\2\2\u019aU\3\2\2\2\u019b\u019c\7\r\2\2\u019c")
        buf.write("W\3\2\2\2\u019d\u019e\7\16\2\2\u019eY\3\2\2\2\u019f\u01a0")
        buf.write("\7\17\2\2\u01a0\u01a1\5 \21\2\u01a1[\3\2\2\2\u01a2\u01a3")
        buf.write("\58\35\2\u01a3]\3\2\2\2\u01a4\u01a6\7-\2\2\u01a5\u01a7")
        buf.write("\5`\61\2\u01a6\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a9\7.\2\2\u01a9_\3\2\2\2\u01aa")
        buf.write("\u01ad\5H%\2\u01ab\u01ad\5\b\5\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\5`\61\2")
        buf.write("\u01af\u01b5\3\2\2\2\u01b0\u01b3\5H%\2\u01b1\u01b3\5\b")
        buf.write("\5\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b5")
        buf.write("\3\2\2\2\u01b4\u01ac\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("a\3\2\2\2\u01b6\u01bd\5d\63\2\u01b7\u01bd\5f\64\2\u01b8")
        buf.write("\u01bd\5h\65\2\u01b9\u01bd\5j\66\2\u01ba\u01bd\5l\67\2")
        buf.write("\u01bb\u01bd\5n8\2\u01bc\u01b6\3\2\2\2\u01bc\u01b7\3\2")
        buf.write("\2\2\u01bc\u01b8\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("\u01bf\7\33\2\2\u01bfc\3\2\2\2\u01c0\u01c1\7\20\2\2\u01c1")
        buf.write("\u01c2\7)\2\2\u01c2\u01c3\t\6\2\2\u01c3\u01c4\7*\2\2\u01c4")
        buf.write("e\3\2\2\2\u01c5\u01c6\7\21\2\2\u01c6\u01c7\7)\2\2\u01c7")
        buf.write("\u01c8\t\7\2\2\u01c8\u01c9\7*\2\2\u01c9g\3\2\2\2\u01ca")
        buf.write("\u01cb\7\22\2\2\u01cb\u01cc\7)\2\2\u01cc\u01cd\t\b\2\2")
        buf.write("\u01cd\u01ce\7*\2\2\u01cei\3\2\2\2\u01cf\u01d0\7\23\2")
        buf.write("\2\u01d0\u01d1\7)\2\2\u01d1\u01d2\t\t\2\2\u01d2\u01d3")
        buf.write("\7*\2\2\u01d3k\3\2\2\2\u01d4\u01d5\7\24\2\2\u01d5\u01d6")
        buf.write("\7)\2\2\u01d6\u01d7\5\22\n\2\u01d7\u01d8\7*\2\2\u01d8")
        buf.write("m\3\2\2\2\u01d9\u01da\7\25\2\2\u01da\u01db\7)\2\2\u01db")
        buf.write("\u01dc\7*\2\2\u01dco\3\2\2\2\u01dd\u01de\t\n\2\2\u01de")
        buf.write("q\3\2\2\2\u01df\u01e0\7-\2\2\u01e0\u01e1\5\22\n\2\u01e1")
        buf.write("\u01e2\7.\2\2\u01e2s\3\2\2\2$u}\u0081\u0086\u009a\u00a9")
        buf.write("\u00b0\u00bb\u00c0\u00c7\u00ce\u00d1\u00d4\u00dc\u00eb")
        buf.write("\u00f2\u00f9\u0103\u010e\u0119\u0121\u0128\u012d\u0136")
        buf.write("\u013f\u0147\u016f\u0177\u0180\u01a6\u01ac\u01b2\u01b4")
        buf.write("\u01bc")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'of'", "'readInteger'", "'readFloat'", 
                     "'readBoolean'", "'readString'", "'if'", "'else'", 
                     "'for'", "'while'", "'do'", "'break'", "'continue'", 
                     "'return'", "'printInteger'", "'writeFloat'", "'printBoolean'", 
                     "'printString'", "'super'", "'preventDefault'", "'function'", 
                     "'inherit'", "'out'", "','", "':'", "';'", "'='", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "<INVALID>", "'::'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'{}'", "'boolean'", "'integer'", 
                     "'float'", "'string'", "'void'", "'auto'", "'array'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FUNCKEYW", "INHERIT", "OUT", "COMMA", "COLON", "SEMICOLON", 
                      "EQUAL", "OPENCMT", "LINECMT", "PLUSOP", "MINUSOP", 
                      "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NEGATEOP", 
                      "CONJUNCOP", "DISJUNCOP", "RELATIONALOP", "STRINGCONCAT", 
                      "LB", "RB", "LSQB", "RSQB", "LCB", "RCB", "CB", "BOOLTYPE", 
                      "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
                      "AUTOTYPE", "ARRAYTYPE", "ARRAY", "INTLIT", "FLOATLIT", 
                      "BOOLEANLIT", "DOUBLEQUOTE", "STRINGLIT", "ID", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_shortvardecl = 4
    RULE_fulvardecl = 5
    RULE_arraydecl = 6
    RULE_idlist = 7
    RULE_exprlist = 8
    RULE_funcdecl = 9
    RULE_funcproto = 10
    RULE_funcbody = 11
    RULE_returntype = 12
    RULE_paralistdecl = 13
    RULE_paradecl = 14
    RULE_expr = 15
    RULE_indexop = 16
    RULE_sign = 17
    RULE_logical_negate = 18
    RULE_multiplying = 19
    RULE_adding = 20
    RULE_logical_and_or = 21
    RULE_relational = 22
    RULE_string = 23
    RULE_operand = 24
    RULE_const = 25
    RULE_var = 26
    RULE_funccall = 27
    RULE_arglist = 28
    RULE_arg = 29
    RULE_specialepxr = 30
    RULE_readint = 31
    RULE_readfloat = 32
    RULE_readbool = 33
    RULE_readstring = 34
    RULE_stmt = 35
    RULE_assignstmt = 36
    RULE_lhs = 37
    RULE_ifstmt = 38
    RULE_forstmt = 39
    RULE_whilestmt = 40
    RULE_dowhilestmt = 41
    RULE_breakstmt = 42
    RULE_continuestmt = 43
    RULE_returnstmt = 44
    RULE_callstmt = 45
    RULE_blockstmt = 46
    RULE_blockBody = 47
    RULE_specialstmt = 48
    RULE_printint = 49
    RULE_writefloat = 50
    RULE_printbool = 51
    RULE_printstring = 52
    RULE_superfunc = 53
    RULE_preventdef = 54
    RULE_vartype = 55
    RULE_array = 56

    ruleNames =  [ "program", "decls", "decl", "vardecl", "shortvardecl", 
                   "fulvardecl", "arraydecl", "idlist", "exprlist", "funcdecl", 
                   "funcproto", "funcbody", "returntype", "paralistdecl", 
                   "paradecl", "expr", "indexop", "sign", "logical_negate", 
                   "multiplying", "adding", "logical_and_or", "relational", 
                   "string", "operand", "const", "var", "funccall", "arglist", 
                   "arg", "specialepxr", "readint", "readfloat", "readbool", 
                   "readstring", "stmt", "assignstmt", "lhs", "ifstmt", 
                   "forstmt", "whilestmt", "dowhilestmt", "breakstmt", "continuestmt", 
                   "returnstmt", "callstmt", "blockstmt", "blockBody", "specialstmt", 
                   "printint", "writefloat", "printbool", "printstring", 
                   "superfunc", "preventdef", "vartype", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    FUNCKEYW=20
    INHERIT=21
    OUT=22
    COMMA=23
    COLON=24
    SEMICOLON=25
    EQUAL=26
    OPENCMT=27
    LINECMT=28
    PLUSOP=29
    MINUSOP=30
    MULTIPLYOP=31
    DIVIDEOP=32
    MODULOOP=33
    NEGATEOP=34
    CONJUNCOP=35
    DISJUNCOP=36
    RELATIONALOP=37
    STRINGCONCAT=38
    LB=39
    RB=40
    LSQB=41
    RSQB=42
    LCB=43
    RCB=44
    CB=45
    BOOLTYPE=46
    INTTYPE=47
    FLOATTYPE=48
    STRINGTYPE=49
    VOIDTYPE=50
    AUTOTYPE=51
    ARRAYTYPE=52
    ARRAY=53
    INTLIT=54
    FLOATLIT=55
    BOOLEANLIT=56
    DOUBLEQUOTE=57
    STRINGLIT=58
    ID=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ID:
                self.state = 114
                self.decls()


            self.state = 117
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.decl()
                self.state = 120
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def shortvardecl(self):
            return self.getTypedRuleContext(MT22Parser.ShortvardeclContext,0)


        def fulvardecl(self):
            return self.getTypedRuleContext(MT22Parser.FulvardeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MT22Parser.ArraydeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 129
                self.shortvardecl()
                pass

            elif la_ == 2:
                self.state = 130
                self.fulvardecl()
                pass

            elif la_ == 3:
                self.state = 131
                self.arraydecl()
                pass


            self.state = 134
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_shortvardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortvardecl" ):
                return visitor.visitShortvardecl(self)
            else:
                return visitor.visitChildren(self)




    def shortvardecl(self):

        localctx = MT22Parser.ShortvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shortvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.idlist()
            self.state = 137
            self.match(MT22Parser.COLON)
            self.state = 138
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FulvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def var(self):
            return self.getTypedRuleContext(MT22Parser.VarContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def fulvardecl(self):
            return self.getTypedRuleContext(MT22Parser.FulvardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_fulvardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFulvardecl" ):
                return visitor.visitFulvardecl(self)
            else:
                return visitor.visitChildren(self)




    def fulvardecl(self):

        localctx = MT22Parser.FulvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fulvardecl)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(MT22Parser.ID)
                self.state = 141
                self.match(MT22Parser.COLON)
                self.state = 142
                self.vartype()
                self.state = 143
                self.match(MT22Parser.EQUAL)
                self.state = 144
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.var()
                self.state = 147
                self.match(MT22Parser.COMMA)
                self.state = 148
                self.fulvardecl()
                self.state = 149
                self.match(MT22Parser.COMMA)
                self.state = 150
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def ARRAYTYPE(self):
            return self.getToken(MT22Parser.ARRAYTYPE, 0)

        def LSQB(self):
            return self.getToken(MT22Parser.LSQB, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def RSQB(self):
            return self.getToken(MT22Parser.RSQB, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MT22Parser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.idlist()
            self.state = 155
            self.match(MT22Parser.COLON)
            self.state = 156
            self.match(MT22Parser.ARRAYTYPE)
            self.state = 157
            self.match(MT22Parser.LSQB)
            self.state = 158
            self.match(MT22Parser.INTLIT)
            self.state = 159
            self.match(MT22Parser.RSQB)
            self.state = 160
            self.match(MT22Parser.T__0)
            self.state = 161
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(MT22Parser.ID)
                self.state = 164
                self.match(MT22Parser.COMMA)
                self.state = 165
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprlist)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.expr()
                self.state = 170
                self.match(MT22Parser.COMMA)
                self.state = 171
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcproto(self):
            return self.getTypedRuleContext(MT22Parser.FuncprotoContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MT22Parser.FuncbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.funcproto()
            self.state = 177
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncprotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCKEYW(self):
            return self.getToken(MT22Parser.FUNCKEYW, 0)

        def returntype(self):
            return self.getTypedRuleContext(MT22Parser.ReturntypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def paralistdecl(self):
            return self.getTypedRuleContext(MT22Parser.ParalistdeclContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcproto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncproto" ):
                return visitor.visitFuncproto(self)
            else:
                return visitor.visitChildren(self)




    def funcproto(self):

        localctx = MT22Parser.FuncprotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcproto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MT22Parser.ID)
            self.state = 180
            self.match(MT22Parser.COLON)
            self.state = 181
            self.match(MT22Parser.FUNCKEYW)
            self.state = 182
            self.returntype()
            self.state = 183
            self.match(MT22Parser.LB)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INHERIT) | (1 << MT22Parser.OUT) | (1 << MT22Parser.ID))) != 0):
                self.state = 184
                self.paralistdecl()


            self.state = 187
            self.match(MT22Parser.RB)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 188
                self.match(MT22Parser.INHERIT)
                self.state = 189
                self.match(MT22Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = MT22Parser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MT22Parser.VOIDTYPE, 0)

        def AUTOTYPE(self):
            return self.getToken(MT22Parser.AUTOTYPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MT22Parser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returntype)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLTYPE, MT22Parser.INTTYPE, MT22Parser.FLOATTYPE, MT22Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.vartype()
                pass
            elif token in [MT22Parser.VOIDTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(MT22Parser.VOIDTYPE)
                pass
            elif token in [MT22Parser.AUTOTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(MT22Parser.AUTOTYPE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paradecl(self):
            return self.getTypedRuleContext(MT22Parser.ParadeclContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def paralistdecl(self):
            return self.getTypedRuleContext(MT22Parser.ParalistdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paralistdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalistdecl" ):
                return visitor.visitParalistdecl(self)
            else:
                return visitor.visitChildren(self)




    def paralistdecl(self):

        localctx = MT22Parser.ParalistdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paralistdecl)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.paradecl()
                self.state = 200
                self.match(MT22Parser.COMMA)
                self.state = 201
                self.paralistdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.paradecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paradecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParadecl" ):
                return visitor.visitParadecl(self)
            else:
                return visitor.visitChildren(self)




    def paradecl(self):

        localctx = MT22Parser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paradecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 206
                self.match(MT22Parser.INHERIT)


            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 209
                self.match(MT22Parser.OUT)


            self.state = 212
            self.match(MT22Parser.ID)
            self.state = 213
            self.match(MT22Parser.COLON)
            self.state = 214
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def specialepxr(self):
            return self.getTypedRuleContext(MT22Parser.SpecialepxrContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUSOP, MT22Parser.NEGATEOP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.indexop()
                pass
            elif token in [MT22Parser.T__1, MT22Parser.T__2, MT22Parser.T__3, MT22Parser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.specialepxr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LSQB(self):
            return self.getToken(MT22Parser.LSQB, 0)

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def sign(self):
            return self.getTypedRuleContext(MT22Parser.SignContext,0)


        def RSQB(self):
            return self.getToken(MT22Parser.RSQB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = MT22Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_indexop)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(MT22Parser.ID)
                self.state = 221
                self.match(MT22Parser.LSQB)
                self.state = 222
                self.indexop()
                self.state = 223
                self.match(MT22Parser.COMMA)
                self.state = 224
                self.sign()
                self.state = 225
                self.match(MT22Parser.RSQB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(MT22Parser.ID)
                self.state = 228
                self.match(MT22Parser.LSQB)
                self.state = 229
                self.sign()
                self.state = 230
                self.match(MT22Parser.RSQB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.sign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def sign(self):
            return self.getTypedRuleContext(MT22Parser.SignContext,0)


        def logical_negate(self):
            return self.getTypedRuleContext(MT22Parser.Logical_negateContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = MT22Parser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sign)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MT22Parser.MINUSOP)
                self.state = 236
                self.sign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(MT22Parser.MINUSOP)
                self.state = 238
                self.logical_negate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.logical_negate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_negateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATEOP(self):
            return self.getToken(MT22Parser.NEGATEOP, 0)

        def logical_negate(self):
            return self.getTypedRuleContext(MT22Parser.Logical_negateContext,0)


        def multiplying(self):
            return self.getTypedRuleContext(MT22Parser.MultiplyingContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_logical_negate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_negate" ):
                return visitor.visitLogical_negate(self)
            else:
                return visitor.visitChildren(self)




    def logical_negate(self):

        localctx = MT22Parser.Logical_negateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logical_negate)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(MT22Parser.NEGATEOP)
                self.state = 243
                self.logical_negate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(MT22Parser.NEGATEOP)
                self.state = 245
                self.multiplying(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.multiplying(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding(self):
            return self.getTypedRuleContext(MT22Parser.AddingContext,0)


        def multiplying(self):
            return self.getTypedRuleContext(MT22Parser.MultiplyingContext,0)


        def MULTIPLYOP(self):
            return self.getToken(MT22Parser.MULTIPLYOP, 0)

        def DIVIDEOP(self):
            return self.getToken(MT22Parser.DIVIDEOP, 0)

        def MODULOOP(self):
            return self.getToken(MT22Parser.MODULOOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)



    def multiplying(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.MultiplyingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_multiplying, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.MultiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying)
                    self.state = 252
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 253
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULTIPLYOP) | (1 << MT22Parser.DIVIDEOP) | (1 << MT22Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 254
                    self.adding(0) 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and_or(self):
            return self.getTypedRuleContext(MT22Parser.Logical_and_orContext,0)


        def adding(self):
            return self.getTypedRuleContext(MT22Parser.AddingContext,0)


        def PLUSOP(self):
            return self.getToken(MT22Parser.PLUSOP, 0)

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)



    def adding(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.AddingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_adding, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.logical_and_or(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.AddingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding)
                    self.state = 263
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 264
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUSOP or _la==MT22Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 265
                    self.logical_and_or(0) 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_and_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self):
            return self.getTypedRuleContext(MT22Parser.RelationalContext,0)


        def logical_and_or(self):
            return self.getTypedRuleContext(MT22Parser.Logical_and_orContext,0)


        def CONJUNCOP(self):
            return self.getToken(MT22Parser.CONJUNCOP, 0)

        def DISJUNCOP(self):
            return self.getToken(MT22Parser.DISJUNCOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logical_and_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and_or" ):
                return visitor.visitLogical_and_or(self)
            else:
                return visitor.visitChildren(self)



    def logical_and_or(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logical_and_orContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_logical_and_or, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.relational()
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_and_orContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_and_or)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.CONJUNCOP or _la==MT22Parser.DISJUNCOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 276
                    self.relational() 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StringContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StringContext,i)


        def RELATIONALOP(self):
            return self.getToken(MT22Parser.RELATIONALOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = MT22Parser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_relational)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.string()
                self.state = 283
                self.match(MT22Parser.RELATIONALOP)
                self.state = 284
                self.string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.OperandContext)
            else:
                return self.getTypedRuleContext(MT22Parser.OperandContext,i)


        def STRINGCONCAT(self):
            return self.getToken(MT22Parser.STRINGCONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = MT22Parser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_string)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.operand()
                self.state = 290
                self.match(MT22Parser.STRINGCONCAT)
                self.state = 291
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const(self):
            return self.getTypedRuleContext(MT22Parser.ConstContext,0)


        def var(self):
            return self.getTypedRuleContext(MT22Parser.VarContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operand)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.const()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = MT22Parser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MT22Parser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def arglist(self):
            return self.getTypedRuleContext(MT22Parser.ArglistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MT22Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MT22Parser.ID)
            self.state = 306
            self.match(MT22Parser.LB)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.T__1) | (1 << MT22Parser.T__2) | (1 << MT22Parser.T__3) | (1 << MT22Parser.T__4) | (1 << MT22Parser.MINUSOP) | (1 << MT22Parser.NEGATEOP) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 307
                self.arglist()


            self.state = 310
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(MT22Parser.ArgContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def arglist(self):
            return self.getTypedRuleContext(MT22Parser.ArglistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = MT22Parser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arglist)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.arg()
                self.state = 313
                self.match(MT22Parser.COMMA)
                self.state = 314
                self.arglist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = MT22Parser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialepxrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readint(self):
            return self.getTypedRuleContext(MT22Parser.ReadintContext,0)


        def readfloat(self):
            return self.getTypedRuleContext(MT22Parser.ReadfloatContext,0)


        def readbool(self):
            return self.getTypedRuleContext(MT22Parser.ReadboolContext,0)


        def readstring(self):
            return self.getTypedRuleContext(MT22Parser.ReadstringContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_specialepxr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecialepxr" ):
                return visitor.visitSpecialepxr(self)
            else:
                return visitor.visitChildren(self)




    def specialepxr(self):

        localctx = MT22Parser.SpecialepxrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_specialepxr)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.readint()
                pass
            elif token in [MT22Parser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.readfloat()
                pass
            elif token in [MT22Parser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                self.readbool()
                pass
            elif token in [MT22Parser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.readstring()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readint

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadint" ):
                return visitor.visitReadint(self)
            else:
                return visitor.visitChildren(self)




    def readint(self):

        localctx = MT22Parser.ReadintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_readint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MT22Parser.T__1)
            self.state = 328
            self.match(MT22Parser.LB)
            self.state = 329
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadfloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readfloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadfloat" ):
                return visitor.visitReadfloat(self)
            else:
                return visitor.visitChildren(self)




    def readfloat(self):

        localctx = MT22Parser.ReadfloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_readfloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MT22Parser.T__2)
            self.state = 332
            self.match(MT22Parser.LB)
            self.state = 333
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readbool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadbool" ):
                return visitor.visitReadbool(self)
            else:
                return visitor.visitChildren(self)




    def readbool(self):

        localctx = MT22Parser.ReadboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_readbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MT22Parser.T__3)
            self.state = 336
            self.match(MT22Parser.LB)
            self.state = 337
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadstringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readstring

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadstring" ):
                return visitor.visitReadstring(self)
            else:
                return visitor.visitChildren(self)




    def readstring(self):

        localctx = MT22Parser.ReadstringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_readstring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(MT22Parser.T__4)
            self.state = 340
            self.match(MT22Parser.LB)
            self.state = 341
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def specialstmt(self):
            return self.getTypedRuleContext(MT22Parser.SpecialstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.assignstmt()
                self.state = 344
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 349
                self.dowhilestmt()
                self.state = 350
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 352
                self.breakstmt()
                self.state = 353
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 355
                self.continuestmt()
                self.state = 356
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.returnstmt()
                self.state = 359
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 361
                self.callstmt()
                self.state = 362
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 364
                self.specialstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.lhs()
            self.state = 368
            self.match(MT22Parser.EQUAL)
            self.state = 369
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_lhs)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MT22Parser.T__5)
            self.state = 376
            self.match(MT22Parser.LB)
            self.state = 377
            self.expr()
            self.state = 378
            self.match(MT22Parser.RB)
            self.state = 379
            self.stmt()
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 380
                self.match(MT22Parser.T__6)
                self.state = 381
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MT22Parser.T__7)
            self.state = 385
            self.match(MT22Parser.LB)
            self.state = 386
            self.match(MT22Parser.ID)
            self.state = 387
            self.match(MT22Parser.EQUAL)
            self.state = 388
            self.expr()
            self.state = 389
            self.match(MT22Parser.COMMA)
            self.state = 390
            self.expr()
            self.state = 391
            self.match(MT22Parser.COMMA)
            self.state = 392
            self.expr()
            self.state = 393
            self.match(MT22Parser.RB)
            self.state = 394
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(MT22Parser.T__8)
            self.state = 397
            self.match(MT22Parser.LB)
            self.state = 398
            self.expr()
            self.state = 399
            self.match(MT22Parser.RB)
            self.state = 400
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MT22Parser.T__9)
            self.state = 403
            self.blockstmt()
            self.state = 404
            self.match(MT22Parser.T__8)
            self.state = 405
            self.match(MT22Parser.LB)
            self.state = 406
            self.expr()
            self.state = 407
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MT22Parser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(MT22Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(MT22Parser.T__12)
            self.state = 414
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.funccall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def blockBody(self):
            return self.getTypedRuleContext(MT22Parser.BlockBodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MT22Parser.LCB)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.T__5) | (1 << MT22Parser.T__7) | (1 << MT22Parser.T__8) | (1 << MT22Parser.T__9) | (1 << MT22Parser.T__10) | (1 << MT22Parser.T__11) | (1 << MT22Parser.T__12) | (1 << MT22Parser.T__13) | (1 << MT22Parser.T__14) | (1 << MT22Parser.T__15) | (1 << MT22Parser.T__16) | (1 << MT22Parser.T__17) | (1 << MT22Parser.T__18) | (1 << MT22Parser.MINUSOP) | (1 << MT22Parser.NEGATEOP) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 419
                self.blockBody()


            self.state = 422
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockBody(self):
            return self.getTypedRuleContext(MT22Parser.BlockBodyContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockBody" ):
                return visitor.visitBlockBody(self)
            else:
                return visitor.visitChildren(self)




    def blockBody(self):

        localctx = MT22Parser.BlockBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_blockBody)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 424
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 425
                    self.vardecl()
                    pass


                self.state = 428
                self.blockBody()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 430
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 431
                    self.vardecl()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def printint(self):
            return self.getTypedRuleContext(MT22Parser.PrintintContext,0)


        def writefloat(self):
            return self.getTypedRuleContext(MT22Parser.WritefloatContext,0)


        def printbool(self):
            return self.getTypedRuleContext(MT22Parser.PrintboolContext,0)


        def printstring(self):
            return self.getTypedRuleContext(MT22Parser.PrintstringContext,0)


        def superfunc(self):
            return self.getTypedRuleContext(MT22Parser.SuperfuncContext,0)


        def preventdef(self):
            return self.getTypedRuleContext(MT22Parser.PreventdefContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_specialstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecialstmt" ):
                return visitor.visitSpecialstmt(self)
            else:
                return visitor.visitChildren(self)




    def specialstmt(self):

        localctx = MT22Parser.SpecialstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_specialstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__13]:
                self.state = 436
                self.printint()
                pass
            elif token in [MT22Parser.T__14]:
                self.state = 437
                self.writefloat()
                pass
            elif token in [MT22Parser.T__15]:
                self.state = 438
                self.printbool()
                pass
            elif token in [MT22Parser.T__16]:
                self.state = 439
                self.printstring()
                pass
            elif token in [MT22Parser.T__17]:
                self.state = 440
                self.superfunc()
                pass
            elif token in [MT22Parser.T__18]:
                self.state = 441
                self.preventdef()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 444
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printint

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintint" ):
                return visitor.visitPrintint(self)
            else:
                return visitor.visitChildren(self)




    def printint(self):

        localctx = MT22Parser.PrintintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_printint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MT22Parser.T__13)
            self.state = 447
            self.match(MT22Parser.LB)
            self.state = 448
            _la = self._input.LA(1)
            if not(_la==MT22Parser.INTLIT or _la==MT22Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 449
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WritefloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_writefloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWritefloat" ):
                return visitor.visitWritefloat(self)
            else:
                return visitor.visitChildren(self)




    def writefloat(self):

        localctx = MT22Parser.WritefloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_writefloat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MT22Parser.T__14)
            self.state = 452
            self.match(MT22Parser.LB)
            self.state = 453
            _la = self._input.LA(1)
            if not(_la==MT22Parser.FLOATLIT or _la==MT22Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 454
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def BOOLEANLIT(self):
            return self.getToken(MT22Parser.BOOLEANLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printbool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintbool" ):
                return visitor.visitPrintbool(self)
            else:
                return visitor.visitChildren(self)




    def printbool(self):

        localctx = MT22Parser.PrintboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_printbool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MT22Parser.T__15)
            self.state = 457
            self.match(MT22Parser.LB)
            self.state = 458
            _la = self._input.LA(1)
            if not(_la==MT22Parser.BOOLEANLIT or _la==MT22Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 459
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printstring

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintstring" ):
                return visitor.visitPrintstring(self)
            else:
                return visitor.visitChildren(self)




    def printstring(self):

        localctx = MT22Parser.PrintstringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_printstring)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(MT22Parser.T__16)
            self.state = 462
            self.match(MT22Parser.LB)
            self.state = 463
            _la = self._input.LA(1)
            if not(_la==MT22Parser.STRINGLIT or _la==MT22Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 464
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_superfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperfunc" ):
                return visitor.visitSuperfunc(self)
            else:
                return visitor.visitChildren(self)




    def superfunc(self):

        localctx = MT22Parser.SuperfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_superfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(MT22Parser.T__17)
            self.state = 467
            self.match(MT22Parser.LB)
            self.state = 468
            self.exprlist()
            self.state = 469
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreventdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_preventdef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreventdef" ):
                return visitor.visitPreventdef(self)
            else:
                return visitor.visitChildren(self)




    def preventdef(self):

        localctx = MT22Parser.PreventdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_preventdef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MT22Parser.T__18)
            self.state = 472
            self.match(MT22Parser.LB)
            self.state = 473
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLTYPE(self):
            return self.getToken(MT22Parser.BOOLTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MT22Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MT22Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MT22Parser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLTYPE) | (1 << MT22Parser.INTTYPE) | (1 << MT22Parser.FLOATTYPE) | (1 << MT22Parser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MT22Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(MT22Parser.LCB)
            self.state = 478
            self.exprlist()
            self.state = 479
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.multiplying_sempred
        self._predicates[20] = self.adding_sempred
        self._predicates[21] = self.logical_and_or_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def multiplying_sempred(self, localctx:MultiplyingContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_sempred(self, localctx:AddingContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def logical_and_or_sempred(self, localctx:Logical_and_orContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




