import cv2
import matplotlib.pyplot as plt

img = cv2.imread("PATENO.png")
plt.imshow(img)

plt.waitforbuttonpress()
plt.close("all")