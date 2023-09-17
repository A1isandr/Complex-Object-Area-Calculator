import numpy as np
from PIL import Image

# Возвращает размер изображения
def get_image_size(filename):
    with Image.open(filename) as img:
        img.load()
    
    return img.size

# Трансформирует изображение в NumPy массив и возвращает его
def transform_to_np_array(filename):
    with Image.open(filename) as img:
        img.load()
    
    return np.asarray(img)
    
# Возвращает версию изображения, где всем пикселям присваевается только строго черное или строго белое значение
def get_treshold(filename):
    with Image.open(filename) as img:
        img.load()

    threshold = 0
    img_treshold = img.convert('L').point(
        lambda x: 255 if x > threshold else 0
    )

    return img_treshold
    
# Вставляет карту точек в исходное изображение
def paste_map_to_image(map, filename):
    (width_px, height_px) = get_image_size(filename)

    img = Image.merge("RGB", (Image.fromarray(map).convert('L'),
                            Image.fromarray(np.zeros((height_px, width_px))).convert('L'),
                            Image.fromarray(np.zeros((height_px, width_px))).convert('L')))
    
    img.save(f"img\\dot_map.png")
    
    img_treshold = get_treshold(f"img\\dot_map.png")

    with Image.open(filename) as orig_img:
        orig_img.load()

    orig_img.paste(img, (0, 0), img_treshold)

    orig_img.save("img\\result.png")
