import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("images/car.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Improve brightness (Image Formation Model)
bright = cv2.convertScaleAbs(image_rgb, alpha=1.2, beta=40)

# Reduce noise
filtered = cv2.GaussianBlur(bright, (5,5), 0)

# Display images
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(bright)
plt.title("Brightness Enhanced")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(filtered)
plt.title("Enhanced + Noise Reduced")
plt.axis("off")

plt.tight_layout()
plt.show()
