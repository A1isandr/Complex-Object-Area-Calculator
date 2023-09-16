from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from res import Calculations

def OpenDialog():
    path = filedialog.askopenfile()

def Start():
    Result['text'] = "Результат :", Calculations.MonteCarlo(filename=filename, 
                                                height=HeightInt.get(), 
                                                width=WidthInt.get(),
                                                n=IterattionInt.get(),
                                                round_num=RoundInt.get()), "км"

    image = Image.open("img\\Result.png")
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)

filename = "img\\Origin.png"

window = Tk()
window.title("Вычисление Площади Объекта Методом Монте-Карло")

HeightInputFrame = Frame(master=window)
WidthInputFrame = Frame(master=window)
IterattionFrame = Frame(master=window)
RoundInputFrame = Frame(master=window)
StartFrame = Frame(master=window)
ResultFrame = Frame(master=window)

HeightInt = IntVar()
WidthInt = IntVar()
IterattionInt = IntVar()
RoundInt = IntVar()
ResultDouble = DoubleVar()

RectangleHeight = Label(master=HeightInputFrame, text="Высота прямоугольника (км): ")
RectangleWidth = Label(master=WidthInputFrame, text="Ширина прямоугольника (км): ")
Iterattions = Label(master=IterattionFrame, text="Количество Итераций: ")
RoundNum = Label(master=RoundInputFrame, text="Количество значимых цифр после запятой: ")
Result = Label(master=ResultFrame, text=f"Результат: 0.0 км")

EntryHeight = Entry(master=HeightInputFrame, textvariable=HeightInt)
EntryWidth = Entry(master=WidthInputFrame, textvariable=WidthInt)
EntryIterattions = Entry(master=IterattionFrame, textvariable=IterattionInt)
EntryRoundNum = Entry(master=RoundInputFrame, textvariable=RoundInt)

StartButton = Button(master=StartFrame, text="Вычислить", command=Start)

RectangleHeight.pack(side="left")
RectangleWidth.pack(side="left")
Iterattions.pack(side="left")
RoundNum.pack(side="left")
Result.pack()

EntryHeight.pack()
EntryWidth.pack()
EntryIterattions.pack()
EntryRoundNum.pack()

StartButton.pack()

HeightInputFrame.pack()
WidthInputFrame.pack()
IterattionFrame.pack()
RoundInputFrame.pack()
StartFrame.pack()
ResultFrame.pack()


#Добавим изображение
image = Image.open(filename)
canvas = Canvas(window, height=image.size[1], width=image.size[0])
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.pack()

#Добавим метку


window.mainloop()