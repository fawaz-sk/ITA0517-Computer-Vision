import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("images/street.jpeg")   # Change to street.jpg if needed

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Simulate low-light
low_light = (image * 0.3).astype(np.uint8)

# Add sensor noise
noise = np.random.normal(0, 20, low_light.shape).astype(np.int16)
noisy_image = np.clip(low_light.astype(np.int16) + noise, 0, 255).astype(np.uint8)

# Display images
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(low_light)
plt.title("Low-Light Image")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(noisy_image)
plt.title("Low-Light + Sensor Noise")
plt.axis("off")

plt.tight_layout()
plt.show()