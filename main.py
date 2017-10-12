import parser
import operators
import variable
import function
import ifp
import value
import classp

parser.parser = parser.pg.build()
def runfile(filename):
    with open(filename) as fp:
        for line in fp:
            if ord(line[0]) != 10:
                parser.parsetxt(line)
runfile('test.gs')
parser.createfile('dingle.lua')
