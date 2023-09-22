import time
import random
import numpy as np
from math import sqrt
from res import ImageProcessing

def monte_carlo(filename, height, width, n, iter, round_num):

    # Засекаем время
    start_time = time.time()

    # Получаем размеры изображения
    (width_px, height_px) = ImageProcessing.get_image_size(filename)

    # Преобразуем изображение в NumPy массив
    img_array = ImageProcessing.transform_to_np_array(filename)
    
    # Инициализируем список, куда будем записывать вычисленную площади на каждой итерации
    sq_list = []

    # Площадь прямоугольника
    sq_rect = height * width

    # "Бомбардируем" изображение точками со случайными координатами (каждую точку заносим в массив dot_map)
    #  Если попадание в цель (пиксель черного цвета), то прибавляем к счетчику on_point 1
    for _ in range(iter):
        on_point = 0 
        # Создаем NumPy массив, заполненный нулями, с размерами изображения. Сюда будем записывать координаты точек
        dot_map = np.zeros((height_px, width_px))

        for _ in range(n):
            x = random.randint(0, width_px-1)
            y = random.randint(0, height_px-1)

            if (img_array[y][x] - [255, 255, 255]).all():
                on_point +=1
            
            dot_map[y][x] = 255

        # Вычисляем площадь объекта и добавляем ее в конец списка
        sq_list.append((on_point / n) * sq_rect)

    # Вычисляем среднее заничение площади объекта
    sq_average = sum(sq_list) / len(sq_list)
    if (round_num != 0): sq_average = round(sq_average, round_num)
    else: sq_average = round(sq_average)

    # Рассчитываем стандартное отклонение для этих площадей
    sum_sq = 0
    for sq in sq_list:
        sum_sq += (sq - sq_average)**2

    error = sqrt(sum_sq / iter)
    if (round_num != 0): error = round(error, round_num)
    else: error = round(error)

    # Объединяем on_point_map и miss_map c исходным изображением
    ImageProcessing.paste_map_to_image(dot_map, filename)

    return (sq_average, error, round(time.time() - start_time, 3))
    