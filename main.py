import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import pow, log10, sin, cos, sqrt

def is_double(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def perform_first_task():
    if field_a.get().strip() == "" or field_b.get().strip() == "" or field_c.get().strip() == "" or field_d.get().strip() == "":
        field_1.delete(0, tk.END)
        field_1.insert(0, "Помилка при введенні даних!")
        return

    a = float(field_a.get())
    b = float(field_b.get())
    c = float(field_c.get())
    d = float(field_d.get())

    if d != 0:
        result = pow((a / d), 2) + pow((b / d), 3) + (c / 2)
        field_1.delete(0, tk.END)
        field_1.insert(0, str(result))
    else:
        field_1.delete(0, tk.END)
        field_1.insert(0, "Помилка при введенні даних!")

def perform_second_task():
    if field_f.get().strip() == "" or field_l.get().strip() == "" or field_k.get().strip() == "" or field_w.get().strip() == "" or field_d2.get().strip() == "":
        field_2.delete(0, tk.END)
        field_2.insert(0, "Помилка при введенні даних!")
        return

    f = float(field_f.get())
    l = float(field_l.get())
    k = float(field_k.get())
    w = float(field_w.get())
    d2 = float(field_d2.get())

    if l * k > 0:
        if f == 0:
            result = log10(l * k) + d2 * sin(w * k)
        else:
            result = cos(w * k) + log10(l * k)
        field_2.delete(0, tk.END)
        field_2.insert(0, str(result))
    else:
        field_2.delete(0, tk.END)
        field_2.insert(0, "Помилка при введенні даних!")

def perform_third_task():
    if field_b3.get().strip() == "":
        for i in range(len(field_res)):
            field_res[i].delete(0, tk.END)
            field_res[i].insert(0, "Помилка при введенні даних")
        return

    b3 = float(field_b3.get())

    for i, field in enumerate(field_res):
        result = sqrt(pow(i - 4, 2) + pow(b3, 2)) - pow(i - 4 + b3, 2)
        field.delete(0, tk.END)
        field.insert(0, str(result))

# Створення головного вікна
root = tk.Tk()
root.title("Перша лабораторна робота")
root.geometry("670x600")

# Створення вкладок
tab_control = ttk.Notebook(root)

# Перша вкладка
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Перше завдання')
tab1.grid_columnconfigure(0, weight=1)

# Добавлення елементів на першу вкладку
label_a = ttk.Label(tab1, text="Введіть значення A")
label_a.grid(row=0, column=0, sticky=tk.W)
field_a = ttk.Entry(tab1, width=10)
field_a.grid(row=0, column=1)

label_b = ttk.Label(tab1, text="Введіть значення B")
label_b.grid(row=1, column=0, sticky=tk.W)
field_b = ttk.Entry(tab1, width=10)
field_b.grid(row=1, column=1)

label_c = ttk.Label(tab1, text="Введіть значення C")
label_c.grid(row=2, column=0, sticky=tk.W)
field_c = ttk.Entry(tab1, width=10)
field_c.grid(row=2, column=1)

label_d = ttk.Label(tab1, text="Введіть значення D")
label_d.grid(row=3, column=0, sticky=tk.W)
field_d = ttk.Entry(tab1, width=10)
field_d.grid(row=3, column=1)

label_1 = ttk.Label(tab1, text="Результат 1 завдання")
label_1.grid(row=5, column=0, sticky=tk.W)
field_1 = ttk.Entry(tab1, width=5)
field_1.grid(row=5, column=1)

button_task1 = ttk.Button(tab1, text="Виконати завдання 1", command=perform_first_task)
button_task1.grid(row=6, column=0, columnspan=2)

# Друга вкладка
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Друге завдання')
tab2.grid_columnconfigure(0, weight=1)

# Добавлення елементів на другу вкладку
label_f = ttk.Label(tab2, text="Введіть значення F")
label_f.grid(row=0, column=0, sticky=tk.W)
field_f = ttk.Entry(tab2, width=10)
field_f.grid(row=0, column=1)

label_l = ttk.Label(tab2, text="Введіть значення L")
label_l.grid(row=1, column=0, sticky=tk.W)
field_l = ttk.Entry(tab2, width=10)
field_l.grid(row=1, column=1)

label_k = ttk.Label(tab2, text="Введіть значення K")
label_k.grid(row=2, column=0, sticky=tk.W)
field_k = ttk.Entry(tab2, width=10)
field_k.grid(row=2, column=1)

label_w = ttk.Label(tab2, text="Введіть значення W")
label_w.grid(row=3, column=0, sticky=tk.W)
field_w = ttk.Entry(tab2, width=10)
field_w.grid(row=3, column=1)

label_d2 = ttk.Label(tab2, text="Введіть значення D")
label_d2.grid(row=4, column=0, sticky=tk.W)
field_d2 = ttk.Entry(tab2, width=10)
field_d2.grid(row=4, column=1)

label_2 = ttk.Label(tab2, text="Результат 2 завдання")
label_2.grid(row=6, column=0, sticky=tk.W)
field_2 = ttk.Entry(tab2, width=5)
field_2.grid(row=6, column=1)

button_task2 = ttk.Button(tab2, text="Виконати завдання 2", command=perform_second_task)
button_task2.grid(row=7, column=0, columnspan=2)

# Третя вкладка
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Третє завдання')
tab3.grid_columnconfigure(0, weight=1)

# Добавлення елементів на третю вкладку
label_b3 = ttk.Label(tab3, text="Введіть значення B")
label_b3.grid(row=0, column=0, sticky=tk.W)
field_b3 = ttk.Entry(tab3, width=10)
field_b3.grid(row=0, column=1)

button_task3 = ttk.Button(tab3, text="Виконати завдання 3", command=perform_third_task)
button_task3.grid(row=1, column=0, columnspan=2)

label_3c = ttk.Label(tab3, image=photo3)
label_3c.grid(row=2, column=0, columnspan=2)

label_res = []
field_res = []

for i in range(23):
    label_res.append(ttk.Label(tab3, text=f"                    f[{i-4}] = "))
    label_res[i].grid(row=i+3, column=0, sticky=tk.W)
    field_res.append(ttk.Entry(tab3, width=5))
    field_res[i].grid(row=i+3, column=1)

root.mainloop()