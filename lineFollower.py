
import cv2 as cv
import numpy as np

kp, kd, ki = 1.0, 1.0, 1.0

def pid():
    global kp, kd, ki
    pass

def main():
    capture = cv.VideoCapture(0)
    
    if not capture.isOpened():
        print("error")
        exit()

    while True:
        isTrue,frame = capture.read()

        resize_ = cv.resize(frame,(500, 500),interpolation = cv.INTER_LINEAR)

        center_x = 1920 // 2
        center_y = 1080 // 2

        grayscale = cv.cvtColor(resize_,cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(grayscale,0,255,cv.THRESH_OTSU)
        
        # blank_image = np.zeros((500, 500, 3), dtype=np.uint8)
        # blank_image[thresh == 255] = [255, 255, 255]
        
        # rect_width = 150
        # rect_height = 250
        # top_left = (center_x - rect_width // 2, center_y - rect_height // 2)
        # bottom_right = (center_x + rect_width // 2, center_y + rect_height // 2)

        # # Draw rectangle on the blank image
        # cv.rectangle(blank_image, top_left, bottom_right, (0, 255, 0), 2)

        # # Draw text on the blank image
        # cv.line(blank_image,(1920//2,0),(1920//2,1080),(0,255,0),2)
        # cv.putText(blank_image, f"kp = {kp} kd = {kd} ki = {ki}", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv.LINE_AA)

        # cv.imshow("feed", blank_image)
        cv.imshow("feed", thresh)

        if cv.waitKey(20) & 0xFF ==ord("q"):
            break
    capture.release()
    cv.destroyAllWindows()

if __name__=="__main__": 
    main()