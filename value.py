import typed
import parser
pg = parser.pg
@pg.production("expression : number")
def expression_number(p):
    return typed.Number(int(p[0].getstr()))

@pg.production("expression : string")
def expression_str(p):
    return typed.String(p[0].getstr())

@pg.production("expression : variablenam")
def expression_var(p):
    return typed.String(p[0].getstr())
