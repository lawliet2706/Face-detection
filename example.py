import cv2
from facedetection import find_faces
from mtcnn import MTCNN

detector = MTCNN()

image = 'ivan.jpg'
result = find_faces(image,detector, margin = 0.2,dimensions: tuple = (256,256,3),conf_thresh:float = 0.98)

display(result)
