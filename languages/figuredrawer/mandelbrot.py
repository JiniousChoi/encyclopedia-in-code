from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

def mandel(c):
    z = 0
    for h in range(20):
        z = z ** 2 + c
        if abs(z) > 2:
            break
    return abs(z) < 2

for x in range(SIZE):
    r = x / 110.0 - 1.6
    for y in range(SIZE):
        i = y / 110.0 - 1.2
        d.point((x,y), mandel(complex(r, i)) * 255)

image.save('./mandelbrot.jpg')
