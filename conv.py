from PIL import Image
import io

from PIL import Image

def convert_img_format(img, output_format):
    """
    Конвертирует объект изображения Pillow (включая HEIC) в указанный формат.
    """
    # Проверяем, что объект — это изображение
    if not isinstance(img, Image.Image):
        raise TypeError("convert_img_format ожидает объект PIL.Image, а не путь к файлу")

    # Конвертируем в RGB, если нужно
    if img.mode in ("RGBA", "P", "LA"):
        img = img.convert("RGB")

    return img

