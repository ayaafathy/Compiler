import sys

from scanner import Lexer
from my_parser import Parser, pg

text = input("Enter String: ")

lexer = Lexer().get_lexer()
tokens = lexer.lex(text)


print('Enter the array:')
userInput = sys.stdin.readlines()
print(userInput)


parser = pg.get_parser()
parser.parse.eval()