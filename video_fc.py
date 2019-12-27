import cv2
from mtcnn import MTCNN
from PIL import Image, ImageEnhance,ImageDraw, ImageFont

video_capture = cv2.VideoCapture(0)
detector = MTCNN()

while True:
    #Capture frame-by-frame
    ret, frame = video_capture.read()
    k = cv2.waitKey(5)
    box = detector.detect_faces(frame)
    faces = []
    for face in box:
        if face['confidence'] >=0.98:
            faces.append(face['box'])
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('FaceDetection', frame)