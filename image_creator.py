from PIL import Image
from pospelik import Pospelik

user = Pospelik()


def get_transparent_bg_img(image: Image):
    image = image.convert('RGBA')
    # Transparency
    newImage = []
    for item in image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)
    image.putdata(newImage)
    return image


def create_img(user: Pospelik = Pospelik()):
    body_img = get_transparent_bg_img(open(user.body_path, 'r'))
    eyes_img = get_transparent_bg_img(open(user.eyes_path, 'r'))
    glasses_img = get_transparent_bg_img(open(user.glasses_path, 'r'))
    smile_img = get_transparent_bg_img(open(user.smile_path, 'r'))

    dst = Image.new('RGB', (body_img.width, body_img.height))
    dst.paste(body_img)
    dst.paste(eyes_img)
    dst.paste(glasses_img)
    dst.paste(smile_img)

    print(dst.size)
    return dst


if __name__ == "__main__":
    photo = create_img(user)
    photo.save("q.png")
