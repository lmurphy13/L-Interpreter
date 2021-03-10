#########################################
# Classes for the Abstract Syntaxt Tree #
# By Liam M. Murphy                     #
#########################################

class Program:
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'(Program({self.content}))'

class Expression:
    def __init__(self, children):
        self.type
        self.children

    def __repr__(self):
        return f'({self.type}({self.children}))'

class BinaryOpExpr(Expression):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def __repr__(self):
        return f'(BinaryOpExpr({self.lhs}, {self.op}, {self.rhs}))'