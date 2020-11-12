import socket
from tkinter import Tk, Label, Button, messagebox
import tkinter as tk

class GetIPAddress:
    def __init__(self, winTitle, xSize, ySize, *args):
         self.window = tk.Tk()
         if args:
              self.window.configure(bg=args)
         self.window.geometry(f'{xSize}x{ySize}')
         self.window.title(winTitle)
         self.windowHeight = self.window.winfo_reqheight()
         self.windowWidth = self.window.winfo_reqwidth()
         self.ipBtn = Button(text="Get IP", command=self.getTheIP)
         self.ipBtn.place(x=self.windowHeight / 2, y=self.windowWidth / 2)
         self.window.resizable(False, False) 
         self.window.mainloop()

    def getTheIP(self):
        self.getIP = socket.gethostbyname(socket.gethostname())
        tk.messagebox.showinfo(message=self.getIP)
    
GetIPGUI = GetIPAddress("Get My IP", 250, 250)