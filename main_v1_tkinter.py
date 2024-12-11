import tkinter as tk
from tkinter import ttk
from math import cos, exp, log, sqrt, sin, atan, tan

def calculate_alpha():
    try:
        x = float(entry_x_linear.get())
        y = float(entry_y_linear.get())
        z = float(entry_z_linear.get())

        if y <= abs(x):
            raise ValueError("Подкоренное выражение должно быть больше нуля.")

        alpha = log(y - sqrt(abs(x))) * (x - y / 2) + sin(atan(z))**2
        linear_result.set(f"\u03B1 = {alpha:.4f}")
    except Exception as e:
        linear_result.set(f"Ошибка: {e}")

def calculate_k():
    try:
        x = float(entry_x_branch.get())
        y = float(entry_y_branch.get())
        xy = x * y

        selected_function = func_choice.get()

        if selected_function == "cos(x)":
            f_x = cos(x)
        elif selected_function == "sqrt(x)":
            if x < 0:
                raise ValueError("x должен быть больше или равен 0 для корня.")
            f_x = sqrt(x)
        elif selected_function == "exp(x)":
            f_x = exp(x)
        else:
            raise ValueError("Выберите функцию.")

        if 1 < xy < 4:
            k = (f_x + y)**2
        elif 8 < xy < 10:
            k = f_x * tan(y)
        else:
            k = f_x + y

        branch_result.set(f"k = {k:.4f}")
    except Exception as e:
        branch_result.set(f"Ошибка: {e}")

def update_result_color():
    if result_red.get():
        result_label_linear.config(fg="red")
        result_label_branch.config(fg="red")
    else:
        result_label_linear.config(fg="black")
        result_label_branch.config(fg="black")

root = tk.Tk()
root.title("Практическая работа №5")
root.geometry("600x500")

notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Linear Algorithm Frame
linear_frame = ttk.Frame(notebook)
notebook.add(linear_frame, text="Линейный алгоритм")
tk.Label(linear_frame, text="Введите значение X:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_x_linear = tk.Entry(linear_frame)
entry_x_linear.grid(row=0, column=1, padx=10, pady=5)

tk.Label(linear_frame, text="Введите значение Y:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_y_linear = tk.Entry(linear_frame)
entry_y_linear.grid(row=1, column=1, padx=10, pady=5)

tk.Label(linear_frame, text="Введите значение Z:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_z_linear = tk.Entry(linear_frame)
entry_z_linear.grid(row=2, column=1, padx=10, pady=5)

linear_result = tk.StringVar()
tk.Label(linear_frame, text="Результат:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
result_label_linear = tk.Label(linear_frame, textvariable=linear_result, width=30, anchor="w", fg="black")
result_label_linear.grid(row=3, column=1, padx=10, pady=5)

tk.Button(linear_frame, text="Рассчитать", command=calculate_alpha).grid(row=4, column=0, columnspan=2, pady=10)

# Branching Algorithm Frame
branch_frame = ttk.Frame(notebook)
notebook.add(branch_frame, text="Разветвляющийся алгоритм")

tk.Label(branch_frame, text="Введите значение X:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_x_branch = tk.Entry(branch_frame)
entry_x_branch.grid(row=0, column=1, padx=10, pady=5)

tk.Label(branch_frame, text="Введите значение Y:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_y_branch = tk.Entry(branch_frame)
entry_y_branch.grid(row=1, column=1, padx=10, pady=5)
tk.Label(branch_frame, text="Выбор функции:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
func_choice = tk.StringVar()
func_choice.set("cos(x)")

tk.Radiobutton(branch_frame, text="cos(x)", variable=func_choice, value="cos(x)").grid(row=3, column=0, sticky="w")
tk.Radiobutton(branch_frame, text="sqrt(x)", variable=func_choice, value="sqrt(x)").grid(row=4, column=0, sticky="w")
tk.Radiobutton(branch_frame, text="exp(x)", variable=func_choice, value="exp(x)").grid(row=5, column=0, sticky="w")

branch_result = tk.StringVar()
tk.Label(branch_frame, text="Результат:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
result_label_branch = tk.Label(branch_frame, textvariable=branch_result, width=30, anchor="w", fg="black")
result_label_branch.grid(row=6, column=1, padx=10, pady=5)

tk.Button(branch_frame, text="Рассчитать", command=calculate_k).grid(row=7, column=0, columnspan=2, pady=10)

# Common Checkbutton for Color
result_red = tk.BooleanVar()
tk.Checkbutton(root, text="Ответ красным цветом", variable=result_red, command=update_result_color).pack(pady=10)

root.mainloop()