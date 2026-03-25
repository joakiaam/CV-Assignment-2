# Computer Vision Assignment 2
1. Apply any two types of noises to a chosen image.
   1. Apply filter to remove the noise and compare the results using MSE/PSNR/SSIM
   2. Use any segmentation method (K-means, Region growing, Watershed, etc.)
before and after the noise is added. Discuss the results with respect to the results.

   or
   3. Use any feature extraction methods (Hough, HoG, SIFT etc.) before
and after the noise is added. Discuss the results with respect to the feature
detection.

```
    • No need to do both (b) and (c), but just one.
    • You may use Python/Matlab/any other options to perform this task.
    • Include the resulting image in the submission
```

# Project Structure
```
.
├── CV-Assignment-2.md
├── CV-Assignment-2.pdf
├── README.md
├── oppg1
│   ├── applynoise.py
│   ├── evaluate.py
│   └── removenoise.py
├── oppg2
│   └── segmentation.py
├── out
│   ├── oppg1
│   │   ├── cv_denoised_gaussion.bmp
│   │   ├── cv_denoised_salt_pepper.bmp
│   │   ├── gaussion_noise.bmp
│   │   └── salt_pepper.bmp
│   └── oppg2
│       ├── seg_gaussian_noisy.bmp
│       ├── seg_original.bmp
│       ├── seg_sp_noisy.bmp
│       └── segmentation_comparison.png
└── src
    ├── CV assignment_2.pdf
    ├── Task1_CV.bmp
    └── Task1a_CV.bmp
```