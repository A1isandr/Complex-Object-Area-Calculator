import tkinter as tk
import ttkbootstrap as ttk
from res import Calculations
from PIL import Image, ImageTk
from tkinter import filedialog



# Подстраивает изображение под размеры окна
def stretch_image(event):
    global resized_tk

    height = event.height
    width = event.width

    image = Image.open(filename)
    resized_image = image.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(0, 0, anchor='nw',image=resized_tk)

def open_dialog():
    path = filedialog.askopenfile()

    # Проверяет введенное число
def check_not_empty(x):
    if x == "0" or x == "":
        return False
    else:
        return True

# Возвращает результаты вычислений
def calcualte():
    global filename

    filename = "img\\origin.png"

    try:
        _result, _error, _runtime = Calculations.monte_carlo(filename=filename, 
                                        height=abs(height_int.get()), 
                                        width=abs(width_int.get()),
                                        n=abs(count_int.get()),
                                        iter=abs(iterations_int.get()),
                                        round_num=abs(round_int.get()))
    except ZeroDivisionError:
        print("Некоторые поля не принимают нули в качестве аргументов")
        return
    
    result['text'] = f"Результат: {_result} км^2"
    error['text'] = f"Погрешность: ± {_error} км^2"
    runtime['text'] = f"Затраченное время: {_runtime} с"

    filename = "img\\result.png"
    image = Image.open(filename)
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw',image=image_tk)



# Имя изображения
filename = "img\\origin.png"

# Характеристики окна
window = ttk.Window(themename="lumen")
window.title("Area Calculator")
window.iconbitmap("res\\calculator.ico")
window.minsize(700, 300)

# Styles
style = ttk.Style()
style.configure("TButton", font=("Calibri bold", 14))
style.configure("TLabel", font=("Calibri", 14))

# Validate
check_func = window.register(check_not_empty)

# Frames
menu_frame = ttk.Frame(window, padding=10)
input_frame = ttk.Frame(menu_frame, relief=tk.SUNKEN, borderwidth=2, padding=10)
output_frame = ttk.Frame(menu_frame, padding=10)

# Variables
height_int = tk.IntVar()
width_int = tk.IntVar()
count_int = tk.IntVar()
iterations_int = tk.IntVar()
round_int = tk.IntVar()
result_double = tk.DoubleVar()

# Lables
rectangle_height = ttk.Label(master=input_frame, text="Высота прямоугольника (км): ", padding=5)
rectangle_width = ttk.Label(master=input_frame, text="Ширина прямоугольника (км): ", padding=5)
count = ttk.Label(master=input_frame, text="Количество точек: ", padding=5)
iterations = ttk.Label(input_frame, text="Количество итераций: ", padding=5)
round_num = ttk.Label(master=input_frame, text="Округлить до: ", padding=5)
result = ttk.Label(master=output_frame, text="Результат: 0 км^2", font="Calibri 14 bold", padding=5)
error = ttk.Label(master=output_frame, text="Погрешность: ± 0 км^2", font="Calibri 14 bold", padding=5)
runtime = ttk.Label(output_frame, text="Затраченное время: 0 c", font="Calibri 12", padding=5)

# Entries
entry_height = ttk.Entry(master=input_frame, textvariable=height_int, width=10, validate="focus", validatecommand=(check_func, '%P'))
entry_width = ttk.Entry(master=input_frame, textvariable=width_int, width=10, validate="focus", validatecommand=(check_func, '%P'))
entry_count = ttk.Entry(master=input_frame, textvariable=count_int, width=10, validate="focus", validatecommand=(check_func, '%P'))
entry_iterations = ttk.Entry(input_frame, textvariable=iterations_int, width=10, validate="focus", validatecommand=(check_func, '%P'))
entry_round_num = ttk.Entry(master=input_frame, textvariable=round_int, width=10, validate="focus")

# Buttons
start_button = ttk.Button(master=window, text="Вычислить", command=calcualte)

# Canvas
image = Image.open(filename)
image_tk = ImageTk.PhotoImage(image)
canvas = tk.Canvas(window, height=image.size[1], width=image.size[0], relief=tk.SUNKEN, borderwidth=1)
canvas.bind("<Configure>", stretch_image)
canvas.create_image(0, 0, anchor='nw',image=image_tk)


#=========================================================================
# Pack
#=========================================================================


# Lables
rectangle_height.grid(row=0, column=1)
rectangle_width.grid(row=1, column=1)
count.grid(row=2, column=1)
iterations.grid(row=3, column=1)
round_num.grid(row=4, column=1)
result.pack()
error.pack()
runtime.pack()

# Entries
entry_height.grid(row=0, column=2)
entry_width.grid(row=1, column=2)
entry_count.grid(row=2, column=2)
entry_iterations.grid(row=3, column=2)
entry_round_num.grid(row=4, column=2)

# Frames
menu_frame.pack()
input_frame.grid(row=0, column=0)
output_frame.grid(row=0, column=1)

# Buttons
start_button.pack()

# Canvas
canvas.pack()


window.mainloop()