# Hand-gesture
## About The Project
The main idea is to make the class handDetector with all the required functions for getting the info from the detected hand. Model detects hand by either video input feed or image input and returns image with landmarks drawn on it. Users can find Distance between selected landmarks on their detected hand.
Model can alse detect how many fingers are open and how many are closed. User can also find co-ordinates of Landmarks on their detected hand.

### Environment Setup
* Install Python 3.9.0 

### Tech Stack Used
* OpenCV
* Numpy
* Mediapipe
* time, math (You may include math and time for displaying fps with ouput source.)

### Key Features
* User can find distance between selected landmarks on detected hand.
* Model can recognize how many fingers are open.
* User can find landmarks on their detected hand and also their coordinates.
* User can give Live video input feed through the webCam. If you donot have a webcam in yout PC you can use DROID CAM Software
* User can also give an image as input.

### Detecting Hand
* To get better idea of Landmarks on the Hand, Refer this documentation provided by [mediapipe](https://google.github.io/mediapipe/solutions/hands.html).
![hand_recognized](https://user-images.githubusercontent.com/83687581/179356667-f560cb6a-12ae-480f-98c9-fb71c39020a0.png)

### Detecting Closed Finger
* See the list returned in Visual Studio Code output section (Highlighted), 1 represents that finger is open, 0 represents finger is closed.
![finger2_closed](https://user-images.githubusercontent.com/83687581/179356812-b117cb31-7ac4-4da2-9b4d-f8eb1675756b.png)

### Finding Distance and Positions of Landmarks
* See the highlighted parts
![Screenshot (81)](https://user-images.githubusercontent.com/83687581/179357090-6fd6f4f2-c294-419e-899f-771b827c2847.png)
