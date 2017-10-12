from rply.token import BaseBox

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class String(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

def returntype(val):
    if(type(val) == int):
        return Number(val)
    else:
        return None
