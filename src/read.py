from PIL import Image



img = Image.open('./src/design.bmp')

pad = lambda hex_: hex_ if len(hex_) > 1 else '0' + hex_
def rgb_to_hex(r, g, b):
    return pad(hex(r)[2:]) + pad(hex(g)[2:]) + pad(hex(b)[2:])


data = img.getdata()
colors = set()
for pixel in data:
    colors.add(pixel)

print(colors)