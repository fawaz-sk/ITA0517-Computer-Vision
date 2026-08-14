import cv2
import numpy as np

img = cv2.imread("images/house.jpg")

src = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

dst = np.float32([
    [20, 80],
    [220, 60],
    [80, 220]
])

M = cv2.getAffineTransform(src, dst)

result = cv2.warpAffine(
    img, M, (img.shape[1], img.shape[0])
)

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()