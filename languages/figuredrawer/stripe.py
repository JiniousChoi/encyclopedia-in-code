from PIL import Image, ImageDraw

SIZE = 256
UNIT = SIZE // 11

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

for x in range(SIZE):
    is_white_pillar = x % UNIT > UNIT/6
    for y in range(SIZE):
        d.point((x,y), is_white_pillar * 255)

image.save('./stripe.jpg')
