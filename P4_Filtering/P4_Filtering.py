import cv2
import numpy as np

# read image as grayscale
img = cv2.imread('P5_EdgeEnchancement/coins.png', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 200, 200)

cv2.imwrite("P5_EdgeEnchancement/coins_edges.png", edges)

# # show results
# cv2.imshow("K_thresh", thresh)
# cv2.imshow("K_morph", morph)
# cv2.imshow("K_letter", letter)
cv2.imshow("coins_edges", edges)
cv2.waitKey(0)