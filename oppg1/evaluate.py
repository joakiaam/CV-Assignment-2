import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def evaluate(original, denoised):
    mse = np.mean((original.astype(np.float64) - denoised.astype(np.float64)) ** 2)
    psnr = 10 * np.log10(255**2 / mse) if mse > 0 else float('inf')
    gray_o = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    gray_d = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)
    s = ssim(gray_o, gray_d, data_range=255)
    return {"MSE": round(mse, 2), "PSNR": round(psnr, 2), "SSIM": round(s, 4)}

if __name__ == "__main__":
    img_src = "../out/oppg1/"
    original = cv2.imread('../src/Task1_CV.bmp')
    denoised_gaussion = cv2.imread(img_src + "cv_denoised_gaussion.bmp")
    denoised_salt_pepper = cv2.imread(img_src + "cv_denoised_salt_pepper.bmp")

    print("Evaluation for Gaussian Noise Denoising:")
    print(evaluate(original, denoised_gaussion))

    print("\nEvaluation for Salt and Pepper Noise Denoising:")
    print(evaluate(original, denoised_salt_pepper))
