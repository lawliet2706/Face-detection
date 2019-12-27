import cv2
from facedetection import find_faces
from mtcnn import MTCNN

detector = MTCNN(steps_threshold  = [0.5, 0.7, 0.98])

image = 'hoomens.jpg'

result = find_faces(image,detector)
for img in result:
    try:
        for face in img:
            face.show()
    except:
        continue
