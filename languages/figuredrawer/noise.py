from PIL import Image, ImageDraw
from random import randint

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

for x in range(SIZE):
    for y in range(SIZE):
        is_white = randint(0,1)
        d.point((x,y), is_white * 255)

image.save('./noise.jpg')
