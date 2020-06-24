from PIL import Image

img = Image.open('./pokedex/pikachu.jpg')

print(img.format)
print(img.size)
print(img.mode)