import numpy as np
from PIL import Image


def GetImageSize(filename):
    with Image.open(filename) as img:
        img.load()
    
    return img.size

def TransformToNPArray(filename):
    with Image.open(filename) as img:
        img.load()
    
    return np.asarray(img)
    
def GetTreshold(filename):
    with Image.open(filename) as img:
        img.load()

    threshold = 0
    img_treshold = img.convert('L').point(
        lambda x: 255 if x > threshold else 0
    )

    return img_treshold
    
def PasteMapToImage(map, filename):
    (width_px, height_px) = GetImageSize(filename)

    img = Image.merge("RGB", (Image.fromarray(map).convert('L'),
                        Image.fromarray(np.zeros((height_px, width_px))).convert('L'),
                        Image.fromarray(np.zeros((height_px, width_px))).convert('L')))
    
    img.save("img\\DotMap.png")
    
    img_treshold = GetTreshold("img\\DotMap.png")

    with Image.open(filename) as orig_img:
        orig_img.load()

    orig_img.paste(img, (0, 0), img_treshold)

    orig_img.save("img\\Result.png")
