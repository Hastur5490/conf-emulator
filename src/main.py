import tkinter as tk
from tkinter import scrolledtext
import getpass
import os

root = tk.Tk()

username = getpass.getuser()
root.title(f"Эмулятор пользователя - [{username}]")
root.geometry("800x800")
root.configure(bg="#121212")

#Область вывода
output = scrolledtext.ScrolledText(root, bg="#1e1e1e", fg= "#FFD700", font=("Consolas", 12), wrap=tk.WORD)
output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
output.config(state="disabled")

#Поле ввода
command_entry = tk.Entry(root, bg="#2d2d2d", fg="white", insertbackground="white", font=("Consolas", 12))
command_entry.pack(fill=tk.X, padx=5, pady=5)
command_entry.focus()

def proccess_command(event=None):
    command = command_entry.get().strip()
    command_entry.delete(0, tk.END)
    if not command:
        return

    expanded_command = os.path.expandvars(command)

    output.config(state="normal")
    output.insert(tk.END, f"$ {command}\n")          # ← вот здесь исправление (пробел после $)
    if expanded_command != command:
        output.insert(tk.END, f"раскрыто: {expanded_command}\n")
    output.see(tk.END)
    output.config(state="disabled")

command_entry.bind("<Return>", proccess_command)

root.mainloop()