import cv2
import numpy as np

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussion_noise(img):
    # Generate random Gaussian noise
    mean = 0
    stddev = 25
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, stddev)

    # Add noise to image
    noisy_img = cv2.add(img, noise)
    return noisy_img

def apply_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = image.copy()
    total_pixels = image.size
    num_salt = int(total_pixels * salt_prob)
    num_pepper = int(total_pixels * pepper_prob)

    # Add salt noise
    for _ in range(num_salt):
        x = cv2.randu(0, image.shape[1])
        y = cv2.randu(0, image.shape[0])
        noisy_image[y, x] = 255

    # Add pepper noise
    for _ in range(num_pepper):
        x = cv2.randu(0, image.shape[1])
        y = cv2.randu(0, image.shape[0])
        noisy_image[y, x] = 0

    return noisy_image

def main():
    image = cv2.imread('../src/Task1_CV.bmp')
    #salt_and_pepper = apply_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01)
    #cv2.imwrite('salt_and_pepper.jpg', salt_and_pepper)
    noisy_image = apply_gaussion_noise(image)
    cv2.imwrite('noisy_image.jpg', noisy_image)

if __name__ == "__main__":    main()
