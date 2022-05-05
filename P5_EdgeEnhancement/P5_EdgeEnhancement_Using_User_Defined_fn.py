import cv2
import numpy as np

# read image as grayscale
img = cv2.imread('P5_EdgeEnhancement/coins.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('',img)
edges = cv2.Canny(img, 200, 200)

cv2.imwrite("P5_EdgeEnhancement/Result/coins_edges.png", edges)


cv2.imshow("coins_edges", edges)
cv2.waitKey(0)