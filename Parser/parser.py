import ply.yacc as yacc
import os
import codecs
import re
from Lexer.tokens import tokens

run_flag = True
pars = []
errors = []
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
           | Body
           | Principal
           | Proc
           | Procs

    '''
    p[0] = p[1]

start = 'Body'


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
    When : WHEN Num THEN LPAREN Instructions RPAREN SEMICOLON
        | WHEN Bool THEN LPAREN Instructions RPAREN SEMICOLON

    '''
    p[0] = (p[1], p[2], p[5])
    print(p[0])

def p_expression_instructions(p):
    '''
    Instructions : New SEMICOLON
                 | Values SEMICOLON
                 | Alter SEMICOLON
                 | AlterB SEMICOLON
                 | Operator SEMICOLON
                 | MoveRight SEMICOLON
                 | MoveLeft SEMICOLON
                 | Hammer SEMICOLON
                 | IsTrue SEMICOLON
                 | Stop SEMICOLON
                 | PrintValues SEMICOLON
                 | Instructions Instructions
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
                | PRINTVALUES LPAREN STRING RPAREN
    '''
    p[0] = (p[1], p[3])
    print(p[0])


def p_add_expression_printValues(p):
    '''
    PrintValues : PRINTVALUES LPAREN STRING COMMA NAME RPAREN
                | PRINTVALUES LPAREN NAME COMMA STRING RPAREN
    '''
    p[0] = (p[1], p[3], p[5])
    print(p[0])

def p_expression_Procs(p):
    '''
    Procs : Proc
          | Proc Procs
    '''
def p_expression_Proc(p):
    '''
    Proc : PROC NAME LPAREN Instructions RPAREN SEMICOLON
    '''
    p[0] = (p[1], p[2], p[4])
def p_expression_Proc_error(p):
    '''
    Proc : PROC error LPAREN  Instructions RPAREN SEMICOLON
    '''
    print("Syntax error: Procedure does not include an identifier")

def p_expression_Principal(p):
    '''
    Principal : PRINCIPAL LPAREN Instructions RPAREN SEMICOLON
    '''

def p_expression_Body(p):
    '''
    Body : Procs Principal Procs
         | Procs Principal
         | Principal
    '''

    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    elif len(p) == 2:
        p[0] = p[1]
def p_expression_Body_error(p):
    '''
    Body : Procs
         | error Procs

    '''
    error_message = "Syntax error at line "+str(p.lineno(1)+1)+": Body of the program does not include @Principal procedure"
    errors.append(error_message)
    print(error_message)
    raise SyntaxError

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def readFile(dir, run):

    if not run:
        run_flag = False
    fp = codecs.open(dir, "r", "utf-8")
    cadena = fp.read()
    parser = yacc.yacc()
    fp.close()
    par = parser.parse(cadena)
    print(str(par))
    return errors


def clearpars():
    errors.clear()
    pars.clear()
