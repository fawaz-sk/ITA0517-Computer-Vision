import cv2
import numpy as np

img = cv2.imread("images/poster.jpg")

src = np.float32([
    [95, 90],
    [545, 70],
    [525, 390],
    [75, 410]
])

dst = np.float32([
    [0, 0],
    [400, 0],
    [400, 300],
    [0, 300]
])

H, _ = cv2.findHomography(src, dst)

result = cv2.warpPerspective(
    img, H, (400, 300)
)

print("Homography Matrix:")
print(H)

cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()