from captcha.image import ImageCaptcha
from random import randint
from datetime import datetime

def generate_captcha():
    curr = datetime.now().strftime('%H.%M.%S.%d.%m.%Y')
    image = ImageCaptcha()
    key = str(randint(1000,9999))
    data = image.generate(key)
    return data, key

