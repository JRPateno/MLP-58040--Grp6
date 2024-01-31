import cv2

img = cv2.imread("PATENO.png", cv2.IMREAD_COLOR)

cv2.imshow("JRP.jpeg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
