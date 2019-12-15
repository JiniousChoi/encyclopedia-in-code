from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

m = SIZE // 4

for x in range(SIZE):
    for y in range(SIZE):
        is_inner_square = x in range(m, SIZE-m) and y in range(m, SIZE-m)
        d.point((x,y), is_inner_square * 255)

image.save('./square.jpg')
