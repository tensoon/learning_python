import tkinter as tk
from tkinter import filedialog, Text

import os

icon = r"C:\Users\balin\OneDrive\Pictures\Bridge4.png"


root = tk.Tk()
x = tk.StringVar()
root.iconphoto(False, tk.PhotoImage(file=icon))
root.title("Config Extractor")
canvas = tk.Canvas(root, height=700, width=700, bg="#282a36")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


openFile = tk.Button(
    frame, text="Open File", padx=10, pady=10, fg="white", bg="#282a36"
)
openFile.pack()

runFile = tk.Button(frame, text="Run", padx=10, pady=10, fg="white", bg="#282a36")
runFile.pack()

tk.Radiobutton(frame, text="Feed Filter", variable=x, value="ff").pack()
tk.Radiobutton(frame, text="Multicast Reader", variable=x, value="mcr").pack()

label = tk.Label(frame, text=x.get())
label.pack()

# os.startfile(filename)
root.mainloop()
