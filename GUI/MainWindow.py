from tkinter import *
from tkinter import filedialog
from Lexer import tokens
from Parser import parser

class IDE:

    def __init__(self):

        # Main IDE Window
        self.ideWindow = Tk()

        # set the width and height of the window
        self.ideWindow.geometry("800x600+200+200")

        # The window will not be resizable
        self.ideWindow.resizable(False, False)

        # shows window title
        self.ideWindow.title("TagaPlate IDE")

        # Canvas creation
        myCanvas = Canvas(self.ideWindow,
                          width="800", height="600",
                          bd=0, highlightthickness=0,
                          bg="#e0dedb")

        myCanvas.pack(fill="both", expand=True)

        # Row counter
        self.row = 1

        # Key command
        self.ideWindow.bind("<F5>", lambda e: self.compile())
        self.ideWindow.bind("<Return>", lambda event: self.addRow())
        self.ideWindow.bind("<BackSpace>", lambda event2: self.checkRow())

    def topBar(self):

        # Creates the top bar where are the buttons to compile, save or open
        menuBar = Menu(self.ideWindow)

        self.ideWindow.config(menu=menuBar)

        fileMenu = Menu(menuBar, tearoff=0)

        menuBar.add_cascade(label="Archivo", menu=fileMenu)

        # Filemenu options definition
        fileMenu.add_command(label="Abrir", command=self.openFile)
        fileMenu.add_command(label="Guardar", command=self.saveFile)

        menuBar.add_command(label="Compilar", command=self.compile)
        menuBar.add_command(label="Ejecutar", command=self.runCompile)

    def codeEntry(self):

        # Entry box for the code
        self.entryBox = Text(self.ideWindow,
                              font=("Fixedsys", 16),
                              bg="#eeeeee",
                              fg="#383e42", highlightthickness=1)

        self.entryBox.place(x=30, y=10, width=750, height=300)

        # Text box for the line numbers
        self.lineNum = Text(self.ideWindow, bg="#e0dedb", font=("Fixedsys", 16), fg="#383e42")
        self.lineNum.place(x=0, y=10, width=30, height=300)
        self.setLineText("1")
        self.lineNum.config(state=DISABLED)

        # sinc scrollbars
        self.uniscrollbar = Scrollbar(self.ideWindow, orient="vertical", command=self.entryBox.yview)
        self.uniscrollbar.place(x=782, y=10, width=15)
        self.uniscrollbar.config(command=self.scrollBoth)
        self.entryBox.config(yscrollcommand=self.updateScroll)
        self.lineNum.config(yscrollcommand=self.updateScroll)

    def scrollBoth(self, action, position, type=None):
        self.entryBox.yview_moveto(position)
        self.lineNum.yview_moveto(position)

    def updateScroll(self, first, last, type=None):
        self.entryBox.yview_moveto(first)
        self.lineNum.yview_moveto(first)
        self.uniscrollbar.set(first, last)

    def codeOutput(self):

        # Output box where the results and errors will be shown
        self.outputBox = Text(self.ideWindow,
                              font=("Fixedsys", 16),
                              bg="#eeeeee", bd=1,
                              fg="#383e42", highlightthickness=1)

        self.outputBox.place(x=10, y=315, width=780, height=275)
        self.outputBox.config(state=DISABLED)

    def startIDE(self):

        self.topBar()
        self.codeEntry()
        self.codeOutput()

        self.ideWindow.mainloop()

    def openFile(self):
        # Creates the new path for the document
        path = filedialog.askopenfilename(initialdir="/",
                                          title="Abrir archivo",
                                          filetypes=(("text files", "*.txt"),
                                          ("All files", "*.*")))
        # open the document and obtains the text
        with open(path, "r") as f:
            cont = 1
            code = ""
            self.tmpText = ""

            for line in f:
                code += line
                cont = cont+1

            # Creatation of the str for the line text box
            for num in range(1, cont):
                self.tmpText = self.tmpText + str(num) + "\n"

            # set text on the line box
            self.lineNum.config(state=NORMAL)
            self.setLineText(self.tmpText)
            self.lineNum.config(state=DISABLED)

            # set text on the entry box
            self.setEntryCode(code)

    def setEntryCode(self, codeRaw):
        self.entryBox.delete('1.0', END)
        self.entryBox.insert(END, codeRaw)

    def getEntryCode(self):
        code = self.entryBox.get("1.0",END)
        return code

    def saveFile(self):

        # Creates the new path for the document
        path = filedialog.asksaveasfilename(initialdir="/", title=
                                            "Guardar como",
                                            filetypes=(("text files", "*.txt"),
                                            ("All files", "*.*")))
        # Saves the text in the new document
        file = open(path, "w")
        code = self.getEntryCode()
        file.write(code)
        file.close()

    def setLineText(self, numbersTxt):
        self.lineNum.delete('1.0', END)
        self.lineNum.insert(END, numbersTxt)

    def compile(self):
        self.outputBox.config(state=NORMAL)
        self.outputBox.delete('1.0',END)
        self.outputBox.update()
        file = open("compile.txt","w")
        code = self.getEntryCode()
        file.write(code)
        file.close()
        toks = tokens.read_File("compile.txt")
        pars = parser.readFile("compile.txt", False)
        print(pars)
        print(toks)

        if (pars == []) and (toks == []):
            self.outputBox.insert(END, "Program succesfully compiled")
        else:
            for par in pars:
                self.outputBox.insert(END,(str(par) + "\n"))
            for tok in toks:
                self.outputBox.insert(END,(str(tok) + "\n"))
        self.outputBox.config(state=DISABLED)
        tokens.cleartoks()
        parser.clearpars()
        pass
    def runCompile(self):
        pass

    def addRow(self):

        # Row counter incrementation
        self.row = self.row + 1
        self.tmpText = ""

        # Creation of the str for the line text box
        for num in range(1, self.row + 1):
            self.tmpText = self.tmpText + str(num) + "\n"

        # set text on the line box
        self.lineNum.config(state=NORMAL)
        self.setLineText(self.tmpText)
        self.lineNum.config(state=DISABLED)

    def deleteRow(self):

        # Check if is only one row and sets row counter
        if self.row == 1:
            self.row = 1
        else:
            self.row = self.row - 1

        self.tmpText = ""

        # Creation of the str for the line text box
        for num in range(1, self.row + 1):
            self.tmpText = self.tmpText + str(num) + "\n"

        # set text on the line box
        self.lineNum.config(state=NORMAL)
        self.setLineText(self.tmpText)
        self.lineNum.config(state=DISABLED)

    def checkRow(self):
        # Checks if the value of the Row counter is equal to the value of Row
        content = self.entryBox.get("1.0","end")
        linebrake = content.count('\n')
        if self.row > int(linebrake):
            self.deleteRow()
