from scanner import Lexer


text = input("Enter String: ")

lexer = Lexer().get_lexer()
tokens = lexer.lex(text)


"""
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
"""