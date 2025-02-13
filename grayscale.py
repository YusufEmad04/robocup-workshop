import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        break

    # convert from bgr to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # select all pixels with intensity > 150 and set them to 255
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # select all pixels with intensity < 50 and set them to 255
    #_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # find contours (first return value is the contours, second is the hierarchy (relationship between contours))
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # draw the rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # calculate the center of the rectangle
        mid_x = (x + w) // 2
        mid_y = (y + h) // 2
        print("FOUND AN OBJECT AT", mid_x, mid_y)

    print("-------------------")

    cv2.imshow("gray", gray)
    cv2.imshow("thresh", thresh)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)