from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

# print(img.format)
# print(img.size)
# print(img.mode)

# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save("smooth.png", 'png')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", 'png')
