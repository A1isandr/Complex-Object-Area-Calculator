from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from res import Calculations

def OpenDialog():
    path = filedialog.askopenfile()

def Start():
    Result['text'] = "Результат :", Calculations.monte_carlo(filename=filename, 
                                                height=height_int.get(), 
                                                width=width_int.get(),
                                                n=count_int.get(),
                                                iter=iterations_int.get(),
                                                round_num=round_int.get()), "км"

    image = Image.open("img\\result.png")
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)

filename = "img\\origin.png"

window = Tk()
window.title("Вычисление Площади Объекта Методом Монте-Карло")

# Frames
height_input_frame = Frame(window)
width_input_frame = Frame(window)
count_input_frame = Frame(window)
iterations_input_frame = Frame(window)
round_input_frame = Frame(window)
start_frame = Frame(window)
result_frame = Frame(window)

# Variables
height_int = IntVar()
width_int = IntVar()
count_int = IntVar()
iterations_int = IntVar()
round_int = IntVar()
result_double = DoubleVar()

# Lables
RectangleHeight = Label(master=height_input_frame, text="Высота прямоугольника (км): ")
RectangleWidth = Label(master=width_input_frame, text="Ширина прямоугольника (км): ")
count = Label(master=count_input_frame, text="Количество точек: ")
iterations = Label(iterations_input_frame, text="Количество итераций: ")
RoundNum = Label(master=round_input_frame, text="Количество значимых цифр после запятой: ")
Result = Label(master=result_frame, text="Результат: 0.0 км")

# Entries
EntryHeight = Entry(master=height_input_frame, textvariable=height_int)
EntryWidth = Entry(master=width_input_frame, textvariable=width_int)
entry_count = Entry(master=count_input_frame, textvariable=count_int)
entry_iterations = Entry(iterations_input_frame, textvariable=iterations_int)
EntryRoundNum = Entry(master=round_input_frame, textvariable=round_int)

# Buttons
StartButton = Button(master=start_frame, text="Вычислить", command=Start)

#=========================================================================
# Pack
#=========================================================================

# Lables
RectangleHeight.pack(side="left")
RectangleWidth.pack(side="left")
count.pack(side="left")
iterations.pack(side="left")
RoundNum.pack(side="left")
Result.pack()

# Entries
EntryHeight.pack()
EntryWidth.pack()
entry_count.pack()
entry_iterations.pack()
EntryRoundNum.pack()

# Buttons
StartButton.pack()

# Frames
height_input_frame.pack()
width_input_frame.pack()
count_input_frame.pack()
iterations_input_frame.pack()
round_input_frame.pack()
start_frame.pack()
result_frame.pack()


#Добавим изображение
image = Image.open(filename)
canvas = Canvas(window, height=image.size[1], width=image.size[0])
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.pack()

#Добавим метку


window.mainloop()