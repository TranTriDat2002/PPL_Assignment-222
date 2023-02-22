# Generated from c:\Data\PPL_ass\assignment1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0235\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u0152")
        buf.write("\n\34\f\34\16\34\u0155\13\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\7\35\u0160\n\35\f\35\16\35\u0163")
        buf.write("\13\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write("\3&\5&\u0183\n&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\3\67\7\67\u01c9\n\67\f")
        buf.write("\67\16\67\u01cc\13\67\3\67\3\67\3\67\7\67\u01d1\n\67\f")
        buf.write("\67\16\67\u01d4\13\67\3\67\3\67\5\67\u01d8\n\67\38\38")
        buf.write("\68\u01dc\n8\r8\168\u01dd\39\39\59\u01e2\n9\39\39\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u01f6\n")
        buf.write(":\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\5=\u0205\n=\3")
        buf.write(">\3>\3?\3?\3?\3?\3?\3?\7?\u020f\n?\f?\16?\u0212\13?\3")
        buf.write("?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\5C\u021f\nC\3C\3C\3C\7")
        buf.write("C\u0224\nC\fC\16C\u0227\13C\3D\6D\u022a\nD\rD\16D\u022b")
        buf.write("\3D\3D\3E\3E\3F\3F\3G\3G\3\u0153\2H\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\2m\67o\2q\2s8u\2w\2y9{:};\177")
        buf.write("\2\u0081\2\u0083\2\u0085<\u0087=\u0089>\u008b?\u008d@")
        buf.write("\3\2\13\4\2\f\f\17\17\3\2\63;\4\2GGgg\4\2--//\3\2$$\t")
        buf.write("\2$$))ddhhppttvv\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2")
        buf.write("\u0245\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f")
        buf.write("\3\2\2\2\5\u0092\3\2\2\2\7\u009e\3\2\2\2\t\u00a8\3\2\2")
        buf.write("\2\13\u00b4\3\2\2\2\r\u00bf\3\2\2\2\17\u00c2\3\2\2\2\21")
        buf.write("\u00c7\3\2\2\2\23\u00cb\3\2\2\2\25\u00d1\3\2\2\2\27\u00d4")
        buf.write("\3\2\2\2\31\u00da\3\2\2\2\33\u00e3\3\2\2\2\35\u00ea\3")
        buf.write("\2\2\2\37\u00f7\3\2\2\2!\u0102\3\2\2\2#\u010f\3\2\2\2")
        buf.write("%\u011b\3\2\2\2\'\u0121\3\2\2\2)\u0130\3\2\2\2+\u0139")
        buf.write("\3\2\2\2-\u0141\3\2\2\2/\u0145\3\2\2\2\61\u0147\3\2\2")
        buf.write("\2\63\u0149\3\2\2\2\65\u014b\3\2\2\2\67\u014d\3\2\2\2")
        buf.write("9\u015b\3\2\2\2;\u0166\3\2\2\2=\u0168\3\2\2\2?\u016a\3")
        buf.write("\2\2\2A\u016c\3\2\2\2C\u016e\3\2\2\2E\u0170\3\2\2\2G\u0172")
        buf.write("\3\2\2\2I\u0175\3\2\2\2K\u0182\3\2\2\2M\u0184\3\2\2\2")
        buf.write("O\u0187\3\2\2\2Q\u0189\3\2\2\2S\u018b\3\2\2\2U\u018d\3")
        buf.write("\2\2\2W\u018f\3\2\2\2Y\u0191\3\2\2\2[\u0193\3\2\2\2]\u0196")
        buf.write("\3\2\2\2_\u019e\3\2\2\2a\u01a6\3\2\2\2c\u01ac\3\2\2\2")
        buf.write("e\u01b3\3\2\2\2g\u01b8\3\2\2\2i\u01bd\3\2\2\2k\u01c3\3")
        buf.write("\2\2\2m\u01d7\3\2\2\2o\u01d9\3\2\2\2q\u01df\3\2\2\2s\u01f5")
        buf.write("\3\2\2\2u\u01f7\3\2\2\2w\u01fc\3\2\2\2y\u0204\3\2\2\2")
        buf.write("{\u0206\3\2\2\2}\u0208\3\2\2\2\177\u0216\3\2\2\2\u0081")
        buf.write("\u0218\3\2\2\2\u0083\u021a\3\2\2\2\u0085\u021e\3\2\2\2")
        buf.write("\u0087\u0229\3\2\2\2\u0089\u022f\3\2\2\2\u008b\u0231\3")
        buf.write("\2\2\2\u008d\u0233\3\2\2\2\u008f\u0090\7q\2\2\u0090\u0091")
        buf.write("\7h\2\2\u0091\4\3\2\2\2\u0092\u0093\7t\2\2\u0093\u0094")
        buf.write("\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096\7f\2\2\u0096\u0097")
        buf.write("\7K\2\2\u0097\u0098\7p\2\2\u0098\u0099\7v\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\u009b\7i\2\2\u009b\u009c\7g\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\6\3\2\2\2\u009e\u009f\7t\2\2\u009f\u00a0")
        buf.write("\7g\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7f\2\2\u00a2\u00a3")
        buf.write("\7H\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6")
        buf.write("\7c\2\2\u00a6\u00a7\7v\2\2\u00a7\b\3\2\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac")
        buf.write("\7f\2\2\u00ac\u00ad\7D\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7p\2\2\u00b3\n\3\2\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8")
        buf.write("\7f\2\2\u00b8\u00b9\7U\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7i\2\2\u00be\f\3\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\16\3\2\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6\20")
        buf.write("\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\22\3\2\2\2\u00cb\u00cc\7y\2\2\u00cc\u00cd")
        buf.write("\7j\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\24\3\2\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\26\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7m\2\2\u00d9\30\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7v\2\2\u00de\u00df")
        buf.write("\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8\u00e9\7p\2\2\u00e9\34\3\2\2\2\u00ea\u00eb")
        buf.write("\7r\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7K\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4")
        buf.write("\7i\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7t\2\2\u00f6\36")
        buf.write("\3\2\2\2\u00f7\u00f8\7y\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7H\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7v\2\2\u0101 \3\2\2\2\u0102\u0103")
        buf.write("\7r\2\2\u0103\u0104\7t\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7v\2\2\u0107\u0108\7D\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7q\2\2\u010a\u010b\7n\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7c\2\2\u010d\u010e\7p\2\2\u010e\"")
        buf.write("\3\2\2\2\u010f\u0110\7r\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7p\2\2\u0113\u0114\7v\2\2\u0114\u0115")
        buf.write("\7U\2\2\u0115\u0116\7v\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7i\2\2\u011a$\3")
        buf.write("\2\2\2\u011b\u011c\7u\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7r\2\2\u011e\u011f\7g\2\2\u011f\u0120\7t\2\2\u0120&\3")
        buf.write("\2\2\2\u0121\u0122\7r\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124\u0125\7x\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7p\2\2\u0127\u0128\7v\2\2\u0128\u0129\7F\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a\u012b\7h\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7n\2\2\u012e\u012f\7v\2\2\u012f(\3")
        buf.write("\2\2\2\u0130\u0131\7h\2\2\u0131\u0132\7w\2\2\u0132\u0133")
        buf.write("\7p\2\2\u0133\u0134\7e\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7k\2\2\u0136\u0137\7q\2\2\u0137\u0138\7p\2\2\u0138*\3")
        buf.write("\2\2\2\u0139\u013a\7k\2\2\u013a\u013b\7p\2\2\u013b\u013c")
        buf.write("\7j\2\2\u013c\u013d\7g\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7k\2\2\u013f\u0140\7v\2\2\u0140,\3\2\2\2\u0141\u0142")
        buf.write("\7q\2\2\u0142\u0143\7w\2\2\u0143\u0144\7v\2\2\u0144.\3")
        buf.write("\2\2\2\u0145\u0146\7.\2\2\u0146\60\3\2\2\2\u0147\u0148")
        buf.write("\7<\2\2\u0148\62\3\2\2\2\u0149\u014a\7=\2\2\u014a\64\3")
        buf.write("\2\2\2\u014b\u014c\7?\2\2\u014c\66\3\2\2\2\u014d\u014e")
        buf.write("\7\61\2\2\u014e\u014f\7,\2\2\u014f\u0153\3\2\2\2\u0150")
        buf.write("\u0152\13\2\2\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2")
        buf.write("\2\u0153\u0154\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0156")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0157\7,\2\2\u0157")
        buf.write("\u0158\7\61\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b\34\2")
        buf.write("\2\u015a8\3\2\2\2\u015b\u015c\7\61\2\2\u015c\u015d\7\61")
        buf.write("\2\2\u015d\u0161\3\2\2\2\u015e\u0160\n\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0164\u0165\b\35\2\2\u0165:\3\2\2\2\u0166\u0167\7-\2")
        buf.write("\2\u0167<\3\2\2\2\u0168\u0169\7/\2\2\u0169>\3\2\2\2\u016a")
        buf.write("\u016b\7,\2\2\u016b@\3\2\2\2\u016c\u016d\7\61\2\2\u016d")
        buf.write("B\3\2\2\2\u016e\u016f\7\'\2\2\u016fD\3\2\2\2\u0170\u0171")
        buf.write("\7#\2\2\u0171F\3\2\2\2\u0172\u0173\7(\2\2\u0173\u0174")
        buf.write("\7(\2\2\u0174H\3\2\2\2\u0175\u0176\7~\2\2\u0176\u0177")
        buf.write("\7~\2\2\u0177J\3\2\2\2\u0178\u0179\7?\2\2\u0179\u0183")
        buf.write("\7?\2\2\u017a\u017b\7#\2\2\u017b\u0183\7?\2\2\u017c\u0183")
        buf.write("\7>\2\2\u017d\u017e\7>\2\2\u017e\u0183\7?\2\2\u017f\u0183")
        buf.write("\7@\2\2\u0180\u0181\7@\2\2\u0181\u0183\7?\2\2\u0182\u0178")
        buf.write("\3\2\2\2\u0182\u017a\3\2\2\2\u0182\u017c\3\2\2\2\u0182")
        buf.write("\u017d\3\2\2\2\u0182\u017f\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0183L\3\2\2\2\u0184\u0185\7<\2\2\u0185\u0186\7<\2\2")
        buf.write("\u0186N\3\2\2\2\u0187\u0188\7*\2\2\u0188P\3\2\2\2\u0189")
        buf.write("\u018a\7+\2\2\u018aR\3\2\2\2\u018b\u018c\7]\2\2\u018c")
        buf.write("T\3\2\2\2\u018d\u018e\7_\2\2\u018eV\3\2\2\2\u018f\u0190")
        buf.write("\7}\2\2\u0190X\3\2\2\2\u0191\u0192\7\177\2\2\u0192Z\3")
        buf.write("\2\2\2\u0193\u0194\7}\2\2\u0194\u0195\7\177\2\2\u0195")
        buf.write("\\\3\2\2\2\u0196\u0197\7d\2\2\u0197\u0198\7q\2\2\u0198")
        buf.write("\u0199\7q\2\2\u0199\u019a\7n\2\2\u019a\u019b\7g\2\2\u019b")
        buf.write("\u019c\7c\2\2\u019c\u019d\7p\2\2\u019d^\3\2\2\2\u019e")
        buf.write("\u019f\7k\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7v\2\2\u01a1")
        buf.write("\u01a2\7g\2\2\u01a2\u01a3\7i\2\2\u01a3\u01a4\7g\2\2\u01a4")
        buf.write("\u01a5\7t\2\2\u01a5`\3\2\2\2\u01a6\u01a7\7h\2\2\u01a7")
        buf.write("\u01a8\7n\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa\7c\2\2\u01aa")
        buf.write("\u01ab\7v\2\2\u01abb\3\2\2\2\u01ac\u01ad\7u\2\2\u01ad")
        buf.write("\u01ae\7v\2\2\u01ae\u01af\7t\2\2\u01af\u01b0\7k\2\2\u01b0")
        buf.write("\u01b1\7p\2\2\u01b1\u01b2\7i\2\2\u01b2d\3\2\2\2\u01b3")
        buf.write("\u01b4\7x\2\2\u01b4\u01b5\7q\2\2\u01b5\u01b6\7k\2\2\u01b6")
        buf.write("\u01b7\7f\2\2\u01b7f\3\2\2\2\u01b8\u01b9\7c\2\2\u01b9")
        buf.write("\u01ba\7w\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc\7q\2\2\u01bc")
        buf.write("h\3\2\2\2\u01bd\u01be\7c\2\2\u01be\u01bf\7t\2\2\u01bf")
        buf.write("\u01c0\7t\2\2\u01c0\u01c1\7c\2\2\u01c1\u01c2\7{\2\2\u01c2")
        buf.write("j\3\2\2\2\u01c3\u01c4\t\3\2\2\u01c4l\3\2\2\2\u01c5\u01d8")
        buf.write("\7\62\2\2\u01c6\u01ca\5k\66\2\u01c7\u01c9\5\u0081A\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01d2\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01ce\7a\2\2\u01ce\u01d1\5\u0081A\2\u01cf")
        buf.write("\u01d1\5\u0081A\2\u01d0\u01cd\3\2\2\2\u01d0\u01cf\3\2")
        buf.write("\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5")
        buf.write("\u01d6\b\67\3\2\u01d6\u01d8\3\2\2\2\u01d7\u01c5\3\2\2")
        buf.write("\2\u01d7\u01c6\3\2\2\2\u01d8n\3\2\2\2\u01d9\u01db\7\60")
        buf.write("\2\2\u01da\u01dc\5\u0081A\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01dep\3\2\2\2\u01df\u01e1\t\4\2\2\u01e0\u01e2\t\5\2")
        buf.write("\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e4\5\u0081A\2\u01e4r\3\2\2\2\u01e5\u01e6")
        buf.write("\5m\67\2\u01e6\u01e7\5o8\2\u01e7\u01e8\5q9\2\u01e8\u01e9")
        buf.write("\b:\4\2\u01e9\u01f6\3\2\2\2\u01ea\u01eb\5m\67\2\u01eb")
        buf.write("\u01ec\5o8\2\u01ec\u01ed\b:\5\2\u01ed\u01f6\3\2\2\2\u01ee")
        buf.write("\u01ef\5m\67\2\u01ef\u01f0\5q9\2\u01f0\u01f1\b:\6\2\u01f1")
        buf.write("\u01f6\3\2\2\2\u01f2\u01f3\5o8\2\u01f3\u01f4\5q9\2\u01f4")
        buf.write("\u01f6\3\2\2\2\u01f5\u01e5\3\2\2\2\u01f5\u01ea\3\2\2\2")
        buf.write("\u01f5\u01ee\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f6t\3\2\2")
        buf.write("\2\u01f7\u01f8\7v\2\2\u01f8\u01f9\7t\2\2\u01f9\u01fa\7")
        buf.write("w\2\2\u01fa\u01fb\7g\2\2\u01fbv\3\2\2\2\u01fc\u01fd\7")
        buf.write("h\2\2\u01fd\u01fe\7c\2\2\u01fe\u01ff\7n\2\2\u01ff\u0200")
        buf.write("\7u\2\2\u0200\u0201\7g\2\2\u0201x\3\2\2\2\u0202\u0205")
        buf.write("\5u;\2\u0203\u0205\5w<\2\u0204\u0202\3\2\2\2\u0204\u0203")
        buf.write("\3\2\2\2\u0205z\3\2\2\2\u0206\u0207\7$\2\2\u0207|\3\2")
        buf.write("\2\2\u0208\u0210\5{>\2\u0209\u020f\n\6\2\2\u020a\u020b")
        buf.write("\7^\2\2\u020b\u020f\t\7\2\2\u020c\u020d\7^\2\2\u020d\u020f")
        buf.write("\7^\2\2\u020e\u0209\3\2\2\2\u020e\u020a\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2")
        buf.write("\u0210\u0211\3\2\2\2\u0211\u0213\3\2\2\2\u0212\u0210\3")
        buf.write("\2\2\2\u0213\u0214\5{>\2\u0214\u0215\b?\7\2\u0215~\3\2")
        buf.write("\2\2\u0216\u0217\t\b\2\2\u0217\u0080\3\2\2\2\u0218\u0219")
        buf.write("\t\t\2\2\u0219\u0082\3\2\2\2\u021a\u021b\7a\2\2\u021b")
        buf.write("\u0084\3\2\2\2\u021c\u021f\5\177@\2\u021d\u021f\5\u0083")
        buf.write("B\2\u021e\u021c\3\2\2\2\u021e\u021d\3\2\2\2\u021f\u0225")
        buf.write("\3\2\2\2\u0220\u0224\5\177@\2\u0221\u0224\5\u0083B\2\u0222")
        buf.write("\u0224\5\u0081A\2\u0223\u0220\3\2\2\2\u0223\u0221\3\2")
        buf.write("\2\2\u0223\u0222\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0223")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0086\3\2\2\2\u0227")
        buf.write("\u0225\3\2\2\2\u0228\u022a\t\n\2\2\u0229\u0228\3\2\2\2")
        buf.write("\u022a\u022b\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3")
        buf.write("\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\bD\2\2\u022e\u0088")
        buf.write("\3\2\2\2\u022f\u0230\13\2\2\2\u0230\u008a\3\2\2\2\u0231")
        buf.write("\u0232\13\2\2\2\u0232\u008c\3\2\2\2\u0233\u0234\13\2\2")
        buf.write("\2\u0234\u008e\3\2\2\2\24\2\u0153\u0161\u0182\u01ca\u01d0")
        buf.write("\u01d2\u01d7\u01dd\u01e1\u01f5\u0204\u020e\u0210\u021e")
        buf.write("\u0223\u0225\u022b\b\b\2\2\3\67\2\3:\3\3:\4\3:\5\3?\6")
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
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    FUNCKEYW = 20
    INHERIT = 21
    OUT = 22
    COMMA = 23
    COLON = 24
    SEMICOLON = 25
    EQUAL = 26
    OPENCMT = 27
    LINECMT = 28
    PLUSOP = 29
    MINUSOP = 30
    MULTIPLYOP = 31
    DIVIDEOP = 32
    MODULOOP = 33
    NEGATEOP = 34
    CONJUNCOP = 35
    DISJUNCOP = 36
    RELATIONALOP = 37
    STRINGCONCAT = 38
    LB = 39
    RB = 40
    LSQB = 41
    RSQB = 42
    LCB = 43
    RCB = 44
    CB = 45
    BOOLTYPE = 46
    INTTYPE = 47
    FLOATTYPE = 48
    STRINGTYPE = 49
    VOIDTYPE = 50
    AUTOTYPE = 51
    ARRAYTYPE = 52
    INTLIT = 53
    FLOATLIT = 54
    BOOLEANLIT = 55
    DOUBLEQUOTE = 56
    STRINGLIT = 57
    ID = 58
    WS = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'of'", "'readInteger'", "'readFloat'", "'readBoolean'", "'readString'", 
            "'if'", "'else'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
            "'return'", "'printInteger'", "'writeFloat'", "'printBoolean'", 
            "'printString'", "'super'", "'preventDefault'", "'function'", 
            "'inherit'", "'out'", "','", "':'", "';'", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'::'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'{}'", "'boolean'", "'integer'", 
            "'float'", "'string'", "'void'", "'auto'", "'array'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "FUNCKEYW", "INHERIT", "OUT", "COMMA", "COLON", "SEMICOLON", 
            "EQUAL", "OPENCMT", "LINECMT", "PLUSOP", "MINUSOP", "MULTIPLYOP", 
            "DIVIDEOP", "MODULOOP", "NEGATEOP", "CONJUNCOP", "DISJUNCOP", 
            "RELATIONALOP", "STRINGCONCAT", "LB", "RB", "LSQB", "RSQB", 
            "LCB", "RCB", "CB", "BOOLTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", 
            "VOIDTYPE", "AUTOTYPE", "ARRAYTYPE", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "DOUBLEQUOTE", "STRINGLIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "FUNCKEYW", 
                  "INHERIT", "OUT", "COMMA", "COLON", "SEMICOLON", "EQUAL", 
                  "OPENCMT", "LINECMT", "PLUSOP", "MINUSOP", "MULTIPLYOP", 
                  "DIVIDEOP", "MODULOOP", "NEGATEOP", "CONJUNCOP", "DISJUNCOP", 
                  "RELATIONALOP", "STRINGCONCAT", "LB", "RB", "LSQB", "RSQB", 
                  "LCB", "RCB", "CB", "BOOLTYPE", "INTTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "VOIDTYPE", "AUTOTYPE", "ARRAYTYPE", "NONZERODIGIT", 
                  "INTLIT", "DECIMAL", "EXP", "FLOATLIT", "TRUE", "FALSE", 
                  "BOOLEANLIT", "DOUBLEQUOTE", "STRINGLIT", "LETTER", "DIGIT", 
                  "UNDERSCORE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[53] = self.INTLIT_action 
            actions[56] = self.FLOATLIT_action 
            actions[61] = self.STRINGLIT_action 
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
     


