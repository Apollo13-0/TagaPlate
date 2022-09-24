from ast import operator
import codecs
from operator import truediv
from AST_INS.AstClass import *
from Lexer.tokens import *
import Parser.parser as pars
import os

global code
code = ""


def Principal_appear(Instructions):
    for i in Instructions:
        if type(i) == Principal:
            return True
        else:
            return False


def proc_defined(i):
    pass


def New_defined(i):
    global code
    name = i.NAME[1:]
    code += "\t" + name + i.Type + "=" + i.Data + "\n"


def Values_defined(i):
    global code
    name = i.NAME[1:]
    code += "\t" + name + "=" + i.Data + "\n"


def Alter_defined(i):
    global code
    name = i.NAME[1:]
    code += "\t" + name + i.Operator + "= " + i.Num + "\n"


def AlterB_defined(i):
    global code
    name = i.NAME[1:]
    code += "\t" + name + "= " + "not " + name + "\n"


def While_defined(i):
    pass


def Repeat_defined(i):
    pass


def Until_defined(i):
    pass


def PrintValues_defined(i):
    pass


def MoveRight_defined(i):
    global code
    code += "\tself.sock.send(b'a')"


def MoveLeft_defined(i):
    global code
    code += "\tself.sock.send(b'b')"


def Stop_defined(i):
    global code
    code += "\tpass"


def Hammer_defined(i):
    global code
    pos = i.Poss
    if pos == 'N':
        code += "\tself.sock.send(b'f')"
    elif pos == 'S':
        code += "\tself.sock.send(b'e')"
    if pos == 'E':
        code += "\tself.sock.send(b'd')"
    elif pos == 'O':
        code += "\tself.sock.send(b'c')"


def CaseWhen_defined(i):
    pass


def Case_defined(i):
    pass


def IsTrue_defined(i):
    pass


def WhenValue_defined(i):
    pass


def declaration(i):
    global code
    Name = i.NAME[1:]
    code += "\t" + Name


def Proc_instructions(Instructions):
    global code
    code += "def principal():\n"

    for i in Instructions:
        if isinstance(i, Procs):
            proc_defined(i)
        elif isinstance(i, New):
            New_defined(i)
        elif isinstance(i, Values):
            Values_defined(i)
        elif isinstance(i, Alter):
            Alter_defined(i)
        elif isinstance(i, AlterB):
            AlterB_defined(i)
        elif isinstance(i, While):
            While_defined(i)
        elif isinstance(i, Repeat):
            Repeat_defined(i)
        elif isinstance(i, Until):
            Until_defined(i)
        elif isinstance(i, PrintValues):
            PrintValues_defined(i)
        elif isinstance(i, MoveRight):
            MoveRight_defined(i)
        elif isinstance(i, MoveLeft):
            MoveLeft_defined(i)
        elif isinstance(i, Stop):
            Stop_defined(i)
        elif isinstance(i, Hammer):
            Hammer_defined(i)
        elif isinstance(i, CaseWhen):
            CaseWhen_defined(i)
        elif isinstance(i, Case):
            Case_defined(i)
        elif isinstance(i, IsTrue):
            IsTrue_defined(i)
        elif isinstance(i, WhenValue):
            WhenValue_defined(i)
        else:
            declaration(i)


def compile_e(file):
    global code
    fp = codecs.open(file)
    cadena = fp.read()
    fp.close()
    Principal_appear(pars.parse_dir(file))
    Proc_instructions(pars.parse_dir(file))
    file = open("Code.txt")
    print(code)
    file.close()
