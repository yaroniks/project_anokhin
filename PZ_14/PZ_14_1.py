# https://cf.ppt-online.org/files/slide/v/vRAlxeaYzgFDVC2krBdPXQtZbW5McoLJ08In6q/slide-21.jpg

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(True, True)

tk.Label(root, text='Анкета Web-разработчика', font=('Arial', 20, 'bold')).grid(row=0, column=0, sticky=tk.W)

tk.Label(root, text='Регистрационное имя').grid(row=1, column=0, sticky=tk.W)
tk.Entry(root).grid(row=1, column=1)

tk.Label(root, text='Пароль').grid(row=2, column=0, sticky=tk.W)
tk.Entry(root).grid(row=2, column=1)
tk.Entry(root).grid(row=3, column=1)
# tk.Label(root, text=': подтвердите пароль').grid(row=3, column=1)

tk.Label(root, text='Ваша специализация').grid(row=4, column=0, sticky=tk.W)
select = ttk.Combobox(root, values=['Web-мастер'])
select.current(0)
select.grid(row=4, column=1)


def register():
    ...


def clear_form():
    ...


tk.Button(root, text='зарегистрировать', command=register).grid(row=5, column=0, sticky=tk.W)
tk.Button(root, text='очистить форму', command=clear_form).grid(row=5, column=0)


if __name__ == '__main__':
    root.mainloop()
