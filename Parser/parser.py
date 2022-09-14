import ply.yacc as yacc
import os
import codecs
import re
from Lexer.tokens import tokens

def p_expression_new(p):
    '''
    New : NEW NAME COMMA LPAREN Values RPAREN
    '''
    p[0] = (p[2], p[5])
    print(p[0])

def p_expression_Num(p):
    '''
    Num : INT
        | FLOAT
    '''
    p[0] = p[1]
    print(p[1])


def p_expression_Plus(p):
    '''
    Num : Num PLUS Num
    '''
    p[0] = (p[2], p[1], p[3])
    print(p[0])


def p_expression_values(p):
    '''
    Values : Num
           | BOOL
    '''
    p[0] = p[1]


def p_expression_Alter(p):
    '''
    Alter : Num ADD Num
          | Num SUB Num
          | Num MUL Num
          | Num DIV Num
    '''
    p[0] = (p[1], p[2], p[3])


def p_expression_AlterB(p):
    '''
    AlterB : BOOL
    '''
    p[0] = p[1]


def p_calc(p):
    '''

    calc : Values
        | empty
    '''
    print(p[1])
    p[0] = p[1]


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
