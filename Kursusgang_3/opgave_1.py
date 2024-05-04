import cv2 as cv
import numpy as np
import random

def add_impulsive_noise(image, noise_ratio):
    noisy_image = np.copy(image)
    height, width = noisy_image.shape

    num_noise = int(np.ceil(noise_ratio * image.size))

    for _ in range(num_noise):
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        intensity = random.randint(0, 255)
        noisy_image[x, y] = intensity

    return noisy_image

def mean_filter(image):
    return cv.blur(image, (3, 3))

def median_filter(image):
    return cv.medianBlur(image, 3)

original_image = cv.imread(r'Kursusgang_3\lena.jpg', cv.IMREAD_GRAYSCALE)

noisy_image = add_impulsive_noise(original_image, noise_ratio=0.2)

mean_filtered_image = mean_filter(noisy_image)

median_filtered_image = median_filter(noisy_image)

cv.imshow("Originalt Billede", original_image)
cv.imshow("Støjfuldt Billede", noisy_image)
cv.imshow("Middelværdifiltreret Billede", mean_filtered_image)
cv.imshow("Medianfiltreret Billede", median_filtered_image)
cv.waitKey(0)
cv.destroyAllWindows()