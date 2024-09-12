from PIL import Image
from numpy import *

im = array(Image.open('cat1.jpg').convert('L'))

im2 = 255 - im
pil_im = Image.fromarray(im2)
pil_im.show()
im3 = (100.0/255) * im + 100
pil_im = Image.fromarray(im3)
pil_im.show()
im4 = 255.0 * (im/255.0)**2
pil_im = Image.fromarray(im4)
pil_im.show()
