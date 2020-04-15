import cv2
import numpy as np

imgpath = 'traffic_light.jpeg'
img = cv2.imread(imgpath)

# Threshold of blue in HSV space 
lower_blue = np.array([0, 220, 0]) 
upper_blue = np.array([50, 255, 50]) 

# preparing the mask to overlay 
mask = cv2.inRange(img, lower_blue, upper_blue) 
print(np.sum(mask))
# The black region in the mask has the value of 0, 
# so when multiplied with original image removes all non-blue regions 
result = cv2.bitwise_and(img, img, mask = mask) 
cv2.imwrite('test_rgb.jpg', result)
