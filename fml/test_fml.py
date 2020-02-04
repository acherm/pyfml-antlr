import sys
from antlr4 import *
from fmlLexer import fmlLexer
from fmlParser import fmlParser


def main(argv):
    input = FileStream(argv[1])
    lexer = fmlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = fmlParser(stream)
    tree = parser.featuremodel()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
