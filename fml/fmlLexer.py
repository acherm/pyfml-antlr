# Generated from fml.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("[\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\7\20P\n\20\f\20\16\20S\13\20\3\21\6\21V\n\21\r\21")
        buf.write("\16\21W\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2")
        buf.write("\5\4\2C\\c|\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2\\\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5&\3\2")
        buf.write("\2\2\7\63\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2\r:\3\2\2")
        buf.write("\2\17=\3\2\2\2\21?\3\2\2\2\23A\3\2\2\2\25C\3\2\2\2\27")
        buf.write("E\3\2\2\2\31G\3\2\2\2\33I\3\2\2\2\35K\3\2\2\2\37M\3\2")
        buf.write("\2\2!U\3\2\2\2#$\7H\2\2$%\7O\2\2%\4\3\2\2\2&\'\7h\2\2")
        buf.write("\'(\7g\2\2()\7c\2\2)*\7v\2\2*+\7w\2\2+,\7t\2\2,-\7g\2")
        buf.write("\2-.\7o\2\2./\7q\2\2/\60\7f\2\2\60\61\7g\2\2\61\62\7n")
        buf.write("\2\2\62\6\3\2\2\2\63\64\7=\2\2\64\b\3\2\2\2\65\66\7<\2")
        buf.write("\2\66\n\3\2\2\2\678\7+\2\289\7A\2\29\f\3\2\2\2:;\7/\2")
        buf.write("\2;<\7@\2\2<\16\3\2\2\2=>\7(\2\2>\20\3\2\2\2?@\7}\2\2")
        buf.write("@\22\3\2\2\2AB\7]\2\2B\24\3\2\2\2CD\7_\2\2D\26\3\2\2\2")
        buf.write("EF\7*\2\2F\30\3\2\2\2GH\7+\2\2H\32\3\2\2\2IJ\7~\2\2J\34")
        buf.write("\3\2\2\2KL\7-\2\2L\36\3\2\2\2MQ\t\2\2\2NP\t\3\2\2ON\3")
        buf.write("\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R \3\2\2\2SQ\3\2\2")
        buf.write("\2TV\t\4\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X")
        buf.write("Y\3\2\2\2YZ\b\21\2\2Z\"\3\2\2\2\5\2QW\3\b\2\2")
        return buf.getvalue()


class fmlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    LCURLY = 8
    LEFT_HOOK = 9
    RIGHT_HOOK = 10
    LEFT_PAREN = 11
    RIGHT_PAREN = 12
    B_OR = 13
    PLUS = 14
    FT_ID = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'FM'", "'featuremodel'", "';'", "':'", "')?'", "'->'", "'&'", 
            "'{'", "'['", "']'", "'('", "')'", "'|'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "LCURLY", "LEFT_HOOK", "RIGHT_HOOK", "LEFT_PAREN", "RIGHT_PAREN", 
            "B_OR", "PLUS", "FT_ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "LCURLY", "LEFT_HOOK", "RIGHT_HOOK", "LEFT_PAREN", "RIGHT_PAREN", 
                  "B_OR", "PLUS", "FT_ID", "WS" ]

    grammarFileName = "fml.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


