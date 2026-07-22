import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("images/noisy.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Add Gaussian Noise (simulate sensor noise)
noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)

# Remove noise using Gaussian Blur
denoised_image = cv2.GaussianBlur(noisy_image, (5,5), 0)

# Display images
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(denoised_image)
plt.title("Noise Reduced")
plt.axis("off")

plt.tight_layout()
plt.show()