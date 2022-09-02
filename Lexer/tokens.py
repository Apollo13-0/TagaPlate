import ply.lex as lex

# list of tokens names

tokens = {
    "NAME",
    "INT", "FLOAT",
    "STRING",

    # Reserved words
    "NEW",
    "PROC", "PRINCIPAL",
    "CALL", "NUM", "BOOL",
    "VALUES",
    "ALTER", "ADD", "SUB", "MUL", "DIV",
    "ALTERB",
    "MOVERIGHT", "MOVELEFT", "HAMMER", "STOP",
    "ISTRUE",
    "REPEAT", "BREAK"
    "UNTIL", "WHILE",
    "CASE", "WHEN", "ELSE",
    "PRINTVALUES",


    # Operators
    "PLUS",
    "MINUS",
    "TIMES",
    "INT_DIVIDE",
    "DIVIDE",
    "MODULE",

    # <, <=,  >, >=, ==, <>
    'LT', 'LE', 'GT', 'GE', "EQUAL", "NOT_EQUAL"

    # Assigment =
    "ASSING",

    # Bracket ( ) { } , . ; :

    "LPAREN", "RPAREN",
    "LBRACE", "RBRACE",
    "COMMA", "DOT",
    "SEMICOLON", "COLON"

}

# Regular expression rules for simple tokens

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\d+'
    try:
        t.value = str(t.value)
    except ValueError:
        print("String value too large %d", t.value)
        t.value = 0
    return t

t_NEW = r"\New"
t_PROC = r"\Proc"
# PRINCIPAL
t_CALL = r"\CALL"
t_NUM = r"\Num"  # ver si se maneja enteros y/o floats
t_BOOL = r"\Bool"
t_VALUES = r"\Values"
t_ALTER = r"\Alter"
t_ADD = r"\ADD"
t_SUB = r"\SUB"
t_MUL = r"\MUL"
t_DIV = r"\DIV"
t_ALTERB = r"\AlterB"
t_MOVERIGHT = r"\MoveRight"
t_MOVELEFT = r"\MoveLeft"
t_HAMMER = r"\Hammer"
t_STOP = r"\Stop"
t_ISTRUE = r"\IsTrue"
t_REPEAT = r"\Repeat"
t_BREAK = r"\Break"
t_UNTIL = r"\Until"
t_WHILE = r"\While"
t_CASE = r"\Case"
t_WHEN = r"\When"
t_ELSE = r"\Else"
t_PRINTVALUES = r"\PrintValues"

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_INT_DIVIDE = r'//'
t_DIVIDE = r'/'
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


t_ignore = ' \t'
