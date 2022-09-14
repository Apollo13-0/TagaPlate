import ply.yacc as yacc
import os
import codecs
import re
from Lexer.tokens import tokens


def p_symbols(p):
    '''
    symbol : New
    | Values
    | Alter
    | AlterB
    | Operator
    | MoveRight
    | MoveLeft
    | Hammer
    '''
    p[0] = p[1]


def p_expression_new(p):
    '''
    New : NEW NAME COMMA LPAREN NUM COMMA Num RPAREN
        | NEW NAME COMMA LPAREN BOOL COMMA Bool RPAREN
    '''
    p[0] = (p[2], p[5], p[7])
    print(p[0])


def p_expression_values(p):
    '''
    Values : VALUES LPAREN NAME COMMA Num RPAREN
           | VALUES LPAREN NAME COMMA Bool RPAREN
           | VALUES LPAREN NAME COMMA ALTER RPAREN
    '''
    p[0] = (p[3], p[5])
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


def p_expression_boolean(p):
    '''
    Bool : TRUE
         | FALSE
         | empty
    '''
    p[0] = p[1]


def p_expression_Alter(p):
    '''
    Alter : ALTER LPAREN NAME COMMA Operator COMMA Num RPAREN
    '''
    p[0] = (p[3], p[5], p[7])
    print(p[0])


def p_expression_operator(p):
    '''
    Operator : ADD
             | SUB
             | MUL
             | DIV
    '''
    p[0] = p[1]


def p_expression_AlterB(p):
    '''
    AlterB : ALTERB LPAREN NAME RPAREN
    '''
    p[0] = p[3]
    print(p[0])


def p_expression_moveR(p):
    '''
     MoveRight : MOVERIGHT
    '''
    p[0] = p[1]


def p_expression_moveL(p):
    '''
    MoveLeft : MOVELEFT
    '''
    p[0] = p[1]

def p_expression_hammer(p):
    '''
    Hammer : HAMMER LPAREN Position RPAREN
    '''
    p[0] = p[3]

def p_expression_position(p):
    '''
    Position : N
             | S
             | E
             | O
    '''
    p[0] = p[1]

def p_expression_stop(p):
    '''
    Stop : STOP
    '''
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
