import cv2
import cv2
 
# The function cv2.imread() is used to read an image.
img_grayscale = cv2.imread('Lena.png',1)
 
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('color',img_grayscale)
 
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)