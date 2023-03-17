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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\5\4r\n\4\3\5\3\5\5")
        buf.write("\5v\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u008a\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\5\n\u0098\n\n\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u009e\n\13\3\f\3\f\3\f\3\f\5\f\u00a4")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ab\n\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b6\n\17\3\17\3")
        buf.write("\17\3\17\5\17\u00bb\n\17\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00c3\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00ca\n")
        buf.write("\22\3\23\5\23\u00cd\n\23\3\23\5\23\u00d0\n\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00de\n\25\f\25\16\25\u00e1\13\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00e9\n\26\3\26\3\26\3\26\7\26\u00ee\n")
        buf.write("\26\f\26\16\26\u00f1\13\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u00f9\n\27\f\27\16\27\u00fc\13\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\7\30\u0104\n\30\f\30\16\30\u0107\13")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u010f\n\31\f\31")
        buf.write("\16\31\u0112\13\31\3\32\3\32\3\32\5\32\u0117\n\32\3\33")
        buf.write("\3\33\3\33\5\33\u011c\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u0124\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u012b")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\5!")
        buf.write("\u0138\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0141\n\"\3#\3")
        buf.write("#\3$\3$\5$\u0147\n$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0161\n%\3&\3")
        buf.write("&\3&\3&\3\'\3\'\5\'\u0169\n\'\3(\3(\3(\3(\3(\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\5)\u0177\n)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\5/\u0198\n/\3\60\3\60\3\61\3\61\5\61\u019e")
        buf.write("\n\61\3\61\3\61\3\62\3\62\5\62\u01a4\n\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01aa\n\62\5\62\u01ac\n\62\3\63\3\63\3\63")
        buf.write("\2\7(*,.\60\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\7\3\2")
        buf.write("\34\35\3\2\26\27\3\2\30\32\3\2-\60\3\2&)\2\u01ae\2f\3")
        buf.write("\2\2\2\4m\3\2\2\2\6q\3\2\2\2\bu\3\2\2\2\ny\3\2\2\2\f\u0089")
        buf.write("\3\2\2\2\16\u008b\3\2\2\2\20\u0092\3\2\2\2\22\u0097\3")
        buf.write("\2\2\2\24\u009d\3\2\2\2\26\u00a3\3\2\2\2\30\u00aa\3\2")
        buf.write("\2\2\32\u00ac\3\2\2\2\34\u00af\3\2\2\2\36\u00bc\3\2\2")
        buf.write("\2 \u00c2\3\2\2\2\"\u00c9\3\2\2\2$\u00cc\3\2\2\2&\u00d5")
        buf.write("\3\2\2\2(\u00d7\3\2\2\2*\u00e8\3\2\2\2,\u00f2\3\2\2\2")
        buf.write(".\u00fd\3\2\2\2\60\u0108\3\2\2\2\62\u0116\3\2\2\2\64\u011b")
        buf.write("\3\2\2\2\66\u0123\3\2\2\28\u012a\3\2\2\2:\u012c\3\2\2")
        buf.write("\2<\u0130\3\2\2\2>\u0132\3\2\2\2@\u0134\3\2\2\2B\u0140")
        buf.write("\3\2\2\2D\u0142\3\2\2\2F\u0144\3\2\2\2H\u0160\3\2\2\2")
        buf.write("J\u0162\3\2\2\2L\u0168\3\2\2\2N\u016a\3\2\2\2P\u016f\3")
        buf.write("\2\2\2R\u0178\3\2\2\2T\u0184\3\2\2\2V\u018a\3\2\2\2X\u0191")
        buf.write("\3\2\2\2Z\u0193\3\2\2\2\\\u0195\3\2\2\2^\u0199\3\2\2\2")
        buf.write("`\u019b\3\2\2\2b\u01ab\3\2\2\2d\u01ad\3\2\2\2fg\5\4\3")
        buf.write("\2gh\7\2\2\3h\3\3\2\2\2ij\5\6\4\2jk\5\4\3\2kn\3\2\2\2")
        buf.write("ln\5\6\4\2mi\3\2\2\2ml\3\2\2\2n\5\3\2\2\2or\5\b\5\2pr")
        buf.write("\5\32\16\2qo\3\2\2\2qp\3\2\2\2r\7\3\2\2\2sv\5\n\6\2tv")
        buf.write("\5\f\7\2us\3\2\2\2ut\3\2\2\2vw\3\2\2\2wx\7\21\2\2x\t\3")
        buf.write("\2\2\2yz\5\26\f\2z{\7\20\2\2{|\5\22\n\2|\13\3\2\2\2}~")
        buf.write("\7\61\2\2~\177\7\20\2\2\177\u0080\5\22\n\2\u0080\u0081")
        buf.write("\7\22\2\2\u0081\u0082\5&\24\2\u0082\u008a\3\2\2\2\u0083")
        buf.write("\u0084\7\61\2\2\u0084\u0085\7\17\2\2\u0085\u0086\5\f\7")
        buf.write("\2\u0086\u0087\7\17\2\2\u0087\u0088\5&\24\2\u0088\u008a")
        buf.write("\3\2\2\2\u0089}\3\2\2\2\u0089\u0083\3\2\2\2\u008a\r\3")
        buf.write("\2\2\2\u008b\u008c\7,\2\2\u008c\u008d\7\"\2\2\u008d\u008e")
        buf.write("\5\24\13\2\u008e\u008f\7#\2\2\u008f\u0090\7\3\2\2\u0090")
        buf.write("\u0091\5\20\t\2\u0091\17\3\2\2\2\u0092\u0093\5d\63\2\u0093")
        buf.write("\21\3\2\2\2\u0094\u0098\5d\63\2\u0095\u0098\7+\2\2\u0096")
        buf.write("\u0098\5\16\b\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2")
        buf.write("\2\u0097\u0096\3\2\2\2\u0098\23\3\2\2\2\u0099\u009a\7")
        buf.write("-\2\2\u009a\u009b\7\17\2\2\u009b\u009e\5\24\13\2\u009c")
        buf.write("\u009e\7-\2\2\u009d\u0099\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\25\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1\7\17")
        buf.write("\2\2\u00a1\u00a4\5\26\f\2\u00a2\u00a4\7\61\2\2\u00a3\u009f")
        buf.write("\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\27\3\2\2\2\u00a5\u00a6")
        buf.write("\5&\24\2\u00a6\u00a7\7\17\2\2\u00a7\u00a8\5\30\r\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00ab\5&\24\2\u00aa\u00a5\3\2\2\2")
        buf.write("\u00aa\u00a9\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00ad\5\34")
        buf.write("\17\2\u00ad\u00ae\5\36\20\2\u00ae\33\3\2\2\2\u00af\u00b0")
        buf.write("\7\61\2\2\u00b0\u00b1\7\20\2\2\u00b1\u00b2\7\f\2\2\u00b2")
        buf.write("\u00b3\5 \21\2\u00b3\u00b5\7 \2\2\u00b4\u00b6\5\"\22\2")
        buf.write("\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3")
        buf.write("\2\2\2\u00b7\u00ba\7!\2\2\u00b8\u00b9\7\r\2\2\u00b9\u00bb")
        buf.write("\7\61\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\35\3\2\2\2\u00bc\u00bd\5`\61\2\u00bd\37\3\2\2\2\u00be")
        buf.write("\u00c3\5d\63\2\u00bf\u00c3\7*\2\2\u00c0\u00c3\7+\2\2\u00c1")
        buf.write("\u00c3\5\16\b\2\u00c2\u00be\3\2\2\2\u00c2\u00bf\3\2\2")
        buf.write("\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3!\3\2")
        buf.write("\2\2\u00c4\u00c5\5$\23\2\u00c5\u00c6\7\17\2\2\u00c6\u00c7")
        buf.write("\5\"\22\2\u00c7\u00ca\3\2\2\2\u00c8\u00ca\5$\23\2\u00c9")
        buf.write("\u00c4\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca#\3\2\2\2\u00cb")
        buf.write("\u00cd\7\r\2\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00d0\7\16\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d2\7\61\2\2\u00d2\u00d3\7\20\2\2\u00d3\u00d4\5\22")
        buf.write("\n\2\u00d4%\3\2\2\2\u00d5\u00d6\5(\25\2\u00d6\'\3\2\2")
        buf.write("\2\u00d7\u00d8\b\25\1\2\u00d8\u00d9\5*\26\2\u00d9\u00df")
        buf.write("\3\2\2\2\u00da\u00db\f\4\2\2\u00db\u00dc\7\37\2\2\u00dc")
        buf.write("\u00de\5(\25\5\u00dd\u00da\3\2\2\2\u00de\u00e1\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0)\3\2\2")
        buf.write("\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\b\26\1\2\u00e3\u00e4")
        buf.write("\5,\27\2\u00e4\u00e5\7\36\2\2\u00e5\u00e6\5*\26\4\u00e6")
        buf.write("\u00e9\3\2\2\2\u00e7\u00e9\5,\27\2\u00e8\u00e2\3\2\2\2")
        buf.write("\u00e8\u00e7\3\2\2\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb\f")
        buf.write("\5\2\2\u00eb\u00ec\7\36\2\2\u00ec\u00ee\5,\27\2\u00ed")
        buf.write("\u00ea\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0+\3\2\2\2\u00f1\u00ef\3\2\2")
        buf.write("\2\u00f2\u00f3\b\27\1\2\u00f3\u00f4\5.\30\2\u00f4\u00fa")
        buf.write("\3\2\2\2\u00f5\u00f6\f\4\2\2\u00f6\u00f7\t\2\2\2\u00f7")
        buf.write("\u00f9\5.\30\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb-\3\2\2")
        buf.write("\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\b\30\1\2\u00fe\u00ff")
        buf.write("\5\60\31\2\u00ff\u0105\3\2\2\2\u0100\u0101\f\4\2\2\u0101")
        buf.write("\u0102\t\3\2\2\u0102\u0104\5\60\31\2\u0103\u0100\3\2\2")
        buf.write("\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106/\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109")
        buf.write("\b\31\1\2\u0109\u010a\5\62\32\2\u010a\u0110\3\2\2\2\u010b")
        buf.write("\u010c\f\4\2\2\u010c\u010d\t\4\2\2\u010d\u010f\5\62\32")
        buf.write("\2\u010e\u010b\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111\61\3\2\2\2\u0112\u0110")
        buf.write("\3\2\2\2\u0113\u0114\7\33\2\2\u0114\u0117\5\62\32\2\u0115")
        buf.write("\u0117\5\64\33\2\u0116\u0113\3\2\2\2\u0116\u0115\3\2\2")
        buf.write("\2\u0117\63\3\2\2\2\u0118\u0119\7\27\2\2\u0119\u011c\5")
        buf.write("\64\33\2\u011a\u011c\5\66\34\2\u011b\u0118\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\65\3\2\2\2\u011d\u011e\7\61\2\2\u011e")
        buf.write("\u011f\7\"\2\2\u011f\u0120\5\30\r\2\u0120\u0121\7#\2\2")
        buf.write("\u0121\u0124\3\2\2\2\u0122\u0124\58\35\2\u0123\u011d\3")
        buf.write("\2\2\2\u0123\u0122\3\2\2\2\u0124\67\3\2\2\2\u0125\u012b")
        buf.write("\5<\37\2\u0126\u012b\5> \2\u0127\u012b\5@!\2\u0128\u012b")
        buf.write("\5F$\2\u0129\u012b\5:\36\2\u012a\u0125\3\2\2\2\u012a\u0126")
        buf.write("\3\2\2\2\u012a\u0127\3\2\2\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b9\3\2\2\2\u012c\u012d\7 \2\2\u012d")
        buf.write("\u012e\5&\24\2\u012e\u012f\7!\2\2\u012f;\3\2\2\2\u0130")
        buf.write("\u0131\t\5\2\2\u0131=\3\2\2\2\u0132\u0133\7\61\2\2\u0133")
        buf.write("?\3\2\2\2\u0134\u0135\7\61\2\2\u0135\u0137\7 \2\2\u0136")
        buf.write("\u0138\5B\"\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013a\7!\2\2\u013aA\3\2\2\2")
        buf.write("\u013b\u013c\5D#\2\u013c\u013d\7\17\2\2\u013d\u013e\5")
        buf.write("B\"\2\u013e\u0141\3\2\2\2\u013f\u0141\5D#\2\u0140\u013b")
        buf.write("\3\2\2\2\u0140\u013f\3\2\2\2\u0141C\3\2\2\2\u0142\u0143")
        buf.write("\5&\24\2\u0143E\3\2\2\2\u0144\u0146\7$\2\2\u0145\u0147")
        buf.write("\5\30\r\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\u0149\7%\2\2\u0149G\3\2\2\2\u014a")
        buf.write("\u014b\5J&\2\u014b\u014c\7\21\2\2\u014c\u0161\3\2\2\2")
        buf.write("\u014d\u0161\5P)\2\u014e\u0161\5R*\2\u014f\u0161\5T+\2")
        buf.write("\u0150\u0151\5V,\2\u0151\u0152\7\21\2\2\u0152\u0161\3")
        buf.write("\2\2\2\u0153\u0154\5X-\2\u0154\u0155\7\21\2\2\u0155\u0161")
        buf.write("\3\2\2\2\u0156\u0157\5Z.\2\u0157\u0158\7\21\2\2\u0158")
        buf.write("\u0161\3\2\2\2\u0159\u015a\5\\/\2\u015a\u015b\7\21\2\2")
        buf.write("\u015b\u0161\3\2\2\2\u015c\u015d\5^\60\2\u015d\u015e\7")
        buf.write("\21\2\2\u015e\u0161\3\2\2\2\u015f\u0161\5`\61\2\u0160")
        buf.write("\u014a\3\2\2\2\u0160\u014d\3\2\2\2\u0160\u014e\3\2\2\2")
        buf.write("\u0160\u014f\3\2\2\2\u0160\u0150\3\2\2\2\u0160\u0153\3")
        buf.write("\2\2\2\u0160\u0156\3\2\2\2\u0160\u0159\3\2\2\2\u0160\u015c")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161I\3\2\2\2\u0162\u0163")
        buf.write("\5L\'\2\u0163\u0164\7\22\2\2\u0164\u0165\5&\24\2\u0165")
        buf.write("K\3\2\2\2\u0166\u0169\7\61\2\2\u0167\u0169\5N(\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169M\3\2\2\2\u016a")
        buf.write("\u016b\7\61\2\2\u016b\u016c\7\"\2\2\u016c\u016d\5\30\r")
        buf.write("\2\u016d\u016e\7#\2\2\u016eO\3\2\2\2\u016f\u0170\7\4\2")
        buf.write("\2\u0170\u0171\7 \2\2\u0171\u0172\5&\24\2\u0172\u0173")
        buf.write("\7!\2\2\u0173\u0176\5H%\2\u0174\u0175\7\5\2\2\u0175\u0177")
        buf.write("\5H%\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177Q")
        buf.write("\3\2\2\2\u0178\u0179\7\6\2\2\u0179\u017a\7 \2\2\u017a")
        buf.write("\u017b\7\61\2\2\u017b\u017c\7\22\2\2\u017c\u017d\5&\24")
        buf.write("\2\u017d\u017e\7\17\2\2\u017e\u017f\5&\24\2\u017f\u0180")
        buf.write("\7\17\2\2\u0180\u0181\5&\24\2\u0181\u0182\7!\2\2\u0182")
        buf.write("\u0183\5H%\2\u0183S\3\2\2\2\u0184\u0185\7\7\2\2\u0185")
        buf.write("\u0186\7 \2\2\u0186\u0187\5&\24\2\u0187\u0188\7!\2\2\u0188")
        buf.write("\u0189\5H%\2\u0189U\3\2\2\2\u018a\u018b\7\b\2\2\u018b")
        buf.write("\u018c\5H%\2\u018c\u018d\7\7\2\2\u018d\u018e\7 \2\2\u018e")
        buf.write("\u018f\5&\24\2\u018f\u0190\7!\2\2\u0190W\3\2\2\2\u0191")
        buf.write("\u0192\7\t\2\2\u0192Y\3\2\2\2\u0193\u0194\7\n\2\2\u0194")
        buf.write("[\3\2\2\2\u0195\u0197\7\13\2\2\u0196\u0198\5&\24\2\u0197")
        buf.write("\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198]\3\2\2\2\u0199")
        buf.write("\u019a\5@!\2\u019a_\3\2\2\2\u019b\u019d\7$\2\2\u019c\u019e")
        buf.write("\5b\62\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\7%\2\2\u01a0a\3\2\2\2\u01a1")
        buf.write("\u01a4\5H%\2\u01a2\u01a4\5\b\5\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\5b\62\2")
        buf.write("\u01a6\u01ac\3\2\2\2\u01a7\u01aa\5H%\2\u01a8\u01aa\5\b")
        buf.write("\5\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ac")
        buf.write("\3\2\2\2\u01ab\u01a3\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("c\3\2\2\2\u01ad\u01ae\t\6\2\2\u01aee\3\2\2\2%mqu\u0089")
        buf.write("\u0097\u009d\u00a3\u00aa\u00b5\u00ba\u00c2\u00c9\u00cc")
        buf.write("\u00cf\u00df\u00e8\u00ef\u00fa\u0105\u0110\u0116\u011b")
        buf.write("\u0123\u012a\u0137\u0140\u0146\u0160\u0168\u0176\u0197")
        buf.write("\u019d\u01a3\u01a9\u01ab")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'of'", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'break'", "'continue'", "'return'", "'function'", 
                     "'inherit'", "'out'", "','", "':'", "';'", "'='", "'.'", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "<INVALID>", "'::'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'boolean'", 
                     "'integer'", "'float'", "'string'", "'void'", "'auto'", 
                     "'array'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNCKEYW", "INHERIT", "OUT", 
                      "COMMA", "COLON", "SEMICOLON", "EQUAL", "DOT", "OPENCMT", 
                      "LINECMT", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                      "MODULOOP", "NEGATEOP", "CONJUNCOP", "DISJUNCOP", 
                      "RELATIONALOP", "STRINGCONCAT", "LB", "RB", "LSQB", 
                      "RSQB", "LCB", "RCB", "BOOLTYPE", "INTTYPE", "FLOATTYPE", 
                      "STRINGTYPE", "VOIDTYPE", "AUTOTYPE", "ARRAYTYPE", 
                      "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "ID", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_shortvardecl = 4
    RULE_fulvardecl = 5
    RULE_arraydecl = 6
    RULE_eletype = 7
    RULE_vartype = 8
    RULE_intlitlist = 9
    RULE_idlist = 10
    RULE_exprlist = 11
    RULE_funcdecl = 12
    RULE_funcproto = 13
    RULE_funcbody = 14
    RULE_returntype = 15
    RULE_paralistdecl = 16
    RULE_paradecl = 17
    RULE_expr = 18
    RULE_stringexpr = 19
    RULE_relationalexpr = 20
    RULE_logical_and_orexpr = 21
    RULE_addingexpr = 22
    RULE_multiplyingexpr = 23
    RULE_logical_negateexpr = 24
    RULE_signexpr = 25
    RULE_indexopexpr = 26
    RULE_operand = 27
    RULE_bracket = 28
    RULE_const = 29
    RULE_var = 30
    RULE_funccall = 31
    RULE_arglist = 32
    RULE_arg = 33
    RULE_arraylit = 34
    RULE_stmt = 35
    RULE_assignstmt = 36
    RULE_lhs = 37
    RULE_indexop = 38
    RULE_ifstmt = 39
    RULE_forstmt = 40
    RULE_whilestmt = 41
    RULE_dowhilestmt = 42
    RULE_breakstmt = 43
    RULE_continuestmt = 44
    RULE_returnstmt = 45
    RULE_callstmt = 46
    RULE_blockstmt = 47
    RULE_blockBody = 48
    RULE_atomictype = 49

    ruleNames =  [ "program", "decls", "decl", "vardecl", "shortvardecl", 
                   "fulvardecl", "arraydecl", "eletype", "vartype", "intlitlist", 
                   "idlist", "exprlist", "funcdecl", "funcproto", "funcbody", 
                   "returntype", "paralistdecl", "paradecl", "expr", "stringexpr", 
                   "relationalexpr", "logical_and_orexpr", "addingexpr", 
                   "multiplyingexpr", "logical_negateexpr", "signexpr", 
                   "indexopexpr", "operand", "bracket", "const", "var", 
                   "funccall", "arglist", "arg", "arraylit", "stmt", "assignstmt", 
                   "lhs", "indexop", "ifstmt", "forstmt", "whilestmt", "dowhilestmt", 
                   "breakstmt", "continuestmt", "returnstmt", "callstmt", 
                   "blockstmt", "blockBody", "atomictype" ]

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
    FUNCKEYW=10
    INHERIT=11
    OUT=12
    COMMA=13
    COLON=14
    SEMICOLON=15
    EQUAL=16
    DOT=17
    OPENCMT=18
    LINECMT=19
    PLUSOP=20
    MINUSOP=21
    MULTIPLYOP=22
    DIVIDEOP=23
    MODULOOP=24
    NEGATEOP=25
    CONJUNCOP=26
    DISJUNCOP=27
    RELATIONALOP=28
    STRINGCONCAT=29
    LB=30
    RB=31
    LSQB=32
    RSQB=33
    LCB=34
    RCB=35
    BOOLTYPE=36
    INTTYPE=37
    FLOATTYPE=38
    STRINGTYPE=39
    VOIDTYPE=40
    AUTOTYPE=41
    ARRAYTYPE=42
    INTLIT=43
    FLOATLIT=44
    BOOLEANLIT=45
    STRINGLIT=46
    ID=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

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

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.decls()
            self.state = 101
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.decl()
                self.state = 104
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 113
                self.shortvardecl()
                pass

            elif la_ == 2:
                self.state = 114
                self.fulvardecl()
                pass


            self.state = 117
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
            self.state = 119
            self.idlist()
            self.state = 120
            self.match(MT22Parser.COLON)
            self.state = 121
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(MT22Parser.ID)
                self.state = 124
                self.match(MT22Parser.COLON)
                self.state = 125
                self.vartype()
                self.state = 126
                self.match(MT22Parser.EQUAL)
                self.state = 127
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(MT22Parser.ID)
                self.state = 130
                self.match(MT22Parser.COMMA)
                self.state = 131
                self.fulvardecl()
                self.state = 132
                self.match(MT22Parser.COMMA)
                self.state = 133
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

        def ARRAYTYPE(self):
            return self.getToken(MT22Parser.ARRAYTYPE, 0)

        def LSQB(self):
            return self.getToken(MT22Parser.LSQB, 0)

        def intlitlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlitlistContext,0)


        def RSQB(self):
            return self.getToken(MT22Parser.RSQB, 0)

        def eletype(self):
            return self.getTypedRuleContext(MT22Parser.EletypeContext,0)


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
            self.state = 137
            self.match(MT22Parser.ARRAYTYPE)
            self.state = 138
            self.match(MT22Parser.LSQB)
            self.state = 139
            self.intlitlist()
            self.state = 140
            self.match(MT22Parser.RSQB)
            self.state = 141
            self.match(MT22Parser.T__0)
            self.state = 142
            self.eletype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EletypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_eletype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEletype" ):
                return visitor.visitEletype(self)
            else:
                return visitor.visitChildren(self)




    def eletype(self):

        localctx = MT22Parser.EletypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_eletype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.atomictype()
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

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def AUTOTYPE(self):
            return self.getToken(MT22Parser.AUTOTYPE, 0)

        def arraydecl(self):
            return self.getTypedRuleContext(MT22Parser.ArraydeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vartype)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLTYPE, MT22Parser.INTTYPE, MT22Parser.FLOATTYPE, MT22Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.atomictype()
                pass
            elif token in [MT22Parser.AUTOTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(MT22Parser.AUTOTYPE)
                pass
            elif token in [MT22Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.arraydecl()
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


    class IntlitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def intlitlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlitlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_intlitlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntlitlist" ):
                return visitor.visitIntlitlist(self)
            else:
                return visitor.visitChildren(self)




    def intlitlist(self):

        localctx = MT22Parser.IntlitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_intlitlist)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(MT22Parser.INTLIT)
                self.state = 152
                self.match(MT22Parser.COMMA)
                self.state = 153
                self.intlitlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(MT22Parser.INTLIT)
                pass


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
        self.enterRule(localctx, 20, self.RULE_idlist)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(MT22Parser.ID)
                self.state = 158
                self.match(MT22Parser.COMMA)
                self.state = 159
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
        self.enterRule(localctx, 22, self.RULE_exprlist)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.expr()
                self.state = 164
                self.match(MT22Parser.COMMA)
                self.state = 165
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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
        self.enterRule(localctx, 24, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.funcproto()
            self.state = 171
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
        self.enterRule(localctx, 26, self.RULE_funcproto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MT22Parser.ID)
            self.state = 174
            self.match(MT22Parser.COLON)
            self.state = 175
            self.match(MT22Parser.FUNCKEYW)
            self.state = 176
            self.returntype()
            self.state = 177
            self.match(MT22Parser.LB)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INHERIT) | (1 << MT22Parser.OUT) | (1 << MT22Parser.ID))) != 0):
                self.state = 178
                self.paralistdecl()


            self.state = 181
            self.match(MT22Parser.RB)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 182
                self.match(MT22Parser.INHERIT)
                self.state = 183
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
        self.enterRule(localctx, 28, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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

        def atomictype(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MT22Parser.VOIDTYPE, 0)

        def AUTOTYPE(self):
            return self.getToken(MT22Parser.AUTOTYPE, 0)

        def arraydecl(self):
            return self.getTypedRuleContext(MT22Parser.ArraydeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MT22Parser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returntype)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLTYPE, MT22Parser.INTTYPE, MT22Parser.FLOATTYPE, MT22Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.atomictype()
                pass
            elif token in [MT22Parser.VOIDTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(MT22Parser.VOIDTYPE)
                pass
            elif token in [MT22Parser.AUTOTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(MT22Parser.AUTOTYPE)
                pass
            elif token in [MT22Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.arraydecl()
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
        self.enterRule(localctx, 32, self.RULE_paralistdecl)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.paradecl()
                self.state = 195
                self.match(MT22Parser.COMMA)
                self.state = 196
                self.paralistdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
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
        self.enterRule(localctx, 34, self.RULE_paradecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 201
                self.match(MT22Parser.INHERIT)


            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 204
                self.match(MT22Parser.OUT)


            self.state = 207
            self.match(MT22Parser.ID)
            self.state = 208
            self.match(MT22Parser.COLON)
            self.state = 209
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

        def stringexpr(self):
            return self.getTypedRuleContext(MT22Parser.StringexprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.stringexpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalexpr(self):
            return self.getTypedRuleContext(MT22Parser.RelationalexprContext,0)


        def stringexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StringexprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StringexprContext,i)


        def STRINGCONCAT(self):
            return self.getToken(MT22Parser.STRINGCONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringexpr" ):
                return visitor.visitStringexpr(self)
            else:
                return visitor.visitChildren(self)



    def stringexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.StringexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_stringexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.relationalexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.StringexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stringexpr)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    self.match(MT22Parser.STRINGCONCAT)
                    self.state = 218
                    self.stringexpr(3) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and_orexpr(self):
            return self.getTypedRuleContext(MT22Parser.Logical_and_orexprContext,0)


        def RELATIONALOP(self):
            return self.getToken(MT22Parser.RELATIONALOP, 0)

        def relationalexpr(self):
            return self.getTypedRuleContext(MT22Parser.RelationalexprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_relationalexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalexpr" ):
                return visitor.visitRelationalexpr(self)
            else:
                return visitor.visitChildren(self)



    def relationalexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.RelationalexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_relationalexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 225
                self.logical_and_orexpr(0)
                self.state = 226
                self.match(MT22Parser.RELATIONALOP)
                self.state = 227
                self.relationalexpr(2)
                pass

            elif la_ == 2:
                self.state = 229
                self.logical_and_orexpr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.RelationalexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalexpr)
                    self.state = 232
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 233
                    self.match(MT22Parser.RELATIONALOP)
                    self.state = 234
                    self.logical_and_orexpr(0) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_and_orexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addingexpr(self):
            return self.getTypedRuleContext(MT22Parser.AddingexprContext,0)


        def logical_and_orexpr(self):
            return self.getTypedRuleContext(MT22Parser.Logical_and_orexprContext,0)


        def CONJUNCOP(self):
            return self.getToken(MT22Parser.CONJUNCOP, 0)

        def DISJUNCOP(self):
            return self.getToken(MT22Parser.DISJUNCOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logical_and_orexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and_orexpr" ):
                return visitor.visitLogical_and_orexpr(self)
            else:
                return visitor.visitChildren(self)



    def logical_and_orexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logical_and_orexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_logical_and_orexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.addingexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_and_orexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_and_orexpr)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.CONJUNCOP or _la==MT22Parser.DISJUNCOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.addingexpr(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddingexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplyingexpr(self):
            return self.getTypedRuleContext(MT22Parser.MultiplyingexprContext,0)


        def addingexpr(self):
            return self.getTypedRuleContext(MT22Parser.AddingexprContext,0)


        def PLUSOP(self):
            return self.getToken(MT22Parser.PLUSOP, 0)

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_addingexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddingexpr" ):
                return visitor.visitAddingexpr(self)
            else:
                return visitor.visitChildren(self)



    def addingexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.AddingexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_addingexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.multiplyingexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.AddingexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addingexpr)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUSOP or _la==MT22Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.multiplyingexpr(0) 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplyingexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_negateexpr(self):
            return self.getTypedRuleContext(MT22Parser.Logical_negateexprContext,0)


        def multiplyingexpr(self):
            return self.getTypedRuleContext(MT22Parser.MultiplyingexprContext,0)


        def MULTIPLYOP(self):
            return self.getToken(MT22Parser.MULTIPLYOP, 0)

        def DIVIDEOP(self):
            return self.getToken(MT22Parser.DIVIDEOP, 0)

        def MODULOOP(self):
            return self.getToken(MT22Parser.MODULOOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplyingexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplyingexpr" ):
                return visitor.visitMultiplyingexpr(self)
            else:
                return visitor.visitChildren(self)



    def multiplyingexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.MultiplyingexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_multiplyingexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.logical_negateexpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.MultiplyingexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplyingexpr)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULTIPLYOP) | (1 << MT22Parser.DIVIDEOP) | (1 << MT22Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 267
                    self.logical_negateexpr() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_negateexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATEOP(self):
            return self.getToken(MT22Parser.NEGATEOP, 0)

        def logical_negateexpr(self):
            return self.getTypedRuleContext(MT22Parser.Logical_negateexprContext,0)


        def signexpr(self):
            return self.getTypedRuleContext(MT22Parser.SignexprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_logical_negateexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_negateexpr" ):
                return visitor.visitLogical_negateexpr(self)
            else:
                return visitor.visitChildren(self)




    def logical_negateexpr(self):

        localctx = MT22Parser.Logical_negateexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_logical_negateexpr)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NEGATEOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(MT22Parser.NEGATEOP)
                self.state = 274
                self.logical_negateexpr()
                pass
            elif token in [MT22Parser.MINUSOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.signexpr()
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


    class SignexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def signexpr(self):
            return self.getTypedRuleContext(MT22Parser.SignexprContext,0)


        def indexopexpr(self):
            return self.getTypedRuleContext(MT22Parser.IndexopexprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_signexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignexpr" ):
                return visitor.visitSignexpr(self)
            else:
                return visitor.visitChildren(self)




    def signexpr(self):

        localctx = MT22Parser.SignexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_signexpr)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(MT22Parser.MINUSOP)
                self.state = 279
                self.signexpr()
                pass
            elif token in [MT22Parser.LB, MT22Parser.LCB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLEANLIT, MT22Parser.STRINGLIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.indexopexpr()
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


    class IndexopexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LSQB(self):
            return self.getToken(MT22Parser.LSQB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RSQB(self):
            return self.getToken(MT22Parser.RSQB, 0)

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexopexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexopexpr" ):
                return visitor.visitIndexopexpr(self)
            else:
                return visitor.visitChildren(self)




    def indexopexpr(self):

        localctx = MT22Parser.IndexopexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_indexopexpr)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(MT22Parser.ID)
                self.state = 284
                self.match(MT22Parser.LSQB)
                self.state = 285
                self.exprlist()
                self.state = 286
                self.match(MT22Parser.RSQB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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


        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def bracket(self):
            return self.getTypedRuleContext(MT22Parser.BracketContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_operand)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.const()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.arraylit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 295
                self.bracket()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracketContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return MT22Parser.RULE_bracket

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracket" ):
                return visitor.visitBracket(self)
            else:
                return visitor.visitChildren(self)




    def bracket(self):

        localctx = MT22Parser.BracketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_bracket)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(MT22Parser.LB)
            self.state = 299
            self.expr()
            self.state = 300
            self.match(MT22Parser.RB)
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

        def BOOLEANLIT(self):
            return self.getToken(MT22Parser.BOOLEANLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = MT22Parser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLEANLIT) | (1 << MT22Parser.STRINGLIT))) != 0)):
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
        self.enterRule(localctx, 60, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
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
        self.enterRule(localctx, 62, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MT22Parser.ID)
            self.state = 307
            self.match(MT22Parser.LB)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MINUSOP) | (1 << MT22Parser.NEGATEOP) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLEANLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 308
                self.arglist()


            self.state = 311
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
        self.enterRule(localctx, 64, self.RULE_arglist)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.arg()
                self.state = 314
                self.match(MT22Parser.COMMA)
                self.state = 315
                self.arglist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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
        self.enterRule(localctx, 66, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(MT22Parser.LCB)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MINUSOP) | (1 << MT22Parser.NEGATEOP) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLEANLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 323
                self.exprlist()


            self.state = 326
            self.match(MT22Parser.RCB)
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


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


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
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.assignstmt()
                self.state = 329
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 333
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 334
                self.dowhilestmt()
                self.state = 335
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 337
                self.breakstmt()
                self.state = 338
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 340
                self.continuestmt()
                self.state = 341
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 343
                self.returnstmt()
                self.state = 344
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 346
                self.callstmt()
                self.state = 347
                self.match(MT22Parser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 349
                self.blockstmt()
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
            self.state = 352
            self.lhs()
            self.state = 353
            self.match(MT22Parser.EQUAL)
            self.state = 354
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
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.indexop()
                pass


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

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


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
        self.enterRule(localctx, 76, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MT22Parser.ID)
            self.state = 361
            self.match(MT22Parser.LSQB)
            self.state = 362
            self.exprlist()
            self.state = 363
            self.match(MT22Parser.RSQB)
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
        self.enterRule(localctx, 78, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MT22Parser.T__1)
            self.state = 366
            self.match(MT22Parser.LB)
            self.state = 367
            self.expr()
            self.state = 368
            self.match(MT22Parser.RB)
            self.state = 369
            self.stmt()
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 370
                self.match(MT22Parser.T__2)
                self.state = 371
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
        self.enterRule(localctx, 80, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MT22Parser.T__3)
            self.state = 375
            self.match(MT22Parser.LB)
            self.state = 376
            self.match(MT22Parser.ID)
            self.state = 377
            self.match(MT22Parser.EQUAL)
            self.state = 378
            self.expr()
            self.state = 379
            self.match(MT22Parser.COMMA)
            self.state = 380
            self.expr()
            self.state = 381
            self.match(MT22Parser.COMMA)
            self.state = 382
            self.expr()
            self.state = 383
            self.match(MT22Parser.RB)
            self.state = 384
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
        self.enterRule(localctx, 82, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MT22Parser.T__4)
            self.state = 387
            self.match(MT22Parser.LB)
            self.state = 388
            self.expr()
            self.state = 389
            self.match(MT22Parser.RB)
            self.state = 390
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

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


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
        self.enterRule(localctx, 84, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MT22Parser.T__5)
            self.state = 393
            self.stmt()
            self.state = 394
            self.match(MT22Parser.T__4)
            self.state = 395
            self.match(MT22Parser.LB)
            self.state = 396
            self.expr()
            self.state = 397
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
        self.enterRule(localctx, 86, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MT22Parser.T__6)
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
        self.enterRule(localctx, 88, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MT22Parser.T__7)
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
        self.enterRule(localctx, 90, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MT22Parser.T__8)
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MINUSOP) | (1 << MT22Parser.NEGATEOP) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLEANLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 404
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
        self.enterRule(localctx, 92, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 94, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MT22Parser.LCB)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.T__1) | (1 << MT22Parser.T__3) | (1 << MT22Parser.T__4) | (1 << MT22Parser.T__5) | (1 << MT22Parser.T__6) | (1 << MT22Parser.T__7) | (1 << MT22Parser.T__8) | (1 << MT22Parser.LCB) | (1 << MT22Parser.ID))) != 0):
                self.state = 410
                self.blockBody()


            self.state = 413
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
        self.enterRule(localctx, 96, self.RULE_blockBody)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 415
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 416
                    self.vardecl()
                    pass


                self.state = 419
                self.blockBody()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 421
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 422
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


    class AtomictypeContext(ParserRuleContext):
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
            return MT22Parser.RULE_atomictype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomictype" ):
                return visitor.visitAtomictype(self)
            else:
                return visitor.visitChildren(self)




    def atomictype(self):

        localctx = MT22Parser.AtomictypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_atomictype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.stringexpr_sempred
        self._predicates[20] = self.relationalexpr_sempred
        self._predicates[21] = self.logical_and_orexpr_sempred
        self._predicates[22] = self.addingexpr_sempred
        self._predicates[23] = self.multiplyingexpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def stringexpr_sempred(self, localctx:StringexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def relationalexpr_sempred(self, localctx:RelationalexprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def logical_and_orexpr_sempred(self, localctx:Logical_and_orexprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def addingexpr_sempred(self, localctx:AddingexprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def multiplyingexpr_sempred(self, localctx:MultiplyingexprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




