import cv2
import numpy as np

img = cv2.imread("images/document.jpg")

src = np.float32([
    [100, 75],
    [555, 105],
    [505, 410],
    [70, 370]
])

dst = np.float32([
    [0, 0],
    [400, 0],
    [400, 300],
    [0, 300]
])

M = cv2.getPerspectiveTransform(src, dst)

result = cv2.warpPerspective(
    img, M, (400, 300)
)

cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()