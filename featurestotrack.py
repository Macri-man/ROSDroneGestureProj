#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture('basic_handwave.ogv')

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 30,
                       qualityLevel = 0.01,
                       minDistance = 8,
                       blockSize = 7)

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
thresh_src = cv2.cvtColor(old_frame,cv2.CV_8UC1)
old_thresh = cv2.adaptiveThreshold(old_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    thresh_src = cv2.cvtColor(frame,cv2.CV_8UC1)
    frame_thresh = cv2.adaptiveThreshold(frame_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    points = p0
   
    # draw the tracks
    for i,(new) in enumerate(points):
        x,y = new.ravel()
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    old_thresh = frame_thresh.copy()

cv2.destroyAllWindows()
cap.release()