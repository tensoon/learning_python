from tkinter import *
from code import *
import sys


class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.insert("end", string)
        self.text_space.see("end")


def buttonCallback():

    code = codeEditor.get("1.0", END + "-1c")

    stdout = sys.stdout
    stderr = sys.stderr

    outputWindow.delete("1.0", END)

    sys.stdout = StdoutRedirector(outputWindow)
    sys.stderr = StdoutRedirector(outputWindow)

    interp = InteractiveInterpreter()
    interp.runcode(code)

    sys.stdout = stdout
    sys.stderr = stderr



if __name__ == "__main__":
    root = Tk()
    frame1 = Frame(root)
    frame1.pack(side=TOP, fill=Y)
    Button(text="Run", command=buttonCallback).pack()
    frame2 = Frame(root)
    frame2.pack(side=BOTTOM, fill=Y)

    codeEditor = Text(frame1)
    codeScroll = Scrollbar(frame1, command=codeEditor.yview)
    codeEditor.configure(yscrollcommand=codeScroll.set)
    codeEditor.pack(side=LEFT)
    codeScroll.pack(side=RIGHT, fill=Y)

    outputWindow = Text(frame2)
    outputScroll = Scrollbar(frame2, command=outputWindow.yview)
    outputWindow.configure(yscrollcommand=outputScroll.set)
    outputWindow.pack(side=LEFT)
    outputScroll.pack(side=RIGHT, fill=Y)

    root.mainloop()
