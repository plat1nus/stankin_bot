from PIL import Image
from pospelik import Pospelik


def create_img(user: Pospelik = Pospelik()):
    body_img = Image.open(user.body_path, 'r')
    eyes_img = Image.open(user.eyes_path, 'r')
    glasses_img = Image.open(user.glasses_path, 'r')
    smile_img = Image.open(user.smile_path, 'r')

    dst = Image.new('RGB', (body_img.width, body_img.height))
    dst.paste(body_img, (0, 0))
    dst.paste(eyes_img, (0, 0))
    dst.paste(glasses_img, (0, 0))
    dst.paste(smile_img, (0, 0))

    return dst.resize(size=(64, 64))
