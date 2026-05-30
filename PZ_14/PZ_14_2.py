# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

import random
import tkinter as tk
from copy import deepcopy
from tkinter import messagebox


def generate_matrix(n: int) -> list[list[int]]:
    return [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]


def change_main_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = deepcopy(matrix)
    for i in range(len(matrix)):
        new_matrix[i][i] *= 2
    return new_matrix


def format_matrix(matrix: list[list[int]]) -> str:
    return "\n".join(
        [" ".join([f"{num:3}" for num in row]) for row in matrix]
    )


def process_matrix():
    try:
        n = int(entry_n.get())

        original = generate_matrix(n)
        modified = change_main_diagonal(original)

        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, "Исходная матрица:\n")
        text_display.insert(tk.END, format_matrix(original) + "\n\n")
        text_display.insert(tk.END, "Главная диагональ увеличена в 2 раза:\n")
        text_display.insert(tk.END, format_matrix(modified))

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое положительное число.")


root = tk.Tk()

frame_top = tk.Frame(root, pady=10)
frame_top.pack()

tk.Label(frame_top, text="Размер матрицы (n):").pack(side=tk.LEFT)
entry_n = tk.Entry(frame_top, width=5)
entry_n.pack(side=tk.LEFT, padx=5)
entry_n.insert(0, "5")  # дефолтное значение

btn_calculate = tk.Button(frame_top, text="Сгенерировать и изменить", command=process_matrix)
btn_calculate.pack(side=tk.LEFT, padx=10)

text_display = tk.Text(root, font=("Courier New", 12), padx=10, pady=10)
text_display.pack()

root.mainloop()
