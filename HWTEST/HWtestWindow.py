from tkinter import *
import socket


class HWtest:

    def __init__(self):
        self.testWindow = Tk()
        self.testWindow.geometry("500x500")
        self.testWindow.resizable(False, False)
        self.testWindow.title("Hardware testing")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect("192.168.4.1", 8888)

        self.frame = Frame(self.testWindow)
        self.frame.pack()

        self.bHammerN = Button(self.frame, text="Hammer(N)", command=self.hammerN)
        self.bHammerN.pack()

        self.bHammerS = Button(self.frame, text="Hammer(S)", command=self.hammerS)
        self.bHammerS.pack()

        self.bHammerE = Button(self.frame, text="Hammer(E)", command=self.hammerE)
        self.bHammerE.pack()

        self.bHammerO = Button(self.frame, text="Hammer(O)", command=self.hammerO)
        self.bHammerO.pack()

        self.bMoveRight = Button(self.frame, text="MoveRight", command=self.turnR)
        self.bMoveRight.pack()

        self.bMoveLeft = Button(self.frame, text="Moveleft", command=self.turnL)
        self.bMoveLeft.pack()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def hammerN(self):
        self.sock.send(b'f')

    def hammerS(self):
        self.sock.send(b'e')

    def hammerE(self):
        self.sock.send(b'd')

    def hammerO(self):
        self.sock.send(b'c')

    def turnR(self):
        self.sock.send(b'a')

    def turnL(self):
        self.sock.send(b'b')
    def startTesting(self):
        self.testWindow.mainloop()