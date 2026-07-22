import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread("images/medical.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# -------------------------------
# Pixel Resolution
# -------------------------------
low_resolution = cv2.resize(image, (128, 128))
high_resolution = cv2.resize(low_resolution, (512, 512))

# -------------------------------
# Intensity Resolution
# -------------------------------
intensity_4bit = (image // 16) * 16      # 16 Gray Levels (4-bit)
intensity_2bit = (image // 64) * 64      # 4 Gray Levels (2-bit)

# -------------------------------
# Display Results
# -------------------------------
plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(high_resolution, cmap='gray')
plt.title("Reduced Pixel Resolution")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(intensity_4bit, cmap='gray')
plt.title("4-bit Intensity Resolution")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(intensity_2bit, cmap='gray')
plt.title("2-bit Intensity Resolution")
plt.axis("off")

plt.tight_layout()
plt.show()