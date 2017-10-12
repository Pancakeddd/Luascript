from rply import LexerGenerator

lg = LexerGenerator()


lg.add('number', r'\-?[0-9]+')
lg.add('add', r'\+')
lg.add('sub', r'\-')
lg.add('ioperator', r'(==|\>=|\<=|\!=|>|<)')
lg.add('equals', r'\=')
lg.add('private', r'local')
lg.add('if', r'if')
lg.add('for', r'for')
lg.add('def', r'def')
lg.add('class', r'class')
lg.add('new', r'new')
lg.add('leftbracket', r'\{')
lg.add('rightbracket', r'\}')
lg.add('end', r'end')
lg.add('parenth', r'\(.*?(\)|\s)+')
lg.add('variablenam', r'[A-Za-z0-9_.:]+')
lg.add('string', r'".+"')
lg.ignore(r'\s+')

l = lg.build()
