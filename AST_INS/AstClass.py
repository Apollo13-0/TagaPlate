class Instructions():
    '''Instruccions class'''


class Procs(Instructions):
    def __init__(self, NAME, instructions):
        self.NAME = NAME
        self.instructions = instructions


class Principal(Instructions):
    def __init__(self, instruccions):
        self.NAME = "@Principal"
        self.instructions = instruccions


class New(Instructions):
    def __init__(self, NAME, Type, Data):
        self.NAME = NAME
        self.Type = Type
        self.Data = Data

class Values(Instructions):
    def __init__(self, NAME, data):
        self.NAME = NAME
        self.Data = data


class While(Instructions):
    def __init__(self, Bool, instructions):
        self.Bool = Bool
        self.instructions = instructions


class Repeat(Instructions):
    def __init__(self, instructions):
        self.instructions = instructions


class Until(Instructions):
    def __init__(self, instructions, Bool):
        self.instructions = instructions
        self.Bool = Bool


class PrintValues(Instructions):
    def __init__(self, String):
        self.String = String


class Alter(Instructions):
    def __init__(self, NAME, Operator, Num):
        self.NAME = NAME
        self.Operator = Operator
        self.Num = Num


class AlterB(Instructions):
    def __init__(self, Name):
        self.NAME = Name


class MoveRight(Instructions):
    def __init__(self):
        self.Move = 180


class MoveLeft(Instructions):
    def __init__(self):
        self.Move = -180


class Stop(Instructions):
    pass


class Hammer(Instructions):
    def __init__(self, poss):
        self.Poss = poss


class CaseWhen(Instructions):
    def __init__(self, Bool, intructions):
        self.Bool = Bool
        self.instructions = intructions


class Case(Instructions):
    def __init__(self, Name, instructions):
        self.NAME = Name
        self.instructions = instructions


class IsTrue(Instructions):
    def __init__(self, NAME):
        self.NAME = NAME


class WhenValue(Instructions):
    def __init__(self, type, Instructions):
        self.Type = type
        self.Instructions = Instructions
