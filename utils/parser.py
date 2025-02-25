# author @22PoojaGaur

from rply import ParserGenerator
from utils.ast import *
from utils.lexer import Lexer


class Parser:

    def __init__(self, pdf=None):
        self.pg = ParserGenerator(
            ['NUMBER', 'DASH', 'CROSS', 'COMMA', 'FILENAME'],

            precedence=[
                ('left', ['DASH', 'CROSS', 'COMMA'])
            ]
        )

        self.pdf = pdf

    def parse(self):
        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(p[0].value)

        @self.pg.production('expression : NUMBER CROSS NUMBER')
        def expression_gridsize(p):
            dimensions = Grid(p[0], p[2]).eval() # set and return grid size
            self.pdf.set_grid_dims(dimensions)
            return dimensions

        @self.pg.production('gridpos : NUMBER COMMA NUMBER')
        def expression_grid_position(p):
            position = GridPos(p[0], p[2]).eval()
            return position

        @self.pg.production('imrange : NUMBER DASH NUMBER')
        def expression_range(p):
            left = p[0]
            right = p[2]

            return RangeOp(left, right).eval()

        @self.pg.production('imrange : NUMBER')
        def expression_single_range(p):
            return [Number(p[0].value).eval()]

        @self.pg.production('expression : imrange FILENAME gridpos gridpos')
        def expression_image_with_pos(p):
            # left = p[0]
            # right = p[2]

            # im_range = RangeOp(left, right).eval()
            im_range = p[0]
            im_file = FileName(p[1].value).eval()

            start = p[2]
            end = p[3]

            for i in im_range:
                if i not in self.pdf.pdf_img_map.keys():
                    self.pdf.pdf_img_map[i] = []

                self.pdf.pdf_img_map[i].append((im_file, start, end))

            #print(self.pdf.pdf_img_map)

            return 'position image expression'

        @self.pg.production('expression : imrange FILENAME')
        def expression_range(p):
            # left = p[0]
            # right = p[2]
            #
            # im_range = RangeOp(left, right).eval()
            im_range = p[0]
            im_file = FileName(p[1].value).eval()

            for i in im_range:
                if i not in self.pdf.pdf_img_map.keys():
                    self.pdf.pdf_img_map[i] = []

                self.pdf.pdf_img_map[i].append((im_file, None, None))

            return ' '.join([str(i) for i in RangeOp(left, right).eval()]) + FileName(p[1]).eval()

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()


if __name__ == '__main__':
    lex = Lexer().lg.build()

    # tokens = lex.lex('13-28 hello.png')
    tokens = lex.lex('4 X 4')

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    print(parser.parse(tokens))
