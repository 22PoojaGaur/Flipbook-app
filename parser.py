# author @22PoojaGaur

from rply import ParserGenerator
from ast import *
from lexer import Lexer

pg = ParserGenerator(
    ['NUMBER', 'DASH', 'FILENAME'],

    precedence=[
        ('left', ['DASH'])
    ]
)


@pg.production('expression : NUMBER')
def expression_number(p):
    return Number(p[0].getstr())


@pg.production('expression : expression DASH expression FILENAME')
def expression_range(p):
    left = p[0]
    right = p[2]

    # return RangeOp(left, right)
    return ' '.join([str(i) for i in RangeOp(left, right).eval()]) + FileName(p[3]).eval()


if __name__ == '__main__':
    lex = Lexer().lg.build()

    parser = pg.build()

    print(parser.parse(lex.lex('13-28 hello.png')))
