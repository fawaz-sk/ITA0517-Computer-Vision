import cv2
import numpy as np

img = cv2.imread("images/board.jpg")

src = np.float32([
    [90, 80],
    [555, 105],
    [520, 405],
    [70, 375]
])

dst = np.float32([
    [0, 0],
    [400, 0],
    [400, 300],
    [0, 300]
])

A = []

for (x, y), (u, v) in zip(src, dst):

    A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
    A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])

A = np.array(A)

U, S, Vt = np.linalg.svd(A)

H = Vt[-1].reshape(3, 3)

H = H / H[2, 2]

print("DLT Homography Matrix:")
print(H)

result = cv2.warpPerspective(
    img, H, (400, 300)
)

cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()