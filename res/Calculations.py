import random
import numpy as np
from res import ImageProcessing

def MonteCarlo(filename, height, width, n, round_num):

    # Получаем размеры изображения
    (width_px, height_px) = ImageProcessing.GetImageSize(filename)

    # Преобразуем изображение в NumPy массив
    img_array = ImageProcessing.TransformToNPArray(filename)
    
    # Создаем NumPy массив, заполненный нулями, с размерами изображения, куда будем ставить точки
    dot_map = np.zeros((height_px, width_px))

    # Вычисляем площадь прямоугольника в км**2 и инициализируем счетчик попаданий в цель
    SqRect = height * width
    on_point = 0

    # "Бомбардируем" изображение точками со случайными координатами (каждую точку заносим в массив dot_map)
    #  Если попадание в цель (пиксель черного цвета), то прибавляем к счетчику 1
    for _ in range(n):
        x = random.randint(0, width_px-1)
        y = random.randint(0, height_px-1)

        if (img_array[y][x] - [255, 255, 255]).all():
            on_point +=1
        
        dot_map[y][x] = 255

    # Объединяем dot_map c исходным изображением
    ImageProcessing.PasteMapToImage(dot_map, filename)

    # Возвращаем вычисленную площадь объекта
    return round((on_point / n) * SqRect, round_num)
    
#print(MonteCarlo("BlackSeaLowRes.png", 635, 1196, 1000, 2))

        