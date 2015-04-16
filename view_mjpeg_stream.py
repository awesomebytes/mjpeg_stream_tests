#! /usr/bin/env python
# From http://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera
import cv2
import urllib
import numpy as np

#CAMERA_URL = "http://localhost:8080/stream?topic=/stereo/left/image"
#CAMERA_URL = "http://ipcam-ptz/mjpg/video.mjpg"
CAMERA_URL = "http://localhost:1337/mjpeg_stream"

stream=urllib.urlopen(CAMERA_URL)
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('OpenCV imshow window mjpeg stream',i)
        if cv2.waitKey(1) ==27:
            exit(0)