import cv2 as cv
import numpy as np


# capture = cv.VideoCapture(0)


capture = cv.VideoCapture("C:/Users/acer/OneDrive/Desktop/laneDetection/lane detection data/4608279-uhd_3840_2160_24fps.mp4")
# capture = cv.VideoCapture("/home/ashutosh/Documents/laneDetection/lane detection data/4695859-uhd_3840_2160_30fps.mp4")
# "C:\Users\acer\OneDrive\Documents\laneDetection\lane detection data\4695859-uhd_3840_2160_30fps.mp4"

if not capture.isOpened():
    print("error")
    exit()

# capture.set(cv.CAP_PROP_FRAME_WIDTH,640)
# capture.set(cv.CAP_PROP_FRAME_HEIGHT,650)
# capture.set(cv.CAP_PROP_FPS,30)

while True:
    isTrue,frame = capture.read()
    resize_ = cv.resize(frame,(600,400),interpolation = cv.INTER_LINEAR)
    grayScale = cv.cvtColor(resize_, cv.COLOR_BGR2GRAY)
    GaussianBlur = cv.GaussianBlur(grayScale, (5,5), 0)
    edge = cv.Canny(GaussianBlur,75,150)

    # ret, thresh = cv.threshold(grayscale,0,255,cv.THRESH_OTSU)
    lines = cv.HoughLinesP(edge, 1, np.pi/180, 30,maxLineGap=250)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            print(x1,y1,x2,y2)
            cv.line(resize_, (x1,y1), (x2,y2),(255,255,255), 3)
    cv.imshow("feed", edge)
    cv.imshow("lol", resize_)

    if cv.waitKey(20) & 0xFF ==ord("q"):
        break
capture.release()
cv.destroyAllWindows()
