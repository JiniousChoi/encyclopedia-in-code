from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

p = 64

for x in range(SIZE):
    for y in range(SIZE):
        inner = (x/p + y/p) % 2
        #inner = (x//p%2 + y//p%2) % 2
        d.point((x,y), inner * 255)

image.save('./continuous_check.jpg')
