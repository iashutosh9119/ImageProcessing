import numpy as np
import cv2
import matplotlib.pyplot as plt

# img = cv2.imread('P5_EdgeEnhancement/coins.png')
img = cv2.imread('P5_EdgeEnhancement/cameraman.tif')

cv2.imshow('Before',img)
coins = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
coins_temp = np.zeros(coins.shape)
coins_temp2 = np.zeros(coins.shape)
print(coins.shape)

# sobel = [   [-1, 0, 1], 
#             [-1, 0, 1],
#             [-1, 0, 1] ]
sobel = [   [1, 0, -1], 
            [2, 0, -2],
            [1, 0, -1] ]
sobel2 = [  [1, 2, 1], 
            [0, 0, 0],
            [-1, -2, -1] ]

for i in range(3,(coins.shape[0]-3)):
    for j in range(3,(coins.shape[1]-3)):
        coins_temp[i+1,j+1] = ((sobel[0][0]*coins[i,j]) + (sobel[0][1]*coins[i,j+1]) + (sobel[0][2]*coins[i,j+2]) + (sobel[1][0]*coins[i+1,j]) + (sobel[1][1]*coins[i+1,j+1]) + (sobel[1][2]*coins[i+1,j+2]) + (sobel[2][0]*coins[i+2,j]) + (sobel[2][1]*coins[i+2,j+1]) + (sobel[2][2]*coins[i+2,j+2]))/300

for i in range(3,(coins.shape[0]-3)):
    for j in range(3,(coins.shape[1]-3)):
        coins_temp2[i+1,j+1] = ((sobel2[0][0]*coins[i,j]) + (sobel2[0][1]*coins[i,j+1]) + (sobel2[0][2]*coins[i,j+2]) + (sobel2[1][0]*coins[i+1,j]) + (sobel2[1][1]*coins[i+1,j+1]) + (sobel2[1][2]*coins[i+1,j+2]) + (sobel2[2][0]*coins[i+2,j]) + (sobel2[2][1]*coins[i+2,j+1]) + (sobel2[2][2]*coins[i+2,j+2]))/300


for i in range(3,(coins.shape[0]-3)):
    for j in range(3,(coins.shape[1]-3)):
        coins_temp[i,j] = coins_temp2[i,j] + coins_temp[i,j] 

cv2.imshow('After',coins_temp)
cv2.waitKey(0)