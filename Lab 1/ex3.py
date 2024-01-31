import cv2

path = r'PATENO.png'

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()