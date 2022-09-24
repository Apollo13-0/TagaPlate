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
           | ControlStructure
           | Sentences
           | Bool_operator

    '''
    p[0] = p[1]

start = 'Body'


def p_expression_new(p):
    '''
    New : NEW NAME COMMA LPAREN NUM COMMA Num RPAREN
        | NEW NAME COMMA LPAREN BOOL COMMA Bool RPAREN
    '''
    #(new , identificador, tipo, valor)
    p[0] = (p[1], p[2], p[5], p[7])

def p_expression_new_error_noid(p):
    '''
    New : NEW COMMA LPAREN NUM COMMA Num RPAREN
        | NEW COMMA LPAREN NUM COMMA Bool RPAREN
    '''
    error_message = "Syntax error at line"+str(p.lineno(2)+1) + "variable identifier missing"
    errors.append(error_message)
    raise SyntaxError
def p_expression_new_error_no_value(p):
    '''
        New : NEW NAME COMMA LPAREN NUM COMMA RPAREN
            | NEW NAME COMMA LPAREN BOOL COMMA RPAREN
    '''
    error_message = "Syntax error at line" + str(p.lineno(2) + 1) + "variable value missing"
    errors.append(error_message)
    raise SyntaxError
def p_expression_new_error_wrong_value(p):
    '''
        New : NEW NAME COMMA LPAREN NUM  COMMA Bool RPAREN
            | NEW NAME COMMA LPAREN BOOL COMMA Num RPAREN
    '''
    error_message = "Syntax error at line" + str(p.lineno(2) + 1) + "variable value does not match type"
    errors.append(error_message)
    raise SyntaxError

def p_expression_values(p):
    '''
    Values : VALUES LPAREN NAME COMMA Num RPAREN
           | VALUES LPAREN NAME COMMA Bool RPAREN
           | VALUES LPAREN NAME COMMA Alter RPAREN
    '''
    #values name, value
    p[0] = (p[1], p[3], p[5])

def p_expression_Num(p):
    '''
    Num : INT
        | FLOAT
    '''

    p[0] = float(p[1])

def p_expression_Plus(p):
    '''
    Num : Num PLUS Num
        | Num MINUS Num
        | Num TIMES Num
        | Num DIVIDE Num
        | Num INT_DIVIDE Num
        | Num MODULE Num
    '''

    if p[2] == '+':
        p[0] = float(p[1]) + float(p[3])
    elif p[2] == '-':
        p[0] = float(p[1]) - float(p[3])
    elif p[2] == '*':
        p[0] = float(p[1]) * float(p[3])
    elif p[2] == '/':
        p[0] = float(p[1]) + float(p[3])
    elif p[2] == '//':
        p[0] = int(float(p[1]) + float(p[3]))
    elif p[2] == '%':
        p[0] = float(p[1]) % float(p[3])



def p_expression_boolean(p):
    '''
    Bool : TRUE
         | FALSE
    '''

    if p[1] == 'True':
        p[0] = True
    else:
        p[0] = False
def p_booleanoperator(p):
    '''
    Bool_operator : LT
                  | GT
                  | LE
                  | GE
                  | EQUAL
                  | NOT_EQUAL
    '''
    p[0] = p[1]
def p_another_boolean(p):
    '''
    Bool : Num Bool_operator Num
         | NAME Bool_operator Num
         | NAME Bool_operator NAME
    '''
    if isinstance(p[1], float) and isinstance(p[3], float):
        if p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        elif p[2] == '<>':
            p[0] = p[1] != p[3]
    else:
        p[0] = (p[1], p[2], p[3])
def p_expression_Alter(p):
    '''
    Alter : ALTER LPAREN NAME COMMA Operator COMMA Num RPAREN
    '''

    # alter, name, operator, num
    p[0] = (p[1], p[3], p[5], p[7])


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
    #alterb, name
    p[0] = (p[1], p[3])
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
    #hammer position
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
    Stop : STOP SEMICOLON
    '''
    p[0] = p[1]


def p_expression_isTrue(p):
    '''
    IsTrue : ISTRUE LPAREN NAME RPAREN
    '''
    #istrue id
    p[0] = (p[1], p[3])

def p_expression_repeat(p):
    '''
    Repeat : REPEAT LPAREN Instructions BREAK SEMICOLON RPAREN SEMICOLON
    '''
    # repeat
    p[0] = (p[1], p[3])

def p_repea_error_nobreak(p):
    '''
    Repeat : REPEAT LPAREN Instructions RPAREN SEMICOLON
    '''
    error_msg = "Syntax error on line "+str(p.lineno(4))+" : Break not found in Repeat structure"
    errors.append(error_msg)
    raise SyntaxError
def p_expression_until(p):
    '''
    Until : UNTIL LPAREN Instructions RPAREN Bool SEMICOLON
    '''
    p[0] = (p[1], p[3], p[5])

def p_until_error_nocond(p):
    '''
        Until : UNTIL LPAREN Instructions RPAREN
              | UNTIL LPAREN Instructions RPAREN  SEMICOLON
    '''
    error_msg = "Syntax error on line " + str(p.lineno(4)) + " : No condition at the end of Until structure"
    errors.append(error_msg)
    raise SyntaxError
def p_expression_while(p):
    '''
    While : WHILE Bool LPAREN Instructions RPAREN SEMICOLON
    '''
    p[0] = (p[1], p[2], p[4])

def p_exoression_while_error(p):
    '''
    While : WHILE LPAREN Instructions RPAREN
          | WHILE LPAREN Instructions RPAREN SEMICOLON
          | WHILE LPAREN Num Instructions RPAREN
          | WHILE LPAREN NAME Instructions RPAREN
          | WHILE LPAREN NAME Instructions RPAREN SEMICOLON
          | WHILE Bool_operator Name Instructions
          | WHILE Bool_operator Name Instructions SEMICOLON
          | WHILE Bool_operator Num Instructions
          | WHILE Bool_operator Num Instructions SEMICOLON
          | WHILE Name Bool_operator  Instructions
          | WHILE Name  Bool_operator Instructions SEMICOLON
          | WHILE Num Bool_operator Instructions
          | WHILE Num Bool_operator Instructions SEMICOLON
    '''
    error_message = "Syntax error at line " +str(p.lineno(1)) + "Condition not found in While and/or no semicolon"
    errors.append(error_message)
    raise SyntaxError
def p_expression_caseWhen(p):
    '''
    Case_When : CASE WHEN LPAREN Bool RPAREN THEN LPAREN Instructions RPAREN LBRACKET SEMICOLON
    '''

    p[0] = (p[1]+p[2], p[4], p[8])


def p_caseWhen_else(p):
    '''
    Case_When : CASE WHEN LPAREN Bool RPAREN THEN LPAREN Instructions RPAREN LBRACKET ELSE LPAREN Instructions RPAREN RBRACKET SEMICOLON
    '''
    p[0] = (p[1] + p[2], p[4], p[8], p[13])
def p_expression_case(p):
    '''
    Case : CASE NAME When SEMICOLON

    '''

    #case, id, when
    p[0] = (p[1], p[2], p[3])


def p_case_else(p):
    '''
    Case : CASE NAME When ELSE LPAREN Instructions RPAREN SEMICOLON
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[6])


def p_expression_whenValue(p):
    '''
    When : WHEN Num THEN LPAREN Instructions RPAREN SEMICOLON
        | WHEN Bool THEN LPAREN Instructions RPAREN SEMICOLON

    '''
    p[0] = (p[1], p[2], p[5])

def p_expression_sentences(p):
    '''
    Sentences : New SEMICOLON
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
    '''
    p[0] = p[1]

def p_controlstructures(p):
    '''
    ControlStructure : When
                     | Case
                     | While
                     | Case_When
                     | Until
                     | Repeat
    '''

    p[0] = p[1]

def p_instructions(p):
    '''
    Instructions : ControlStructure
                 | Sentences
                 | Instructions Instructions
    '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('Instructions', p[1], p[2])

def p_expression_printValues(p):
    '''
    PrintValues : PRINTVALUES LPAREN NAME RPAREN
                | PRINTVALUES LPAREN STRING RPAREN
    '''
    p[0] = (p[1], p[3])


def p_add_expression_printValues(p):
    '''
    PrintValues : PRINTVALUES LPAREN STRING COMMA NAME RPAREN
                | PRINTVALUES LPAREN NAME COMMA STRING RPAREN
    '''
    p[0] = (p[1], p[3], p[5])

def p_expression_Procs(p):
    '''
    Procs : Proc
          | Proc Procs
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = (p[1], p[2])

def p_expression_Proc(p):
    '''
    Proc : PROC NAME LPAREN Instructions RPAREN SEMICOLON
    '''
    p[0] = (p[1], p[2], p[4])

def p_expression_Proc_error(p):
    '''
    Proc : PROC  LPAREN  Instructions RPAREN SEMICOLON
    '''
    error_message = "Syntax error at line:" +str(p.lineno(2))+" Procedure does not include an identifier"
    errors.append(error_message)
    print(error_message)
    raise SyntaxError

def p_expression_Principal(p):
    '''
    Principal : PRINCIPAL LPAREN Instructions RPAREN SEMICOLON
    '''
    p[0] = (p[1], p[3])
def p_expression_Principal_error(p):
    '''
    Principal : PRINCIPAL error Instructions RPAREN SEMICOLON
              | PRINCIPAL LPAREN Instructions SEMICOLON
    '''
    error_message = "Syntax error at line"+str(p.lineno(1)+1)+": Parenthesis needed"
    errors.append(error_message)
    print(error_message)

def p_expression_Body(p):
    '''
    Body : Procs Principal Procs
         | Procs Principal
         | Principal Procs
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
    '''
    error_message = "Syntax error at line "+str(p.lineno(1)+1)+": Body of the program does not include @Principal procedure"
    errors.append(error_message)
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
    print(pars)
    return errors

def clearpars():
    errors.clear()
    pars.clear()
