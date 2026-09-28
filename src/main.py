import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

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

root.mainloop()