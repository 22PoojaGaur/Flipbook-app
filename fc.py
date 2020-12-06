# author @22PoojaGaur

import argparse

from utils.generators import MyPDF
from utils.lexer import Lexer
from utils.parser import Parser


class ArgParse:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('--outputfile', help='name of output file')
        self.parser.add_argument('--program', help='name of the flip program file')


class Args:
    pass


if __name__ == '__main__':

    args = Args()
    parse_args = ArgParse().parser.parse_args(namespace=args)

    if args.outputfile is not None:
        print('output file name is ', args.outputfile)

        out_filename = str(args.outputfile)
        extn = out_filename.split('.')[1]

        pfile = open(args.program, 'r')

        if extn == 'pdf':  # generate pdf
            pdf = MyPDF()

            lex = Lexer().lg.build()
            pg = Parser(pdf=pdf)
            pg.parse()
            parse = pg.get_parser()

            for cmd in pfile.readlines():
                print(parse.parse(lex.lex(cmd)))

            pdf.pdf.output(out_filename, 'F')

        elif extn == 'gif':
            pass  # generate gif
