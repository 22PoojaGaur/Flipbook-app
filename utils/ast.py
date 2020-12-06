# author @22PoojaGaur

from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class FileName(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)


class RangeOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return [i for i in range(self.left.eval(), self.right.eval()+1)]
