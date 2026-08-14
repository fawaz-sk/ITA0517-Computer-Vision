import cv2

img = cv2.imread("images/flower.jpg")

clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Clockwise", clockwise)
cv2.imshow("Counter Clockwise", counter)

cv2.waitKey(0)
cv2.destroyAllWindows()