import parser
pg = parser.pg
@pg.production("expression : if expression ioperator expression leftbracket")
def expression_ifstate(p):
    parser.appendtext("if {0} {1} {2} then".format(p[1].eval(),p[2].getstr(),p[3].eval()))

@pg.production("expression : if expression leftbracket")
def expression_ifstate(p):
    parser.appendtext("if {0} then".format(p[1].eval()))

@pg.production("expression : for variablenam expression expression leftbracket")
def expression_forstate(p):
    parser.appendtext("for {0} = {1},{2} do".format(p[1].getstr(),p[2].eval(),p[3].eval()))
