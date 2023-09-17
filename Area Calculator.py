import tkinter as tk
import ttkbootstrap as ttk
from res import Calculations
from PIL import Image, ImageTk
from tkinter import filedialog



def open_dialog():
    path = filedialog.askopenfile()

# Возвращает результаты вычислений
def calcualte():
    try:
        result, error = Calculations.monte_carlo(filename=FILENAME, 
                                        height=height_int.get(), 
                                        width=width_int.get(),
                                        n=count_int.get(),
                                        iter=iterations_int.get(),
                                        round_num=round_int.get())
    except:
        return
    
    Result['text'] = f"Результат : {result} км"
    Error['text'] = f"Погрешность: ± {error} км"

    image = Image.open("img\\result.png")
    image_tk = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=image_tk)

# Проверяет введенное число
def validate_number(x):
    if x == "0" or x == "":
        return False
    else:
        return True

# Подстраивает изображение под размеры окна
def stretch_image(event):
    global resized_tk

    height = event.height
    width = event.width

    resized_image = image.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(0, 0, anchor='nw',image=resized_tk)


# Имя изображения
FILENAME = "img\\origin.png"

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
digit_func = window.register(validate_number)

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
RectangleHeight = ttk.Label(master=input_frame, text="Высота прямоугольника (км): ", padding=5)
RectangleWidth = ttk.Label(master=input_frame, text="Ширина прямоугольника (км): ", padding=5)
count = ttk.Label(master=input_frame, text="Количество точек: ", padding=5)
iterations = ttk.Label(input_frame, text="Количество итераций: ", padding=5)
RoundNum = ttk.Label(master=input_frame, text="Количество значимых цифр после запятой: ", padding=5)
Result = ttk.Label(master=output_frame, text="Результат: 0.0 км", font="Calibri 14 bold", padding=5)
Error = ttk.Label(master=output_frame, text="Погрешность: ± 0.0 км", font="Calibri 14 bold", padding=5)

# Entries
EntryHeight = ttk.Entry(master=input_frame, textvariable=height_int, width=10, validate="focus", validatecommand=(digit_func, '%P'))
EntryWidth = ttk.Entry(master=input_frame, textvariable=width_int, width=10, validate="focus", validatecommand=(digit_func, '%P'))
entry_count = ttk.Entry(master=input_frame, textvariable=count_int, width=10, validate="focus", validatecommand=(digit_func, '%P'))
entry_iterations = ttk.Entry(input_frame, textvariable=iterations_int, width=10, validate="focus", validatecommand=(digit_func, '%P'))
EntryRoundNum = ttk.Entry(master=input_frame, textvariable=round_int, width=10, validate="focus", validatecommand=(digit_func, '%P'))

# Buttons
StartButton = ttk.Button(master=window, text="Вычислить", command=calcualte)

# Image
image = Image.open(FILENAME)
image_tk = ImageTk.PhotoImage(image)

# Canvas
canvas = tk.Canvas(window, height=image.size[1], width=image.size[0], relief=tk.SUNKEN, borderwidth=1)
canvas.bind("<Configure>", stretch_image)
canvas.create_image(0, 0, anchor='nw', image=image_tk)


#=========================================================================
# Pack
#=========================================================================


# Lables
RectangleHeight.grid(row=0, column=1)
RectangleWidth.grid(row=1, column=1)
count.grid(row=2, column=1)
iterations.grid(row=3, column=1)
RoundNum.grid(row=4, column=1)
Result.pack()
Error.pack()

# Entries
EntryHeight.grid(row=0, column=2)
EntryWidth.grid(row=1, column=2)
entry_count.grid(row=2, column=2)
entry_iterations.grid(row=3, column=2)
EntryRoundNum.grid(row=4, column=2)

# Frames
menu_frame.pack()
input_frame.grid(row=0, column=0)
output_frame.grid(row=0, column=1)

# Buttons
StartButton.pack()

# Canvas
canvas.pack()


window.mainloop()