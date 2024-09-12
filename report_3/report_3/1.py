from PIL import Image
import os

pil_im = Image.open('cat1.jpg').convert('1')
pil_im.show()
pil_im.save('binarycat.jpg')




