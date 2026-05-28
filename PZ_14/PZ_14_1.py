# https://cf.ppt-online.org/files/slide/v/vRAlxeaYzgFDVC2krBdPXQtZbW5McoLJ08In6q/slide-21.jpg

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(True, True)

tk.Label(root, text='Анкета Web-разработчика', font=('Arial', 20, 'bold')).pack(anchor="w")

frame = tk.Frame(root, background='#d1dac9')

tk.Label(root, text='Анкета Web-разработчика', font=('Arial', 20, 'bold')).pack(anchor="w")


if __name__ == '__main__':
    root.mainloop()
