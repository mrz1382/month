import cv2
import mediapipe as mp 

cap = cv2.VideoCapture(0)

while true:
    success , img = cap.read()
    
    cv2.imshow("Image" ,img)
    cv2.waitKey(1)