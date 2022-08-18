from tkinter import *
from tkinter import filedialog

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

        # Key command
        self.ideWindow.bind('<F5>', lambda e: self.compile())

        self.row = 0

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

        # first approach of the side bar for numeration
        self.lineNum = Text(self.ideWindow, bg="#444444", font=("Fixedsys", 16), fg="#eeeeee")
        self.lineNum.place(x=5, y=10,width=20, height=300)
        self.lineNum.tag_configure('line', justify='right')
        self.lineNum.config(state=DISABLED)

        # self.uniscrollbar = Scrollbar(self.ideWindow)
        # #self.uniscrollbar.grid(row=self.__uniscrollbarRow, column=self.__uniscrollbarCol, sticky=NS)
        # self.uniscrollbar.place(x=750, y=10, width=15)
        # # self.uniscrollbar.pack()
        # self.uniscrollbar.config(command=self.__scrollBoth)
        # self.entryBox.config(yscrollcommand=self.__updateScroll)
        # self.lineNum.config(yscrollcommand=self.__updateScroll)

    # methods that scrolls both text box
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
            code = ""
            for line in f:
                code += line
        # set text on the entry box
        self.setCode(code)

    def setCode(self, codeRaw):
        self.entryBox.delete('1.0', END)
        self.entryBox.insert(END, codeRaw)

    def getCode(self):
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
        code = self.getCode()
        file.write(code)
        file.close()

    def compile(self):
        pass

    def runCompile(self):
        pass