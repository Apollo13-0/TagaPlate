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
           | IsTrue
           | Stop
           | Repeat
           | Num
           | PrintValues
           | Instructions
           | Position
           | While
           | Until
           | Case
           | Case_When
    '''
    p[0] = p[1]


def p_expression_new(p):
    '''
    New : NEW NAME COMMA LPAREN NUM COMMA Num RPAREN
        | NEW NAME COMMA LPAREN BOOL COMMA Bool RPAREN
    '''
    p[0] = (p[1], p[2], p[5], p[7])
    print(p[0])


def p_expression_values(p):
    '''
    Values : VALUES LPAREN NAME COMMA Num RPAREN
           | VALUES LPAREN NAME COMMA Bool RPAREN
           | VALUES LPAREN NAME COMMA ALTER RPAREN
    '''
    p[0] = (p[1], p[3], p[5])
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
        | Num MINUS Num
        | Num TIMES Num
        | Num DIVIDE Num
        | Num MODULE Num
    '''
    p[0] = (p[2], p[1], p[3])
    print(p[0])


def p_expression_boolean(p):
    '''
    Bool : TRUE
         | FALSE
    '''
    p[0] = p[1]

def p_another_boolean(p):
    '''
    Bool : Num LT Num
         | Num GT Num
         | Num LE Num
         | Num GE Num
         | Num EQUAL Num
         | Num NOT_EQUAL Num
         | NAME LT Num
         | NAME GT Num
         | NAME LE Num
         | NAME GE Num
         | NAME EQUAL Num
         | NAME NOT_EQUAL Num
         | NAME LT NAME
         | NAME GT NAME
         | NAME LE NAME
         | NAME GE NAME
         | NAME EQUAL NAME
         | NAME NOT_EQUAL NAME
    '''
    p[0] = (p[1], p[2], p[3])

def p_expression_Alter(p):
    '''
    Alter : ALTER LPAREN NAME COMMA Operator COMMA Num RPAREN
    '''
    p[0] = (p[1], p[3], p[5], p[7])
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
    p[0] = (p[1], p[3])
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
    p[0] = (p[1], p[3])


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


def p_expression_isTrue(p):
    '''
    IsTrue : ISTRUE LPAREN NAME RPAREN
    '''
    p[0] = (p[1], p[3])
    print(p[0])


def p_expression_repeat(p):
    '''
    Repeat : REPEAT LPAREN Instructions BREAK RPAREN
    '''
    p[0] = (p[1], p[3])
    print(p[0])


def p_expression_until(p):
    '''
    Until : UNTIL LPAREN Instructions RPAREN Bool
    '''
    p[0] = (p[1], p[3], p[5])
    print(p[0])


def p_expression_while(p):
    '''
    While : WHILE Bool LPAREN Instructions RPAREN
    '''
    p[0] = (p[1], p[2], p[4])
    print(p[0])


def p_expression_caseWhen(p):
    '''
    Case_When : CASE WHEN LPAREN Bool RPAREN THEN LPAREN Instructions RPAREN LBRACKET ELSE LPAREN Instructions RPAREN RBRACKET
         | CASE WHEN LPAREN Bool RPAREN THEN LPAREN Instructions RPAREN LBRACKET
    '''
    p[0] = (p[1], p[2], p[4], p[8], p[13])
    print(p[0])


def p_expression_case(p):
    '''
    Case : CASE NAME When

    '''
    p[0] = (p[1], p[2], p[3])
    print(p[0])
def p_case_else(p):
    '''
    Case : CASE NAME When ELSE LPAREN Instructions RPAREN
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[6])

def p_expression_whenValue(p):
    '''
    When : WHEN Num THEN LPAREN Instructions RPAREN
        | WHEN Bool THEN LPAREN Instructions RPAREN
    '''
    p[0] = (p[1], p[2], p[5])
    print(p[0])


def p_expression_whenConcatenated(p):
    '''
    When : When COMMA When
    '''
    p[0] = (p[2], p[1], p[3])





def p_expression_instructions(p):
    '''
    Instructions : New
                 | Values
                 | Alter
                 | AlterB
                 | Operator
                 | MoveRight
                 | MoveLeft
                 | Hammer
                 | IsTrue
                 | Stop
                 | PrintValues
    '''
    p[0] = p[1]


def p_expresion_instructions_concatenation(p):
    '''
    Instructions  : Instructions COMMA Instructions
    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_printValues(p):
    '''
    PrintValues : PRINTVALUES LPAREN NAME RPAREN
    '''
    p[0] = (p[1], p[3])
    print(p[0])


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
