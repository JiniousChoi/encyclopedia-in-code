from PIL import Image, ImageDraw

SIZE = 256
r = SIZE / 3

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

for x in range(SIZE):
    for y in range(SIZE):
        is_inner = (x - SIZE//2)**2 + (y - SIZE//2)**2 <= r**2
        d.point((x,y), is_inner * 255)

image.save('./circle.jpg')
