import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def apply_kmeans_segmentation(image, num_clusters=5):
    # Convert image to RGB for processing
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Reshape image to be a list of pixels
    pixel_values = image_rgb.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    
    # Define criteria and apply K-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert back to uint8
    centers = np.uint8(centers)
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image_rgb.shape)
    
    # Reshape labels back to image shape
    labels = labels.reshape(image.shape[:2])
    
    return segmented_image, labels, centers



def calculate_segmentation_quality(image, num_clusters):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixel_values = image_rgb.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, label_ref, centers = cv2.kmeans(pixel_values, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Calculate within-cluster sum of squares
    wcss = 0
    for i in range(num_clusters):
        cluster_points = pixel_values[label_ref.flatten() == i]
        if len(cluster_points) > 0:
            wcss += np.sum((cluster_points - centers[i])**2)
    
    return wcss

def segment_and_compare():
    # Load original image
    image_path = '../src/Task1_CV.bmp'
    original_image = cv2.imread(image_path)
    
    if original_image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    # Load pre-generated noisy images from Task 1
    gaussian_noisy = cv2.imread('../out/oppg1/gaussion_noise.bmp')
    sp_noisy = cv2.imread('../out/oppg1/salt_pepper.bmp')

    num_clusters = 5
    
    # 1. Segmentation on original image
    print("Processing original image...")
    seg_original, labels_original, centers_original = apply_kmeans_segmentation(original_image, num_clusters)
    
    # 2. Segmentation on Gaussian noisy image (from Task 1)
    print("Segmenting Gaussian noisy image (from Task 1)...")
    seg_gaussian_noisy, labels_gaussian, centers_gaussian = apply_kmeans_segmentation(gaussian_noisy, num_clusters)
    
    # 3. Segmentation on Salt and Pepper noisy image (from Task 1)
    print("Segmenting salt and pepper noisy image (from Task 1)...")
    seg_sp_noisy, labels_sp, centers_sp = apply_kmeans_segmentation(sp_noisy, num_clusters)
    
    # Calculate quality metrics
    print("\nCalculating segmentation quality metrics...")
    quality_original = calculate_segmentation_quality(original_image, labels_original, num_clusters)
    quality_gaussian = calculate_segmentation_quality(gaussian_noisy, labels_gaussian, num_clusters)
    quality_sp = calculate_segmentation_quality(sp_noisy, labels_sp, num_clusters)
    
    print(f"\nSegmentation Quality (Within-Cluster Sum of Squares):")
    print(f"Original Image: {quality_original:.2f}")
    print(f"Gaussian Noisy Image: {quality_gaussian:.2f}")
    print(f"Salt & Pepper Noisy Image: {quality_sp:.2f}")
    
    # Save segmented images
    output_dir = '../out/oppg2/'
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    cv2.imwrite(output_dir + 'seg_original.bmp', cv2.cvtColor(seg_original, cv2.COLOR_RGB2BGR))
    cv2.imwrite(output_dir + 'seg_gaussian_noisy.bmp', cv2.cvtColor(seg_gaussian_noisy, cv2.COLOR_RGB2BGR))
    cv2.imwrite(output_dir + 'seg_sp_noisy.bmp', cv2.cvtColor(seg_sp_noisy, cv2.COLOR_RGB2BGR))
    
    print(f"\nSegmented images saved to {output_dir}")
    
    # Visualize results
    visualize_segmentation(original_image, seg_original, gaussian_noisy, seg_gaussian_noisy, 
                          sp_noisy, seg_sp_noisy, quality_original, quality_gaussian, quality_sp)

def visualize_segmentation(original, seg_original, gaussian_noisy, seg_gaussian, 
                          sp_noisy, seg_sp, q_orig, q_gauss, q_sp):
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    
    # Convert BGR to RGB for display
    axes[0, 0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(seg_original)
    axes[0, 1].set_title(f'Segmented Original\n(Quality: {q_orig:.0f})')
    axes[0, 1].axis('off')
    
    axes[1, 0].imshow(cv2.cvtColor(gaussian_noisy, cv2.COLOR_BGR2RGB))
    axes[1, 0].set_title('Gaussian Noisy Image')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(seg_gaussian)
    axes[1, 1].set_title(f'Segmented Gaussian Noisy\n(Quality: {q_gauss:.0f})')
    axes[1, 1].axis('off')
    
    axes[2, 0].imshow(cv2.cvtColor(sp_noisy, cv2.COLOR_BGR2RGB))
    axes[2, 0].set_title('Salt & Pepper Noisy Image')
    axes[2, 0].axis('off')
    
    axes[2, 1].imshow(seg_sp)
    axes[2, 1].set_title(f'Segmented Salt & Pepper\n(Quality: {q_sp:.0f})')
    axes[2, 1].axis('off')
    
    plt.tight_layout()
    plt.savefig('../out/oppg2/segmentation_comparison.png', dpi=150, bbox_inches='tight')
    print("Visualization saved to ../out/oppg2/segmentation_comparison.png")
    plt.close()

if __name__ == "__main__":
    segment_and_compare()

