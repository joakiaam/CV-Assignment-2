import cv2

img_src = "../out/oppg1/"

def denoise():
    salt_pepper = cv2.imread(img_src + "salt_pepper.bmp")
    gaussion_noise = cv2.imread(img_src + "gaussion_noise.bmp")

    cv_denoised_gaussion = cv2.fastNlMeansDenoisingColored(gaussion_noise, None, 10, 10, 7, 21)
    cv_denoised_salt_pepper = cv2.medianBlur(salt_pepper, 3)

    cv2.imwrite(img_src + "cv_denoised_gaussion.bmp", cv_denoised_gaussion)
    cv2.imwrite(img_src + "cv_denoised_salt_pepper.bmp", cv_denoised_salt_pepper)

if __name__ == "__main__":    denoise()

