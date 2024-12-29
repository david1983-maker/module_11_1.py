from PIL import Image
from PIL import ImageFont, ImageDraw


def new_foto(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_foto('jaguar.jpg')
im_2 = new_foto('babotka.png')

im.paste(im_2, (900, 300))

draw = ImageDraw.Draw(im)

font = ImageFont.truetype('Swiftchops.ttf', 300)
draw.text((0,0),'Leopard',font=font,fill='orange')
im.show('hhh')
