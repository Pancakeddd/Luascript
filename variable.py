import parser
pg = parser.pg

@pg.production("expression : variablenam equals expression")
def expression_varcreate(p):
    parser.appendtext("{0} = {1}".format(p[0].getstr(),p[2].eval()))

@pg.production("expression : private variablenam equals expression")
def expression_privarcreate(p):
    parser.appendtext("local "+varcreate(p[1].getstr(),p[3].eval()))
