from PIL import Image
from pylab import *

im = array(Image.open('cat1.jpg').convert('L'))

figure()

gray()

contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()



