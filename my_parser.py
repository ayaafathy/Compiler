import sys
from _ast import operator, Mult, Div
from rply import ParserGenerator
from tabulate import tabulate
from ast import Number, Sum, Print, Boolean, Sub


class Parser():
  def __init__(self):
    self.pg = ParserGenerator(
      ['Class', 'Inheritance', 'Condition Statement''Else Statement', 'Integer', 'SInteger',
       'Character', 'String', 'Float', 'SFloat', 'Void', 'Boolean',
       'Break', 'Loop', 'Return', 'Struct', 'Switch scan', 'Switch Conditionof', 'Start Symbol', 'End Symbol',
       'Addition operator', 'Subtraction operator', 'Multiplication operator', 'Division operator',
       'AND operator', 'OR operator', 'NOT operator', 'Equality operator', 'Less than operator',
       'More than operator', 'Modulus', 'SEMI_COLON',
       'Not equal operator', 'Less than or equal operator', 'More than or equal operator', 'Assignment operator',
       'Access Operator', 'Left parenthesis', 'Right parenthesis', 'Left sq bracket', 'Right sq bracket',
       'Left bracket', 'Right bracket', 'Constant', 'Quotation Mark', 'Require', 'Begin Comment', 'End Comment',
       'single line Comment', 'Token Delimiter', 'Line Delimiter', 'Identifier', 'Identifier Separator']
    )

  @property
  def parse(self):
    # 1

    @self.pg.production('Program : Start-Symbols Left parenthesis Comment Line Delimiter Program ')
    def program(p):
      return print('program used')

    @self.pg.production('Program : Require_command Line Delimiter Program')
    def program(p):
      return 1

    @self.pg.production(
      'Program : AccessModifiers-Type Token Delimiter id Left parenthesis field-decl Line Delimiter method-decl Right parenthesis Right parenthesis End-Symbols')
    def program(p):
      return 1

    # 2
    @self.pg.production('Start-Symbols : Start Symbol')
    def Start(p):
      return (p[0].value)

    # 3
    @self.pg.production('End-Symbols : End Symbol')
    def End(p):
      return (p[0].value)

    # 4

    @self.pg.production(
      'AccessModifiers-Type: public OR operation  Private single line Comment addto scanner ')
    def AccessModifiers(p):
      return 4

    # 5
    @self.pg.production(
      'field-decl : type Token Delimiter id Identifier Separator field-decl OR operator type Token Delimiter id Left sq bracket Integer Right sq bracket OR operator type Token Delimiter id Equality operator Constant OR operator type Token Delimiter id ')
    def Condition(p):
      return 5

    # 6

    @self.pg.production(
      'method-decl : type Token Delimiter id Left bracket field-decl OR operator em Right bracket block ')
    def Loop(p):
      return 6

    # 7
    @self.pg.production(
      'block : Left parenthesis var-decl Line Delimiter statement Right parenthesis ')
    def block(p):
      return 7

    # 8
    @self.pg.production(
      'var-decl : var Subtraction Operator decl Identifier Separator type Token Delimiter id OR operator type Token Delimiter id ')
    def var(p):
      return 8

    # 9

    @self.pg.production(
      'type : Integer OR operator SInteger OR operator String OR operator Float OR operator SFloat OR operator Void OR operator Boolean ')
    def type(p):
      return 9

    # 10

    @self.pg.production(
      'statement : assign Line Delimiter OR operation method-call Line Delimiter OR operation Condition-Stmt Line Delimiter OR operator Loop-Stmt Line Delimiter Return-Stmt')
    def statement(p):
      return 10

    # 11
    @self.pg.production(
      'assign: L-value Assignment operator expr Line Delimiter')
    def assign(p):
      return 11

    # 12
    @self.pg.production('< l-value>: id OR operation id Left sq bracket expr Right sq bracket')
    def value(p):
      return 12

    # 13
    @self.pg.production('method-call: id Left bracket method-arg Right bracket Line Delimiter ')
    def methodCall(p):
      return 13

    # 14
    @self.pg.production('method-arg:expr OR operator em')
    def methodArg(p):
      return 14

    # 15
    @self.pg.production('TrueFor-Stmt: Condition Statement Left bracket expr Right bracket Statement Else Statement')
    def true(p):
      return 15

    # 16
    @self.pg.production('Whatever-Stmt: Loop Left bracket expr Right bracket Statement')
    def whatever(p):
      return 16

    # 17
    @self.pg.production('Respondwith-Stmt: BackedValue Token Delimiter Expression Line Delimiter')
    def Respondwith(p):
      return 17

    @self.pg.production('Respondwith-Stmt: BackedValue Token Delimiter ID Line Delimiter')
    def Respondwith(p):
      return 17

    # 18
    @self.pg.production('terminatethis_Statement: TerminateThisNow SEMI_COLON')
    def terminatethis(p):
      return 18

    # 19
    @self.pg.production(
      'expr: id Left sq bracket expr Right sq bracket OR operator method-call OR operator constant OR operator expr bin-op expr OR operator Left bracket expr Right bracket')
    def expr(p):
      return 19

    # 20
    @self.pg.production('bin-op: arith-op OR operator rel-op OR operator eq-op OR operator cond-op')
    def bin(p):
      return 20

    # 21
    @self.pg.production(
      'arith-op : Addition operator OR operator Subtraction operator OR operator Multiplication operator OR operator Division operator OR operator modulus ')
    def arith(p):

      operator = p[0]
      if operator.gettokentype() == 'Addition operator':
        return Sum()
      elif operator.gettokentype() == 'Subtraction operator':
        return Sub()
      elif operator.gettokentype() == 'Multiplication operator':
        return Mult()
      else:
        return Div()

    # 22
    @self.pg.production('rel-op : Less than operator')
    def rel(p):
      return Print(p[0])

    @self.pg.production('rel-op : More than operator')
    def rel(p):
      return Print(p[0])

    @self.pg.production('rel-op : Less than or equal operator')
    def rel(p):
      return Print(p[0])

    @self.pg.production('rel-op : More than or equal operator')
    def rel(p):
      return Print(p[0])

    # 23
    @self.pg.production('eq-op : Equality operator')
    def eq(p):
      return Print(p[0])

    @self.pg.production('eq-op : Not equal operator')
    def eq(p):
      return Print(p[0])

    # 24
    @self.pg.production('cond-op : AND operator')
    def cond(p):
      return Print(p[0])

    @self.pg.production('cond-op : OR operator')
    def cond(p):
      return Print(p[0])

    # 25
    @self.pg.production('constant: Integer Constant')
    def constant(p):
      return Print(p[0])

    # 26
    @self.pg.production('bool-constant: true OR operation false')
    def boolconstant(p):

      return Boolean()

    # 27

    @self.pg.production('require_command: require Left bracket F_name Line Delimiter string')
    def require(p):
      return Print(p[3])

    # 28

    @self.pg.production('F_name : String ')
    def fname(p):
      return Print(p[0])

    # 29

    @self.pg.production('Comment : String ')
    def Comment(p):
      return Print(p[0])

    @self.pg.error
    def error_handle(token):
      raise ValueError(token)

    return

  def get_parser(self):
    return self.pg.build()



print('Enter the array:')
userInput = sys.stdin.readlines()
print(userInput)

my_parser = Parser()

for pg in my_parser.get_parser().parser.parse.eval():
  if (pg in my_parser.get_parser().parser.parse.eval() != 0):
    Match = 'Matched'
  else:
    # lexer.error_handler(token)
    # lexer.getsourcepos()
    Match = 'Not Matched'

  table = [['Line NO', 'Matchability', 'Rule Used'],
           [pg.parse.eval(), Match, pg.get_parser()]]

  print(tabulate(table))
