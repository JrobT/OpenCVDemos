import numpy as np
import cv2

imgdir = "img/"

# load colour image in grayscale
img = cv2.imread(imgdir + "image.jpeg", 0)
cv2.imshow("Image", img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite(imgdir + "imagegray.png", img)
    cv2.destroyAllWindows()
