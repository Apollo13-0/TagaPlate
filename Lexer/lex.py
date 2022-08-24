import ply.lex as lex

# list of tokens names

tokens = {
    "NAME",
    "NUMBER",
    "STRING",

    # Reserved words
    "NEW",
    "IF",
    "ELSE",
    "FOR",
    "TO",
    "STEP",
    "SET",
    "PRINT",
    "DEF",
    "NUM",
    "BOOL",

    # Operators
    "PLUS",
    "MINUS",
    "TIMES",
    "INT_DIVIDE",
    "DIVIDE",
    "MODULE",
    "EQUAL",
    "NOT_EQUAL"

    # Assigment
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
t_DIVIDE = r'/'
t_INT_DIVIDE = r'//'
t_MODULE = r'%'
t_EQUAL = r'=='
t_LPAREN = r'\('
t_RPAREN = r'\)'
