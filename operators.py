import parser
import typed
pg = parser.pg

@pg.production("expression : expression add add")
def expression_inc(p):
    parser.appendtext("{0} = {0} + 1".format(p[0].eval()))

@pg.production("expression : expression sub sub")
def expression_dec(p):
    parser.appendtext("{0} = {0} - 1".format(p[0].eval()))
