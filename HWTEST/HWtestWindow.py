from tkinter import *
import socket

class HWtest:

    def __init__(self):
        self.testWindow = Tk()
        self.testWindow.geometry("800x600+200+200")
        self.testWindow.resizable(False, False)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self, host, port):
        self.sock.connect((host, port))
    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN