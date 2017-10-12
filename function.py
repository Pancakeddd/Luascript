import parser
pg = parser.pg

@pg.production("expression : variablenam parenth")
def expression_varcreate(p):
    parser.appendtext("{0}{1}".format(p[0].getstr(),p[1].getstr()[:-1]))

@pg.production("expression : def variablenam parenth leftbracket")
def expression_ifstate(p):
    parser.appendtext("function {0} {1}".format(p[1].getstr(),p[2].getstr()[:-1]))

@pg.production("expression : rightbracket")
def expression_varcreate(p):
    parser.appendtext("end")
