##########################
# Parser                 #
# Author: Liam M. Murphy #
##########################

from stages import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse_tokens(self):
        for token in self.tokens:
            if token.type == 'BEGIN':
                return ()






def run(tokens):
    parser = Parser(tokens)
    for token in parser.tokens:
        print(token)