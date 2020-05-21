# Python Libs
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


window = tk.Tk()
app = tk.StringVar()
window.title("Config Extractor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
ff_btn = tk.Radiobutton(fr_buttons, text="Feed Filter", variable=app, value="ff")
mcr_btn = tk.Radiobutton(fr_buttons, text="Multicast Reader", variable=app, value="mcr")
xml_btn = tk.Radiobutton(fr_buttons, text="XML Service", variable=app, value="xml")


ff_btn.grid(row=1, column=0, sticky="w", padx=5)
mcr_btn.grid(row=2, column=0, sticky="w", padx=5)
xml_btn.grid(row=3, column=0, sticky="w", padx=5)
btn_open.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=5, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
txt_edit.insert(END, output)

window.mainloop()
