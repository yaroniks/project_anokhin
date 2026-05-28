import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Анкета Web-разработчика")
root.resizable(False, False)

BG = "white"
CELL_BG = "#d4d4c0"



tk.Label(root, text="Анкета Web-разработчика",
         font=("Arial", 18, "bold")).pack(anchor="w", padx=10, pady=(10, 6))

frame = tk.Frame(root, bd=1, relief="solid")
frame.pack(padx=10, pady=4, fill="x")
frame.columnconfigure(0, minsize=160)
frame.columnconfigure(1, weight=1)


def make_cell(parent, row_idx, col, bg_color, **kwargs):
    f = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    f.grid(row=row_idx, column=col, sticky="nsew", **kwargs)
    return f


# ── 1. Регистрационное имя ────────────────────────────────────
lf = make_cell(frame, 0, 0, CELL_BG, ipadx=4, ipady=4)
tk.Label(lf, text="Регистрационное имя", bg=CELL_BG, font=("Arial", 10)).pack(anchor="nw", padx=4, pady=2)
rf = make_cell(frame, 0, 1, "#bfbfbf", ipadx=4, ipady=4)
entry_name = tk.Entry(rf, width=25)
entry_name.pack(anchor="w", padx=4, pady=2)

# ── 2. Пароль ─────────────────────────────────────────────────
lf = make_cell(frame, 1, 0, CELL_BG, ipadx=4, ipady=4)
tk.Label(lf, text="Пароль", bg=CELL_BG, font=("Arial", 10)).pack(anchor="nw", padx=4, pady=2)
rf = make_cell(frame, 1, 1, "#bfbfbf", ipadx=4, ipady=4)
entry_pass1 = tk.Entry(rf, width=25, show="*")
entry_pass1.pack(anchor="w", padx=4, pady=(2, 0))
sub = tk.Frame(rf, bg="#bfbfbf")
sub.pack(anchor="w", padx=4, pady=(2, 2))
entry_pass2 = tk.Entry(sub, width=20, show="*")
entry_pass2.pack(side="left")
tk.Label(sub, text=": подтвердите пароль", bg="#bfbfbf", font=("Arial", 9)).pack(side="left", padx=4)

# ── 3. Специализация ──────────────────────────────────────────
lf = make_cell(frame, 2, 0, CELL_BG, ipadx=4, ipady=4)
tk.Label(lf, text="Ваша специализация", bg=CELL_BG, font=("Arial", 10)).pack(anchor="nw", padx=4, pady=2)
rf = make_cell(frame, 2, 1, "#bfbfbf", ipadx=4, ipady=4)
spec_options = ["Web-мастер", "Frontend", "Backend", "Fullstack", "DevOps"]
spec_var = tk.StringVar(value=spec_options[0])
ttk.Combobox(rf, textvariable=spec_var, values=spec_options,
             state="readonly", width=18).pack(anchor="w", padx=4, pady=2)

# ── 4. Пол ────────────────────────────────────────────────────
lf = make_cell(frame, 3, 0, CELL_BG, ipadx=4, ipady=4)
tk.Label(lf, text="Пол", bg=CELL_BG, font=("Arial", 10)).pack(anchor="nw", padx=4, pady=2)
rf = make_cell(frame, 3, 1, "#bfbfbf", ipadx=4, ipady=4)
gender_var = tk.StringVar(value="М")
g_frame = tk.Frame(rf, bg="#bfbfbf")
g_frame.pack(anchor="w", padx=4, pady=2)
tk.Radiobutton(g_frame, text="М", variable=gender_var, value="М",
               bg="#bfbfbf", font=("Arial", 10)).pack(side="left")
tk.Radiobutton(g_frame, text="Ж", variable=gender_var, value="Ж",
               bg="#bfbfbf", font=("Arial", 10)).pack(side="left")

# ── 5. Навыки ─────────────────────────────────────────────────
lf = make_cell(frame, 4, 0, CELL_BG, ipadx=4, ipady=4)
tk.Label(lf, text="Ваши навыки", bg=CELL_BG, font=("Arial", 10)).pack(anchor="nw", padx=4, pady=2)
rf = make_cell(frame, 4, 1, "#bfbfbf", ipadx=4, ipady=4)
skills = [
    "знание HTML и CSS", "знание Perl", "знание ASP",
    "знание Adobe Photoshop", "знание JAVA",
    "знание JavaScript", "знание Flash",
]
skill_vars = []
for s in skills:
    v = tk.BooleanVar()
    skill_vars.append(v)
    tk.Checkbutton(rf, text=s, variable=v, bg="#bfbfbf",
                   font=("Arial", 10), anchor="w").pack(anchor="w", padx=4)

# ── 6. Доп. сведения ──────────────────────────────────────────
lf = make_cell(frame, 5, 0, CELL_BG, ipadx=4, ipady=4)
tk.Label(lf, text="Дополнительные\nсведения о себе", bg=CELL_BG,
         font=("Arial", 10), justify="left").pack(anchor="nw", padx=4, pady=2)
rf = make_cell(frame, 5, 1, "#bfbfbf")
text_bio = tk.Text(rf, width=42, height=4, font=("Arial", 10))
sb = tk.Scrollbar(rf, command=text_bio.yview)
text_bio.configure(yscrollcommand=sb.set)
text_bio.pack(side="left", padx=4, pady=4)
sb.pack(side="left", fill="y", pady=4)


# ── Функция очистки ───────────────────────────────────────────
def clear_form():
    entry_name.delete(0, tk.END)
    entry_pass1.delete(0, tk.END)
    entry_pass2.delete(0, tk.END)
    spec_var.set(spec_options[0])
    gender_var.set("М")
    for v in skill_vars:
        v.set(False)
    text_bio.delete("1.0", tk.END)


# ── Кнопки ────────────────────────────────────────────────────
btn_frame = tk.Frame(root)
btn_frame.pack(pady=8, padx=10, fill="x")

tk.Button(btn_frame, text="зарегистрировать",
          width=20, font=("Arial", 10), relief="raised", bd=2).pack(side="left", padx=(0, 6))
tk.Button(btn_frame, text="очистить форму",
          width=20, font=("Arial", 10), relief="raised", bd=2,
          command=clear_form).pack(side="left")

root.mainloop()
