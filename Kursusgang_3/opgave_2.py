import cv2
import numpy as np

def add_gaussian_noise(image, mean, sigma):
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy_image = np.uint8(np.clip(image + gauss, 0, 255))
    return noisy_image

def mean_filter(image):
    return cv2.blur(image, (3, 3))

def median_filter(image):
    return cv2.medianBlur(image, 3)

original_image = cv2.imread(r'Kursusgang_3\lena.jpg', cv2.IMREAD_GRAYSCALE)

sigma = 25
noisy_image = add_gaussian_noise(original_image, 0, sigma)

mean_filtered_image = mean_filter(noisy_image)

median_filtered_image = median_filter(noisy_image)

cv2.imshow("Originalt Billede", original_image)
cv2.imshow("Støjfuldt Billede", noisy_image)
cv2.imshow("Middelværdifiltreret Billede", mean_filtered_image)
cv2.imshow("Medianfiltreret Billede", median_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()