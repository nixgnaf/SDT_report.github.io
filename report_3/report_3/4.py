from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('cat1.jpg').convert('L'))
im2 = filters.gaussian_filter(im,10)

pil_im = Image.fromarray(im2)

pil_im.show()
