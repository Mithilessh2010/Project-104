import cv2
import numpy as np

img = cv2.imread('assets/solar-system.jpg') 

cv2.putText(img,  
           "Sun",
           (100, 80),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 4,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mercury",
           (150, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Venus",
           (225, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Earth",
           (325, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mars",
           (425, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (650, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Saturn",
           (850, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (950, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (1100, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale = 0.5,  
           color=(255,255,255)
           )
cv2.imshow('output',img)
cv2.waitKey(0)