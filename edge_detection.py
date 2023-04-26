import numpy as np
import cv2
import random
from matplotlib import pyplot as plt

def create_synthetic_image(width, height, background_intensity, color_intensity):
    image = np.full((height, width, 3), background_intensity, dtype=np.uint8)
    square_size = 100
    circle_radius = 50
    top_left = (width // 4 - square_size // 2, height // 2 - square_size // 2)
    bottom_right = (top_left[0] + square_size, top_left[1] + square_size)
    cv2.rectangle(image, top_left, bottom_right, color_intensity, -1)
    circle_center = (3 * width // 4, height // 2)
    cv2.circle(image, circle_center, circle_radius, color_intensity, -1)
    return image

def apply_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 100, 200)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    sobel = np.hypot(sobelx, sobely)
    sobel = (sobel / np.max(sobel) * 255).astype(np.uint8)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = np.abs(laplacian)
    laplacian = (laplacian / np.max(laplacian) * 255).astype(np.uint8)

    return canny, sobel, laplacian

def evaluate_edge_detection(image, edge_image):
    ground_truth_edges = np.zeros(image.shape[:2], dtype=np.uint8)
    ground_truth_edges[100:200, 200:300] = 255
    ground_truth_edges[50:250, 400:450] = 255
    ground_truth_edges[50:250, 450:500] = 255
    ground_truth_edges[50:100, 400:500] = 255
    ground_truth_edges[200:250, 400:500] = 255

    precision = np.sum((edge_image == 255) & (ground_truth_edges == 255)) / np.sum(edge_image == 255)
    recall = np.sum((edge_image == 255) & (ground_truth_edges == 255)) / np.sum(ground_truth_edges == 255)

    return precision, recall

def add_noise(image, noise_intensity):
    noisy_image = image.copy()
    noise = np.random.randint(-noise_intensity, noise_intensity + 1, image.shape, dtype=np.int32)
    noisy_image = np.clip(noisy_image.astype(np.int32) + noise, 0, 255).astype(np.uint8)
    return noisy_image

def display_images(images, titles):
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(15, 6))
    for ax, img, title in zip(axes.flatten(), images, titles):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
    plt.show()

width = 600 
height = 300
background_intensity = 50
color_intensity = (0, 255, 0)

# call the functions we created above
image = create_synthetic_image(width, height, background_intensity, color_intensity)
canny, sobel, laplacian = apply_edge_detection(image)

# performance eval
canny_precision, canny_recall = evaluate_edge_detection(image, canny)
sobel_precision, sobel_recall = evaluate_edge_detection(image, sobel)
laplacian_precision, laplacian_recall = evaluate_edge_detection(image, laplacian)

print("Canny Precision:", canny_precision, "Recall:", canny_recall)
print("Sobel Precision:", sobel_precision, "Recall:", sobel_recall)
print("Laplacian Precision:", laplacian_precision, "Recall:", laplacian_recall)

# add noise using rng from 1 to 30 inclusive
a = 1
b = 30
noise_intensity = random.randint(a, b)
print("Intensity value is", noise_intensity)
noisy_image = add_noise(image, noise_intensity)

# apply edge detection to new noisy image
noisy_canny, noisy_sobel, noisy_laplacian = apply_edge_detection(noisy_image)

# eval noisy image
noisy_canny_precision, noisy_canny_recall = evaluate_edge_detection(noisy_image, noisy_canny)
noisy_sobel_precision, noisy_sobel_recall = evaluate_edge_detection(noisy_image, noisy_sobel)
noisy_laplacian_precision, noisy_laplacian_recall = evaluate_edge_detection(noisy_image, noisy_laplacian)

print("Noisy Canny Precision:", noisy_canny_precision, "Recall:", noisy_canny_recall)
print("Noisy Sobel Precision:", noisy_sobel_precision, "Recall:", noisy_sobel_recall)
print("Noisy Laplacian Precision:", noisy_laplacian_precision, "Recall:", noisy_laplacian_recall)

# display using our function with matplotlib
images = [image, noisy_image, canny, noisy_canny, sobel, noisy_sobel, laplacian, noisy_laplacian]
titles = ['Original Image', 'Noisy Image',
            'Canny Edges', 'Noisy Canny Edges',
            'Sobel Edges', 'Noisy Sobel Edges',
            'Laplacian Edges', 'Noisy Laplacian Edges']

display_images(images, titles)
