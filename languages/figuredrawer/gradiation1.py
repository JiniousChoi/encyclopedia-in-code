from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

for x in range(SIZE):
    for y in range(SIZE):
        d.point((x,y), x)

image.save('./gradiation1.jpg')
