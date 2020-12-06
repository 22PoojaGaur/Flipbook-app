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


def start(program_name, out_filename):
    fname = out_filename.split('.')[0]
    extn = out_filename.split('.')[1]

    pfile = open(program_name, 'r')

    pdf = MyPDF()

    lex = Lexer().lg.build()
    pg = Parser(pdf=pdf)
    pg.parse()
    parse = pg.get_parser()

    for cmd in pfile.readlines():
        print(parse.parse(lex.lex(cmd)))

    pdf.print_to_pdf()

    pdf.pdf.output(str(fname) + ".pdf", 'F')

    if extn == 'gif':
        import os
        command = "convert -alpha remove -verbose -delay 20 " + str(fname) + ".pdf " + str(fname) + ".gif"
        os.system(command)


if __name__ == '__main__':

    args = Args()
    parse_args = ArgParse().parser.parse_args(namespace=args)

    if args.outputfile is None:
        raise ValueError('Output file name required')

    start(args.program, args.outputfile)
