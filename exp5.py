import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("images/object.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Simulate low resolution (low sampling)
low_res = cv2.resize(image, (100, 100))

# Restore to original size for comparison
restored = cv2.resize(low_res, (image.shape[1], image.shape[0]))

# Display images
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(low_res)
plt.title("Low Resolution")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(restored)
plt.title("Restored Image")
plt.axis("off")

plt.tight_layout()
plt.show()