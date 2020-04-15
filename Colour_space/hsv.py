import cv2
import numpy as np

imgpath = 'traffic_light.jpeg'

img = cv2.imread(imgpath)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold of green in HSV space 
lower_blue = np.array([36,0,0]) 
upper_blue = np.array([86,200, 200]) 

# preparing the mask to overlay 
mask = cv2.inRange(hsv, lower_blue, upper_blue) 
print(np.sum(mask))

result = cv2.bitwise_and(hsv, hsv, mask = mask) 
cv2.imwrite('test_hsv.jpg', result)
