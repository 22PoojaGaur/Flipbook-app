# author @22PoojaGaur

from rply import ParserGenerator
from utils.ast import *
from utils.lexer import Lexer


class Parser:

    def __init__(self, pdf=None):
        self.pg = ParserGenerator(
            ['NUMBER', 'DASH', 'FILENAME'],

            precedence=[
                ('left', ['DASH'])
            ]
        )

        self.pdf = pdf

    def parse(self):
        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(p[0].value)

        @self.pg.production('expression : expression DASH expression FILENAME')
        def expression_range(p):
            left = p[0]
            right = p[2]

            im_range = RangeOp(left, right).eval()
            im_file = FileName(p[3].value).eval()

            for i in im_range:
                self.pdf.add_page()
                path = './imgs/' + im_file
                self.pdf.add_image(path, im_file.split('.')[1])

            return ' '.join([str(i) for i in RangeOp(left, right).eval()]) + FileName(p[3]).eval()

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()


if __name__ == '__main__':
    lex = Lexer().lg.build()

    tokens = lex.lex('13-28 hello.png')

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    print(parser.parse(tokens))
