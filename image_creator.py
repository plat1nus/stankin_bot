from PIL import Image


def create_img(body, eyes, glasses, smile):
    body_img = Image.open(body, 'r')
    eyes_img = Image.open(eyes, 'r')
    glasses_img = Image.open(glasses, 'r')
    smile_img = Image.open(smile, 'r')

    dst = Image.new('RGB', (body_img.width, body_img.height))
    dst.paste(body_img, (0, 0))
    dst.paste(eyes_img, (0, 0))
    dst.paste(glasses_img, (0, 0))
    dst.paste(smile_img, (0, 0))

    return dst


