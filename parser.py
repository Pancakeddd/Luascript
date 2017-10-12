import lexer as lexr
from rply import ParserGenerator

#lexed = lex.parsetext("string = 1


pg = ParserGenerator(
    ['number','string','char',
    'add','sub','mul','div','mod','equals',
    'private','variablenam','parenth','class','new',
    'if','for','end','def','ioperator',
    'leftbracket','rightbracket'
    ]
)

finishtext = ""
def appendtext(text):
    global finishtext
    finishtext = finishtext + text
    finishtext = finishtext + "\n"
def gettext():
    return finishtext

@pg.error
def error_handler(token):
    raise ValueError("Error %s Unexpected" % token.gettokentype())

def parsetxt(text):
    parser.parse(lexr.l.lex(text))

def createfile(name):
    fileout = open(name,"w")
    fileout.write(finishtext)
