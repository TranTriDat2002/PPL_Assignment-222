# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\7\23\u00cb\n\23\f")
        buf.write("\23\16\23\u00ce\13\23\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u00d9\n\24\f\24\16\24\u00dc\13\24\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u00fc\n")
        buf.write("\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\7-\u013f\n-\f-\16-\u0142\13-\3-\3-\3-\7-\u0147\n-\f")
        buf.write("-\16-\u014a\13-\3-\3-\5-\u014e\n-\3.\3.\7.\u0152\n.\f")
        buf.write(".\16.\u0155\13.\3/\3/\5/\u0159\n/\3/\6/\u015c\n/\r/\16")
        buf.write("/\u015d\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0170\n\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\5\63\u017f\n\63\3\64\3\64\3\64\3\64\7\64\u0185\n")
        buf.write("\64\f\64\16\64\u0188\13\64\3\64\3\64\3\64\3\65\3\65\3")
        buf.write("\66\3\66\3\67\3\67\38\38\58\u0195\n8\38\38\38\78\u019a")
        buf.write("\n8\f8\168\u019d\138\39\69\u01a0\n9\r9\169\u01a1\39\3")
        buf.write("9\3:\3:\3:\3:\7:\u01aa\n:\f:\16:\u01ad\13:\3:\3:\3;\3")
        buf.write(";\3;\3;\7;\u01b5\n;\f;\16;\u01b8\13;\3;\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3\u00cc\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y-[\2]\2_.a\2c\2e/g\60i\2")
        buf.write("k\2m\2o\61q\62s\63u\64w\65\3\2\f\4\2\f\f\17\17\3\2\63")
        buf.write(";\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\n\2$$))^^ddhhpptt")
        buf.write("vv\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\4\2$$^^\2\u01d5")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2Y\3\2\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\3y\3\2\2\2\5|\3\2\2\2\7\177\3\2\2\2\t\u0084\3\2")
        buf.write("\2\2\13\u0088\3\2\2\2\r\u008e\3\2\2\2\17\u0091\3\2\2\2")
        buf.write("\21\u0097\3\2\2\2\23\u00a0\3\2\2\2\25\u00a7\3\2\2\2\27")
        buf.write("\u00b0\3\2\2\2\31\u00b8\3\2\2\2\33\u00bc\3\2\2\2\35\u00be")
        buf.write("\3\2\2\2\37\u00c0\3\2\2\2!\u00c2\3\2\2\2#\u00c4\3\2\2")
        buf.write("\2%\u00c6\3\2\2\2\'\u00d4\3\2\2\2)\u00df\3\2\2\2+\u00e1")
        buf.write("\3\2\2\2-\u00e3\3\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2")
        buf.write("\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67\u00ee\3\2\2\2")
        buf.write("9\u00fb\3\2\2\2;\u00fd\3\2\2\2=\u0100\3\2\2\2?\u0102\3")
        buf.write("\2\2\2A\u0104\3\2\2\2C\u0106\3\2\2\2E\u0108\3\2\2\2G\u010a")
        buf.write("\3\2\2\2I\u010c\3\2\2\2K\u0114\3\2\2\2M\u011c\3\2\2\2")
        buf.write("O\u0122\3\2\2\2Q\u0129\3\2\2\2S\u012e\3\2\2\2U\u0133\3")
        buf.write("\2\2\2W\u0139\3\2\2\2Y\u014d\3\2\2\2[\u014f\3\2\2\2]\u0156")
        buf.write("\3\2\2\2_\u016f\3\2\2\2a\u0171\3\2\2\2c\u0176\3\2\2\2")
        buf.write("e\u017e\3\2\2\2g\u0180\3\2\2\2i\u018c\3\2\2\2k\u018e\3")
        buf.write("\2\2\2m\u0190\3\2\2\2o\u0194\3\2\2\2q\u019f\3\2\2\2s\u01a5")
        buf.write("\3\2\2\2u\u01b0\3\2\2\2w\u01be\3\2\2\2yz\7q\2\2z{\7h\2")
        buf.write("\2{\4\3\2\2\2|}\7k\2\2}~\7h\2\2~\6\3\2\2\2\177\u0080\7")
        buf.write("g\2\2\u0080\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\b\3\2\2\2\u0084\u0085\7h\2\2\u0085\u0086")
        buf.write("\7q\2\2\u0086\u0087\7t\2\2\u0087\n\3\2\2\2\u0088\u0089")
        buf.write("\7y\2\2\u0089\u008a\7j\2\2\u008a\u008b\7k\2\2\u008b\u008c")
        buf.write("\7n\2\2\u008c\u008d\7g\2\2\u008d\f\3\2\2\2\u008e\u008f")
        buf.write("\7f\2\2\u008f\u0090\7q\2\2\u0090\16\3\2\2\2\u0091\u0092")
        buf.write("\7d\2\2\u0092\u0093\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7m\2\2\u0096\20\3\2\2\2\u0097\u0098")
        buf.write("\7e\2\2\u0098\u0099\7q\2\2\u0099\u009a\7p\2\2\u009a\u009b")
        buf.write("\7v\2\2\u009b\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e")
        buf.write("\7w\2\2\u009e\u009f\7g\2\2\u009f\22\3\2\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7w\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7p\2\2\u00a6\24")
        buf.write("\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7e\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7p\2\2\u00af\26")
        buf.write("\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3")
        buf.write("\7j\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7v\2\2\u00b7\30\3\2\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7v\2\2\u00bb\32")
        buf.write("\3\2\2\2\u00bc\u00bd\7.\2\2\u00bd\34\3\2\2\2\u00be\u00bf")
        buf.write("\7<\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\7=\2\2\u00c1 \3\2")
        buf.write("\2\2\u00c2\u00c3\7?\2\2\u00c3\"\3\2\2\2\u00c4\u00c5\7")
        buf.write("\60\2\2\u00c5$\3\2\2\2\u00c6\u00c7\7\61\2\2\u00c7\u00c8")
        buf.write("\7,\2\2\u00c8\u00cc\3\2\2\2\u00c9\u00cb\13\2\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3")
        buf.write("\2\2\2\u00cf\u00d0\7,\2\2\u00d0\u00d1\7\61\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d3\b\23\2\2\u00d3&\3\2\2\2\u00d4\u00d5")
        buf.write("\7\61\2\2\u00d5\u00d6\7\61\2\2\u00d6\u00da\3\2\2\2\u00d7")
        buf.write("\u00d9\n\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\3")
        buf.write("\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\b\24\2\2\u00de")
        buf.write("(\3\2\2\2\u00df\u00e0\7-\2\2\u00e0*\3\2\2\2\u00e1\u00e2")
        buf.write("\7/\2\2\u00e2,\3\2\2\2\u00e3\u00e4\7,\2\2\u00e4.\3\2\2")
        buf.write("\2\u00e5\u00e6\7\61\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\7")
        buf.write("\'\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\7#\2\2\u00ea\64\3")
        buf.write("\2\2\2\u00eb\u00ec\7(\2\2\u00ec\u00ed\7(\2\2\u00ed\66")
        buf.write("\3\2\2\2\u00ee\u00ef\7~\2\2\u00ef\u00f0\7~\2\2\u00f08")
        buf.write("\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2\u00fc\7?\2\2\u00f3\u00f4")
        buf.write("\7#\2\2\u00f4\u00fc\7?\2\2\u00f5\u00fc\7>\2\2\u00f6\u00f7")
        buf.write("\7>\2\2\u00f7\u00fc\7?\2\2\u00f8\u00fc\7@\2\2\u00f9\u00fa")
        buf.write("\7@\2\2\u00fa\u00fc\7?\2\2\u00fb\u00f1\3\2\2\2\u00fb\u00f3")
        buf.write("\3\2\2\2\u00fb\u00f5\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fb")
        buf.write("\u00f8\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc:\3\2\2\2\u00fd")
        buf.write("\u00fe\7<\2\2\u00fe\u00ff\7<\2\2\u00ff<\3\2\2\2\u0100")
        buf.write("\u0101\7*\2\2\u0101>\3\2\2\2\u0102\u0103\7+\2\2\u0103")
        buf.write("@\3\2\2\2\u0104\u0105\7]\2\2\u0105B\3\2\2\2\u0106\u0107")
        buf.write("\7_\2\2\u0107D\3\2\2\2\u0108\u0109\7}\2\2\u0109F\3\2\2")
        buf.write("\2\u010a\u010b\7\177\2\2\u010bH\3\2\2\2\u010c\u010d\7")
        buf.write("d\2\2\u010d\u010e\7q\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7n\2\2\u0110\u0111\7g\2\2\u0111\u0112\7c\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113J\3\2\2\2\u0114\u0115\7k\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7v\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7i\2\2\u0119\u011a\7g\2\2\u011a\u011b\7t\2\2\u011bL\3")
        buf.write("\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7n\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7c\2\2\u0120\u0121\7v\2\2\u0121N\3")
        buf.write("\2\2\2\u0122\u0123\7u\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7t\2\2\u0125\u0126\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128")
        buf.write("\7i\2\2\u0128P\3\2\2\2\u0129\u012a\7x\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7k\2\2\u012c\u012d\7f\2\2\u012dR\3")
        buf.write("\2\2\2\u012e\u012f\7c\2\2\u012f\u0130\7w\2\2\u0130\u0131")
        buf.write("\7v\2\2\u0131\u0132\7q\2\2\u0132T\3\2\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7t\2\2\u0135\u0136\7t\2\2\u0136\u0137")
        buf.write("\7c\2\2\u0137\u0138\7{\2\2\u0138V\3\2\2\2\u0139\u013a")
        buf.write("\t\3\2\2\u013aX\3\2\2\2\u013b\u014e\7\62\2\2\u013c\u0140")
        buf.write("\5W,\2\u013d\u013f\5k\66\2\u013e\u013d\3\2\2\2\u013f\u0142")
        buf.write("\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0148\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144\7a\2\2")
        buf.write("\u0144\u0147\5k\66\2\u0145\u0147\5k\66\2\u0146\u0143\3")
        buf.write("\2\2\2\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014b\u014c\b-\3\2\u014c\u014e\3\2\2\2")
        buf.write("\u014d\u013b\3\2\2\2\u014d\u013c\3\2\2\2\u014eZ\3\2\2")
        buf.write("\2\u014f\u0153\5#\22\2\u0150\u0152\5k\66\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\\\3\2\2\2\u0155\u0153\3\2\2\2\u0156")
        buf.write("\u0158\t\4\2\2\u0157\u0159\t\5\2\2\u0158\u0157\3\2\2\2")
        buf.write("\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u015c\5")
        buf.write("k\66\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e^\3\2\2\2\u015f\u0160")
        buf.write("\5Y-\2\u0160\u0161\5[.\2\u0161\u0162\5]/\2\u0162\u0163")
        buf.write("\b\60\4\2\u0163\u0170\3\2\2\2\u0164\u0165\5Y-\2\u0165")
        buf.write("\u0166\5[.\2\u0166\u0167\b\60\5\2\u0167\u0170\3\2\2\2")
        buf.write("\u0168\u0169\5Y-\2\u0169\u016a\5]/\2\u016a\u016b\b\60")
        buf.write("\6\2\u016b\u0170\3\2\2\2\u016c\u016d\5[.\2\u016d\u016e")
        buf.write("\5]/\2\u016e\u0170\3\2\2\2\u016f\u015f\3\2\2\2\u016f\u0164")
        buf.write("\3\2\2\2\u016f\u0168\3\2\2\2\u016f\u016c\3\2\2\2\u0170")
        buf.write("`\3\2\2\2\u0171\u0172\7v\2\2\u0172\u0173\7t\2\2\u0173")
        buf.write("\u0174\7w\2\2\u0174\u0175\7g\2\2\u0175b\3\2\2\2\u0176")
        buf.write("\u0177\7h\2\2\u0177\u0178\7c\2\2\u0178\u0179\7n\2\2\u0179")
        buf.write("\u017a\7u\2\2\u017a\u017b\7g\2\2\u017bd\3\2\2\2\u017c")
        buf.write("\u017f\5a\61\2\u017d\u017f\5c\62\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017d\3\2\2\2\u017ff\3\2\2\2\u0180\u0186\7$\2\2")
        buf.write("\u0181\u0185\n\6\2\2\u0182\u0183\7^\2\2\u0183\u0185\t")
        buf.write("\7\2\2\u0184\u0181\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0188")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\7$\2\2")
        buf.write("\u018a\u018b\b\64\7\2\u018bh\3\2\2\2\u018c\u018d\t\b\2")
        buf.write("\2\u018dj\3\2\2\2\u018e\u018f\t\t\2\2\u018fl\3\2\2\2\u0190")
        buf.write("\u0191\7a\2\2\u0191n\3\2\2\2\u0192\u0195\5i\65\2\u0193")
        buf.write("\u0195\5m\67\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195\u019b\3\2\2\2\u0196\u019a\5i\65\2\u0197\u019a\5")
        buf.write("m\67\2\u0198\u019a\5k\66\2\u0199\u0196\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019cp\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019e\u01a0\t\n\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\b9\2\2\u01a4r\3")
        buf.write("\2\2\2\u01a5\u01ab\7$\2\2\u01a6\u01aa\n\6\2\2\u01a7\u01a8")
        buf.write("\7^\2\2\u01a8\u01aa\t\7\2\2\u01a9\u01a6\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ae\u01af\b:\b\2\u01aft\3\2\2\2\u01b0\u01b6\7")
        buf.write("$\2\2\u01b1\u01b5\n\13\2\2\u01b2\u01b3\7^\2\2\u01b3\u01b5")
        buf.write("\t\7\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7")
        buf.write("^\2\2\u01ba\u01bb\n\7\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd")
        buf.write("\b;\t\2\u01bdv\3\2\2\2\u01be\u01bf\13\2\2\2\u01bf\u01c0")
        buf.write("\b<\n\2\u01c0x\3\2\2\2\31\2\u00cc\u00da\u00fb\u0140\u0146")
        buf.write("\u0148\u014d\u0153\u0158\u015d\u016f\u017e\u0184\u0186")
        buf.write("\u0194\u0199\u019b\u01a1\u01a9\u01ab\u01b4\u01b6\13\b")
        buf.write("\2\2\3-\2\3\60\3\3\60\4\3\60\5\3\64\6\3:\7\3;\b\3<\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    FUNCKEYW = 10
    INHERIT = 11
    OUT = 12
    COMMA = 13
    COLON = 14
    SEMICOLON = 15
    EQUAL = 16
    DOT = 17
    OPENCMT = 18
    LINECMT = 19
    PLUSOP = 20
    MINUSOP = 21
    MULTIPLYOP = 22
    DIVIDEOP = 23
    MODULOOP = 24
    NEGATEOP = 25
    CONJUNCOP = 26
    DISJUNCOP = 27
    RELATIONALOP = 28
    STRINGCONCAT = 29
    LB = 30
    RB = 31
    LSQB = 32
    RSQB = 33
    LCB = 34
    RCB = 35
    BOOLTYPE = 36
    INTTYPE = 37
    FLOATTYPE = 38
    STRINGTYPE = 39
    VOIDTYPE = 40
    AUTOTYPE = 41
    ARRAYTYPE = 42
    INTLIT = 43
    FLOATLIT = 44
    BOOLEANLIT = 45
    STRINGLIT = 46
    ID = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'of'", "'if'", "'else'", "'for'", "'while'", "'do'", "'break'", 
            "'continue'", "'return'", "'function'", "'inherit'", "'out'", 
            "','", "':'", "';'", "'='", "'.'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'::'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "'boolean'", "'integer'", "'float'", "'string'", 
            "'void'", "'auto'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "FUNCKEYW", "INHERIT", "OUT", "COMMA", "COLON", "SEMICOLON", 
            "EQUAL", "DOT", "OPENCMT", "LINECMT", "PLUSOP", "MINUSOP", "MULTIPLYOP", 
            "DIVIDEOP", "MODULOOP", "NEGATEOP", "CONJUNCOP", "DISJUNCOP", 
            "RELATIONALOP", "STRINGCONCAT", "LB", "RB", "LSQB", "RSQB", 
            "LCB", "RCB", "BOOLTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", 
            "VOIDTYPE", "AUTOTYPE", "ARRAYTYPE", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "STRINGLIT", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "FUNCKEYW", "INHERIT", "OUT", "COMMA", 
                  "COLON", "SEMICOLON", "EQUAL", "DOT", "OPENCMT", "LINECMT", 
                  "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", 
                  "NEGATEOP", "CONJUNCOP", "DISJUNCOP", "RELATIONALOP", 
                  "STRINGCONCAT", "LB", "RB", "LSQB", "RSQB", "LCB", "RCB", 
                  "BOOLTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
                  "AUTOTYPE", "ARRAYTYPE", "NONZERODIGIT", "INTLIT", "DECIMAL", 
                  "EXP", "FLOATLIT", "TRUE", "FALSE", "BOOLEANLIT", "STRINGLIT", 
                  "LETTER", "DIGIT", "UNDERSCORE", "ID", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[43] = self.INTLIT_action 
            actions[46] = self.FLOATLIT_action 
            actions[50] = self.STRINGLIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	self.text = self.text[1:];
            	raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	self.text = self.text[1:];
            	raise IllegalEscape(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	raise ErrorToken(self.text)

     


