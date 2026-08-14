import cv2
import numpy as np

cap = cv2.VideoCapture("videos/road.mp4")

src = np.float32([
    [100, 100],
    [540, 100],
    [500, 400],
    [100, 400]
])

dst = np.float32([
    [0, 0],
    [400, 0],
    [400, 300],
    [0, 300]
])

M = cv2.getPerspectiveTransform(src, dst)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    result = cv2.warpPerspective(
        frame, M, (400, 300)
    )

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Video", result)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()