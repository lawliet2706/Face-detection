import cv2
from facedetection import find_faces
from mtcnn import MTCNN

detector = MTCNN()

image = 'hoomens.jpg'

result = find_faces(image,detector)
for img in result:
    img.show()
