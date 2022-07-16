# Imorting All the required Modules Necessary 
# You may include math and time for displaying fps with ouput source
#############################################################################################################
import cv2
import numpy as np
import mediapipe as mp
import time

#############################################################################################################



# The main code is for you to make the class handDetector with all the required functions for getting the 
# info from the detected hand
#############################################################################################################





class handDetector():
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
# Firstly the initialize constuctor is already defined if need be you can make any changes to this constructor
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        
#############################################################################################################
# findHands function takes the image source from the calling block and if the input draw = True then draw the
# hands with all the landmarks using mediapip Hands solution (Read the doc for details)
# Also add the results to the class variable results which would then be used for further calculations
    def findHands(self, img, draw=True):
        #Firstly remember to convert the given image in RBG to RGB
        # call hands.process and pass the converted image to it and store in self.results
        self.results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        
        # For Debugging you can print(results.multi_hand_landmarks)
        # Write the code for drawing the landmarks
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)


        # Finally return the image
        return img
# findPosition function takes the image source, hand we are currently working in the image source
# and if to draw or not from the calling block and if the input draw = True then draw the
# hand positions with all the landmarks using mediapip Hands solution (Read the doc for details)
# also make the x-coordinate, y-coordinate and the the rectangle containing the hand and aslo the landmark list
# Also add the results to the class variable results which would then be used for further calculations
    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        #Write the code here 
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y *h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (54,42,41),2, cv2.FILLED)
                xList.append([cx])
                yList.append([cy])
            
            bbox = [(min(xList), min(yList)), (max(xList), min(yList)), (max(xList), max(yList)), (min(xList), max(yList))]
        # Remember: mp gives you landmarks which are normalized to 0.0 and 1.0 which need to be converted into 
        # exact coordinates for use
        print(len(self.lmList))

        # Draw if the draw given is true

        return self.lmList, bbox
# fingersUp function return list of 5 fingers and their respective state
# 0- down and 1- Up
# Make sure to go through the mediapipe docs to get to know landmark 
# number of each finger and a method to know if the finger is up or not 
    def fingersUp(self):
        if len(self.lmList)!=0:
            fingers = []
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

# findDistance function returns the image after drawing distance between 2 points 
# and drawing thar distance and highlighting the points with r radius circle and 
# t thickness line and also return length there
# this function would help us make our click to execute

    def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        

        # write your code here
        length = ((((x2-x1)**2) + ((y2-y1)**2))**0.5)
        img = cv2.putText(img, str(length), (cx,cy),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)

        return length, img, [x1, y1, x2, y2, cx, cy]
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################





# Now for the main function is to check and debug the class
# You may change it any way you want
# I have added the FPS counter and take the video feed from the PC
# If you donot have a webcam in yout PC you can use DROID CAM Software
# To debug you can also use image of a hand , the code for this I have commented out
# you can decomment it out and comment the video feed code to debug if you feel 

#############################################################################################################

def main():
    pTime = 0
    cTime = 0
    # Add the video source here
    # 0-For your first webcam in the PC
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        print(detector.findDistance(0,6, img))
        #if len(lmList) != 0:
            #print(lmList[0][3])
        print(detector.fingersUp())
            
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 1)

        cv2.imshow("Image", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
        #img = handDetector.findHands(img)
        #lmList = handDetector.findPosition(img)
        # #if len(lmList) != 0:
        # #    print(lmList[3])
            

if __name__ == "__main__":
    main()
