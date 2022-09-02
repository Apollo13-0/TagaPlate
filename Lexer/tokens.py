import ply.lex as lex

# list of tokens names

tokens = {
    "NAME",
    "NUMBER",
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
    "REPEAT",
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

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_INT_DIVIDE = r'//'
t_DIVIDE = r'/'
t_MODULE = r'%'

# Assigment
t_EQUAL = r'=='

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
