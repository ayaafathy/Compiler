from rply import LexerGenerator
from tabulate import tabulate

class Lexer():

  def __init__(self):
    self.lexer = LexerGenerator()


  def _add_tokens(self):

    #Class
    self.lexer.add('Class', r'Pattern')

    #Inheritance
    self.lexer.add('Inheritance', r'DerivedFrom')

    #Condition
    self.lexer.add('Condition Statement', r'TrueFor')
    self.lexer.add('Else Statement', r'Else')

    #Integer
    self.lexer.add('Integer', r'Ity')

    #SInteger
    self.lexer.add('SInteger', r'Sity')

    #cWQ: Character ???
    self.lexer.add('Character', r'Cwq')

    #CwqSequence: String ???
    self.lexer.add('String', r'cwq[a-zA-Z]*')

    #Float
    self.lexer.add('Float', r'Ifity')

    #SFloat
    self.lexer.add('SFloat', r'Sifity')

    #Void
    self.lexer.add('Void', r'Valueless')

    #Boolean
    self.lexer.add('Boolean', r'Logical')

    #Break
    self.lexer.add('Break', r'BreakFromThis')

    #Loop
    self.lexer.add('Loop', r'Whatever')

    #Return
    self.lexer.add('Return', r'Respondwith')

    #Struct
    self.lexer.add('Struct', r'Srap')

    #Switch
    self.lexer.add('Switch scan', r'Scan')
    self.lexer.add('Switch Conditionof', r'Conditionof')

    #Stat Symbol
    self.lexer.add('Start Symbol', r'^\@')

    #End Symbol
    self.lexer.add('End Symbol', r'\$')

    #Arithmetic Operations
    self.lexer.add('Addition operator', r'\+')
    self.lexer.add('Subtraction operator', r'-')
    self.lexer.add('Multiplication operator', r'\*')
    self.lexer.add('Division operator', r'/')

    #Logic operators
    self.lexer.add('AND operator', r'&&')
    self.lexer.add('OR operator', r'\|\|')
    self.lexer.add('NOT operator', r'~')

    #Relational operators
    self.lexer.add('Equality operator', r'==')
    self.lexer.add('Less than operator', r'<')
    self.lexer.add('More than operator', r'>')
    self.lexer.add('Not equal operator', r'!=')
    self.lexer.add('Less than or equal operator', r'<=')
    self.lexer.add('More than or equal operator', r'>=')

    #Assignment operator
    self.lexer.add('Assignment operator', r'=')

    #Access Operator
    self.lexer.add('Access Operator', r'->')

    #Braces
    self.lexer.add('Left parenthesis', r'\{')
    self.lexer.add('Right parenthesis', r'\}')
    self.lexer.add('Left sq bracket', r'\[')
    self.lexer.add('Right sq bracket', r'\]')
    self.lexer.add('Left bracket', r'\(')
    self.lexer.add('Right bracket', r'\)')

    #Numbers
    self.lexer.add('Constant', r'\d+')

    #Quotation Marks
    self.lexer.add('Quotation Mark', r'"')
    self.lexer.add('Quotation Mark', r'\'')

    #Inclusion
    self.lexer.add('Require', r'Inclusion')

    #Comments
    self.lexer.add('Begin Comment', r'/-')
    self.lexer.add('End Comment', r'-/')
    self.lexer.add('single line Comment', r'--')

    #Token Delimiter
    self.lexer.add('Token Delimiter', r'#')

    #Line Delimiter
    self.lexer.add('Line Delimiter', r'\^')
    self.lexer.add('Line Delimiter', r'\.')

    #Identifier
    self.lexer.add('Identifier', r'_*[A-Za-z][A-Za-z0-9_]*')

   #Identifier Separator
    self.lexer.add('Identifier Separator', r',')

    #Ignore Spaces
    self.lexer.ignore('\s+')




  # Ignore Commented Lines
  def ignore_comments(text):
    for line in text:
      line = line.lstrip()
      if line.startswith('--'):
        continue
      yield (line)



  def error_handler(token):
    raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())



  def get_lexer(self):
    self._add_tokens()
    return self.lexer.build()





text = input("Enter String: ")
lexer = Lexer()

for token in lexer.get_lexer().lex(text):
  if(token in lexer.get_lexer().lex(text) != 0):
    Match = 'Matched'
  else:
    #lexer.error_handler(token)
    #lexer.getsourcepos()
    Match = 'Not Matched'


  table = [['Line NO','Lexeme','Return Token','Word NO in line','Matchability'],
          [token.source_pos.lineno, token.value, token.name, token.source_pos.colno, Match]]

  print(tabulate(table))
