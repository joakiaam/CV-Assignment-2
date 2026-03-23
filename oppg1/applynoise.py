import cv2
import numpy as np

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussion_noise(image):
    # Generate random Gaussian noise
    mean = 0
    stddev = 25
    noise = np.zeros(image.shape, np.uint8)
    cv2.randn(noise, mean, stddev)

    # Add noise to image
    noisy_img = cv2.add(image, noise)
    return noisy_img

def apply_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    height, width = image.shape[:2]
    total_pixels = height * width
    num_salt = int(total_pixels * salt_prob)
    num_pepper = int(total_pixels * pepper_prob)

    rng = np.random.default_rng()

    # Use integer index arrays to avoid float index errors.
    salt_y = rng.integers(0, height, size=num_salt)
    salt_x = rng.integers(0, width, size=num_salt)
    pepper_y = rng.integers(0, height, size=num_pepper)
    pepper_x = rng.integers(0, width, size=num_pepper)

    if image.ndim == 2:
        noisy_image[salt_y, salt_x] = 255
        noisy_image[pepper_y, pepper_x] = 0
    else:
        noisy_image[salt_y, salt_x, :] = 255
        noisy_image[pepper_y, pepper_x, :] = 0

    return noisy_image

def main():
    image = cv2.imread('../src/Task1_CV.bmp')
    salt_and_pepper = apply_salt_and_pepper_noise(image, 0.01, 0.01)
    cv2.imwrite('../out/oppg1/salt_pepper.bmp', salt_and_pepper)
    noisy_image = apply_gaussion_noise(image)
    cv2.imwrite('../out/oppg1/gaussion_noise.bmp', noisy_image)

if __name__ == "__main__":    main()
