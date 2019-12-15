import cv2
from facedetection import find_faces
from mtcnn import MTCNN
from PIL import Image, ImageEnhance,ImageDraw, ImageFont

detector = MTCNN()

image = ['IMG_5940.JPG','ivan.jpg','20150816_132332.jpg']
result = find_faces(image,detector)

for img in result:
    img.show()
