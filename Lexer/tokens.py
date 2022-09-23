import ply.lex as lex
import codecs

# list of tokens names
toks = []
errors = []
tokens = [
    "NAME",
    "INT", "FLOAT","STRING",

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
    "CASE", "WHEN", "ELSE", "CASE_WHEN", "THEN",
    "PRINTVALUES",
    "TRUE",
    "FALSE",
    "OPERATOR",
    "N", "S", "E", "O",
    "POSITION",
    "INSTRUCTIONS",
    "CONCATENATION",

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

    # Bracket ( ) { } , . ; : [ ]

    "LPAREN", "RPAREN",
    "LBRACE", "RBRACE",
    "COMMA", "DOT",
    "SEMICOLON", "COLON",
    "LBRACKET", "RBRACKET"

]


# Regular expression rules for simple tokens

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        toks.append(str("Float value too large %d" + t.value))
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


def t_STRING(t):
    r'"[A-Za-z_][A-Za-z0-9_]*"'
    t.type = "STRING"
    return t


def t_error(t):
    errors.append(str("Illegal input '%s'" % t.value))
    t.lexer.skip(len(t.value))


def t_comment(t):
    r'\--.*'
    pass


def t_ccode_nonspace(t):
    r'\s+'
    pass


t_NEW = "New"
t_PROC = "Proc"
t_PRINCIPAL = "@Principal"
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
t_THEN = "Then"
t_CASE_WHEN = "Case_When"
t_ELSE = "Else"
t_PRINTVALUES = "PrintValues"
t_FALSE = "False"
t_TRUE = "True"
t_OPERATOR = "Operator"
t_N = "N"
t_S = "S"
t_O = "O"
t_E = "E"
t_POSITION = "Position"
t_INSTRUCTIONS = "Instructions"
t_CONCATENATION = "Concatenation"


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
t_LBRACKET = r"\["
t_RBRACKET = r"\]"

t_ignore = " "

lexer = lex.lex()


def read_File(dir):
    fp = codecs.open(dir, "r", "utf-8")
    cadena = fp.read()
    fp.close()
    lexer.input(cadena)
    while True:
        tok = lexer.token()
        if not tok:
            break
        toks.append(str(tok))
    return errors


def cleartoks():
    errors.clear()
    toks.clear()
