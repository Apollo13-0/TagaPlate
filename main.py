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
    #lexer = tokens.lexer
    #tokens.read_File("/Users/Joanj/PycharmProjects/TagaPlate/compile.txt")

    ideWindow = MainWindow.IDE()
    ideWindow.startIDE()


if __name__ == "__main__":
    main()
