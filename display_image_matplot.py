import numpy as np
import cv2
from matplotlib import pyplot as plt

imgdir = "img/"

# load colour image in grayscale
img = cv2.imread(imgdir + "image.jpeg", 0)
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])
plt.show()
