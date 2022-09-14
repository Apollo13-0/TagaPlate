import ply.lex as lex
import codecs

# list of tokens names
toks =[]
tokens = [
    "NAME",
    "INT", "FLOAT",

    # Reserved words
    "NEW",
    "PROC", "PRINCIPAL",
    "CALL", "NUM", "BOOL",
    "VALUES",
    "ALTER", "ADD", "SUB", "MUL", "DIV",
    "ALTERB",
    "MOVERIGHT", "MOVELEFT", "HAMMER", "STOP",
    "ISTRUE",
    "REPEAT", "BREAK",
    "UNTIL", "WHILE",
    "CASE", "WHEN", "ELSE",
    "PRINTVALUES",
    "TRUE",
    "FALSE",

    # Operators
    "PLUS",
    "MINUS",
    "TIMES",
    "INT_DIVIDE",
    "DIVIDE",
    "MODULE",


    # <, <=,  >, >=, ==, <>
    'LT', 'LE', 'GT', 'GE', "EQUAL", "NOT_EQUAL",

    # Assigment =
    "ASSING",

    # Bracket ( ) { } , . ; :

    "LPAREN", "RPAREN",
    "LBRACE", "RBRACE",
    "COMMA", "DOT",
    "SEMICOLON", "COLON",

]


# Regular expression rules for simple tokens

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        toks.append(str("Floaat value too large %d" + t.value))
        t.value = 0
    return t


def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        toks.append(str("Integer value too large %d" + t.value))
        t.value = 0
    return t
def t_NAME(t):
    r'@[A-Za-z_][A-Za-z0-9_]*'
    t.type = "NAME"
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    toks.append(str("Illegal character '%s'" % t.value[0]))
    t.lexer.skip(1)
def t_comment(t):
    r'\--.*'
    pass

def t_ccode_nonspace(t):
 r'\s+'
 pass

t_NEW = "New"
t_PROC = "Proc"
# PRINCIPAL
t_CALL = "CALL"
t_NUM = "Num"  # ver si se maneja enteros y/o floats
t_BOOL = "Bool"
t_VALUES = "Values"
t_ALTER = "Alter"
t_ADD = "ADD"
t_SUB = "SUB"
t_MUL = "MUL"
t_DIV = "DIV"
t_ALTERB = "AlterB"
t_MOVERIGHT = "MoveRight"
t_MOVELEFT = "MoveLeft"
t_HAMMER = "Hammer"
t_STOP = "Stop"
t_ISTRUE = "IsTrue"
t_REPEAT = "Repeat"
t_BREAK = "Break"
t_UNTIL = "Until"
t_WHILE = "While"
t_CASE = "Case"
t_WHEN = "When"
t_ELSE = "Else"
t_PRINTVALUES = "PrintValues"

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_INT_DIVIDE = r'\//'
t_DIVIDE = r'\/'
t_MODULE = r'%'

t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQUAL = r'=='
t_NOT_EQUAL = r'<>'

# Assigment
t_ASSING = r'='

# Bracket
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r"\,"
t_DOT = r"\."
t_SEMICOLON = r"\;"
t_COLON = r"\:"

t_ignore = " "

lexer = lex.lex()


def read_File(dir):
    fp = codecs.open(dir, "r", "utf-8")
    cadena = fp.read()
    fp.close()
    lexer.input(cadena)
    while True:
        tok = lexer.token()
        if not tok: break
        toks.append(str(tok))
    return toks
def cleartoks():
    toks.clear()