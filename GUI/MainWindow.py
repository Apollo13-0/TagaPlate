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
        self.ideWindow.bind('<F5>', lambda e: self.compileCode())

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
                              font=("Helvetica", 14),
                              bg="#eeeeee", bd=1,
                              fg="#383e42", highlightthickness=1,
                              insertbackground='white')

        self.entryBox.place(x=10, y=10, width=780, height=300)


    def codeOutput(self):

        # Output box where the results and errors will be shown
        self.outputBox = Text(self.ideWindow,
                              font=("Helvetica", 14),
                              bg="#eeeeee", bd=1,
                              fg="#383e42", highlightthickness=1,
                              insertbackground='white')

        self.outputBox.place(x=10, y=315, width=780, height=275)



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