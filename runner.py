from stages import lexer
from stages import parser
import sys

program = ''

with open (sys.argv[1], 'r') as f:
    for line in f:
        program += line

parser.run((lexer.run(program)))
