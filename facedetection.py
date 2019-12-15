# Check the directory

import os
import numpy as np
#from mtcnn import MTCNN
import cv2
from PIL import Image, ImageEnhance,ImageDraw, ImageFont

def find_faces(names, mtcnn_detector, margin = 0.3,dimensions: tuple = (256,256,3),conf_thresh:float = 0.98):
    """
    names : input image we want to perform face detection on. Shout be of the format:
            dirname + image_name

    mtcnn_detector : Allows to perform MTCNN Detection ->
                        a) Detection of faces (with the confidence probability)
                        b) Detection of keypoints (left eye, right eye, nose, mouth_left, mouth_right)

    dimension:  Allows to define the shape of the output images and contact_sheet ->
                tuple of the format (width,height,num_faces), defines the dimensions of contact sheet:
                                     width : width of one image i.e face
                                     height : height of one image i.e face
                                     num_face : number of faces in one row of contact sheet
                Overall size of the concact sheet is :
                                    overall_width  : width * num_faces
                                    overall_height : height * int(np.ceil(faces/num_faces)), where faces is the total
                                    number of faces detected by our detector.
                                    So, we get overall_width by overall_height contact sheet.
    conf_thresh: Allows to manipulate the threshold value, so we can filter out the faces with low
                 confidence levels

    margin: Allows to manipulate the margin between the boxes ,the output of the detect_faces(img), and the frame?
                1. setting it to 0 will return the picture of the face
                2. setting it to large value will give an error

    """
    width,height,num_faces = dimensions
    if type(names) == list:
        contact_sheets = []
        for img_name in names:
            # read the image and convert it from BGR to RGB
            img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)
            pil_img=Image.fromarray(img)
            #detect faces
            boxes = mtcnn_detector.detect_faces(img)
            faces = []
            conf = []
            thresh = conf_thresh

            for face in boxes:
                if face['confidence'] >=thresh:
                    faces.append(face['box'])
                    conf.append(face['confidence'])
            i = 0
            faces_in_each = []
            if not faces:
                contact_sheets.append(Image.new(pil_img.mode, (width*num_faces,height*int(np.ceil(1/num_faces)))))
                continue
            for x,y,w,h in faces:
                #Crop face that satisfy our threshold
                cropped = pil_img.crop((x-margin*w,y-margin*h,x+w+margin*w,y+h+margin*h)).resize((width,height))
                #Sho confidence level as a text
                d = ImageDraw.Draw(cropped)
                s = str('Confidence level: ' + str(conf[i]))
                d.text((30,30), s, fill=(255,255,0))
                # add all cropped faces into a list
                faces_in_each.append(cropped)
                i+=1

             contact_sheet = Image.new(pil_img.mode, (width*num_faces,height*int(np.ceil(len(faces_in_each)/num_faces))))
             #contact sheet modification to display each iteration's result
             x = 0
             y = 0
                
             for face in faces_in_each:
                 face.thumbnail((width,height))
                 contact_sheet.paste(face, (x, y))
                 if x+width == contact_sheet.width:
                     x=0
                     y=y+height
                 else:
                     x=x+width
            contact_sheets.append(contact_sheet)
        return contact_sheets
    else:
        # read the image and convert it from BGR to RGB
        img = cv2.cvtColor(cv2.imread(names), cv2.COLOR_BGR2RGB)
        pil_img=Image.fromarray(img)

        boxes = mtcnn_detector.detect_faces(img)
        faces = []
        conf = []
        thresh = conf_thresh
        for face in boxes:
            if face['confidence'] >=thresh:
                faces.append(face['box'])
                conf.append(face['confidence'])
        if not faces:
             contact_sheets.append(Image.new(pil_img.mode, (width*num_faces,height*int(np.ceil(1/num_faces)))))    
        i = 0
        faces_in_each = []
        for x,y,w,h in faces:
            cropped = pil_img.crop((x-margin*w,y-margin*h,x+w+margin*w,y+h+margin*h)).resize((width,height))
            d = ImageDraw.Draw(cropped)
            s = str('Confidence level: ' + str(conf[i]))
            d.text((30,30), s, fill=(255,255,0))
            faces_in_each.append(cropped)
            i+=1
            contact_sheet = Image.new(pil_img.mode, (width*num_faces,height*int(np.ceil(len(faces_in_each)/num_faces))))
            x = 0
            y = 0

            for face in faces_in_each:
                face.thumbnail((width,height))
                contact_sheet.paste(face, (x, y))
                if x+width == contact_sheet.width:
                    x=0
                    y=y+height
                else:
                    x=x+width
        return contact_sheet
