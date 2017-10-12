import parser
import typed
pg = parser.pg

@pg.production("expression : class variablenam parenth leftbracket")
def expression_class(p):
    parser.appendtext("function __{0}new {1}".format(p[1].getstr(),p[2].getstr()[:-1]))
    parser.appendtext("local {0} = {{}}".format(p[1].getstr()))

@pg.production("expression : new variablenam parenth")
def expression_class(p):
    return typed.String("__{0}new{1}".format(p[1].getstr(),p[2].getstr()[:-1]))
