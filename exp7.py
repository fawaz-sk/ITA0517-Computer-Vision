import cv2

# Load image in grayscale
img = cv2.imread("images/car.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

# Quantization
quantized = (img // 64) * 64

cv2.imshow("Original Image", img)
cv2.imshow("Quantized Image", quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()