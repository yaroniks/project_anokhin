# https://cf.ppt-online.org/files/slide/v/vRAlxeaYzgFDVC2krBdPXQtZbW5McoLJ08In6q/slide-21.jpg

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

CELL_BG = "#d4d4c0"
RIGHT_BG = "#bfbfbf"

tk.Label(root, text="Анкета Web-разработчика", font=("Arial", 18, "bold"), bg="white").pack(anchor="w", padx=10, pady=10)

main_frame = tk.Frame(root, bd=1, relief="solid", bg="black")
main_frame.pack(padx=10, pady=5)


def create_row(row: int, text: str) -> tk.Frame:
    # Левая ячейка
    lbl_frame = tk.Frame(main_frame, bg=CELL_BG, bd=1, relief="solid", width=160, height=40)
    lbl_frame.grid(row=row, column=0, sticky="nsew")
    tk.Label(lbl_frame, text=text, bg=CELL_BG, font=("Arial", 10)).pack(anchor="nw", padx=5, pady=5)

    # Правая ячейка
    content_frame = tk.Frame(main_frame, bg=RIGHT_BG, bd=1, relief="solid")
    content_frame.grid(row=row, column=1, sticky="nsew")

    return content_frame


# Регистрация
f1 = create_row(0, "Регистрационное имя")
entry_name = tk.Entry(f1, width=30)
entry_name.pack(padx=5, pady=5, anchor="w")

# Парлоь
f2 = create_row(1, "Пароль")
entry_pass1 = tk.Entry(f2, width=30, show="*")
entry_pass1.pack(padx=5, pady=2, anchor="w")
pass_sub = tk.Frame(f2, bg=RIGHT_BG)
pass_sub.pack(fill="x", padx=5, pady=2)
entry_pass2 = tk.Entry(pass_sub, width=15, show="*")
entry_pass2.pack(side="left")
tk.Label(pass_sub, text=": подтвердите пароль", bg=RIGHT_BG, font=("Arial", 8)).pack(side="left")

# Специализация
f3 = create_row(2, "Ваша специализация")
spec_var = tk.StringVar(value="Web-мастер")
ttk.Combobox(f3, textvariable=spec_var, values=["Web-мастер", "Frontend", "Backend"],
             state="readonly").pack(padx=5, pady=5, anchor="w")

# Пол
f4 = create_row(3, "Пол")
gender_var = tk.StringVar(value="М")
tk.Radiobutton(f4, text="М", variable=gender_var, value="М", bg=RIGHT_BG).pack(side="left", padx=5)
tk.Radiobutton(f4, text="Ж", variable=gender_var, value="Ж", bg=RIGHT_BG).pack(side="left")

# Навыки
f5 = create_row(4, "Ваши навыки")
skills = ["знание HTML и CSS", "знание Perl", "знание ASP", "знание Adobe Photoshop", "знание JAVA"]
skill_vars = []
for s in skills:
    v = tk.BooleanVar()
    skill_vars.append(v)
    tk.Checkbutton(f5, text=s, variable=v, bg=RIGHT_BG, font=("Arial", 9)).pack(anchor="w", padx=5)

# Доп сведения
f6 = create_row(5, "Дополнительные\nсведения о себе")
text_bio = tk.Text(f6, width=40, height=4, font=("Arial", 10))
text_bio.pack(side="left", padx=5, pady=5)
scroll = tk.Scrollbar(f6, command=text_bio.yview)
scroll.pack(side="left", fill="y", pady=5)
text_bio.config(yscrollcommand=scroll.set)


def clear():
    entry_name.delete(0, 'end')
    entry_pass1.delete(0, 'end')
    entry_pass2.delete(0, 'end')
    text_bio.delete("1.0", 'end')
    spec_var.set("Web-мастер")
    gender_var.set("М")
    for i in skill_vars:
        i.set(False)


btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(fill="x", padx=10, pady=10)
tk.Button(btn_frame, text="зарегистрировать", width=18).pack(side="left", padx=5)
tk.Button(btn_frame, text="очистить форму", width=18, command=clear).pack(side="left")

root.mainloop()
