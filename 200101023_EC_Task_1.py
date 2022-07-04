import cv2
import numpy as np
img = cv2.imread('Sample4.png') 
imgGrey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh= cv2.threshold(imgGrey,127,255,0)
contours, Hieracy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx],-1,(0,255,0),3)
    x= approx.ravel()[0]
    y= approx.ravel()[1]-5
    if len(approx)==3:
        cv2.putText(img, "triangle",(x,y), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    elif len(approx)==4:
        a,b,w,h= cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img,"square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
        else:
            cv2.putText(img,"parallelogram",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    elif len(approx)==5:
        cv2.putText(img,"pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    else:
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
cv2.imshow("Sample4",img)

cv2.waitKey(0)
cv2.destroyAllWindows()




