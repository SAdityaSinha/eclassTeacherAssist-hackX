# a security system must consist of these three features
#       1) Read the vision and have an idea of the enviornment
#       2) Detect the unusual movement 
#       3) Needs to alert the user

import cv2
cam = cv2.VideoCapture(0)

#gain the access to the camera
# while cam.isOpened():
#     ret,frame = cam.read()    #ret is to convert the frame data to a numerical value 
#     if cv2.waitKey(5) == ord("t"): #ord is to convert the character into the binary formate , but hoe the statement works is still unclear to me
#         break
#     cv2.imshow("MySpy",frame)

#now working with motion 
from playsound import playsound
while cam.isOpened():
    ret,f1 = cam.read()
    ret,f2 = cam.read()
    diff = cv2.absdiff(f1,f2) #to calculate the difference between the frames
    bw = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #to make rgb to black&white for better clearity and eas in understanding
    blur = cv2.GaussianBlur(bw, (5,5),0) # I felt it to be important for using contours
    _, sharp = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(sharp,None, iterations=3)
    cont, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in cont :
        if cv2.contourArea(c) < 30000: #Control the sensitivity by decreasing or increasing this value
            continue
        a,b,c,d = cv2.boundingRect(c)
        cv2.rectangle(f1, (a,b), (a+c , b+d), (0,0,255))
        playsound('music.wav')
    if cv2.waitKey(5) == ord("t"):
        break
    cv2.imshow("MySpy",f1) #to see the output
