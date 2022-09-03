import GUI.MainWindow as MainWindow
from Lexer import tokens


def main():

    # lexer = tokens.lexer
    # lexer.input("New")
    #
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(tok)

    ideWindow = MainWindow.IDE()
    ideWindow.startIDE()


if __name__ == "__main__":
    main()