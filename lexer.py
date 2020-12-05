# author @22PoojaGaur
from tokens import Tokens

from rply import LexerGenerator


class Lexer:

    def __init__(self):
        self.lg = LexerGenerator()

        self.add_tokens()

    def add_tokens(self):
        for (token, regex) in Tokens.items():
            self.lg.add(token, regex)

        # ignore spaces
        self.lg.ignore(r'\s+')


if __name__ == '__main__':
    lexer = Lexer().lg.build()

    for token in lexer.lex('01-05 myfile.jpeg'):
        print(token)
