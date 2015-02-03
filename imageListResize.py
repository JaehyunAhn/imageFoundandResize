# -*- coding: utf-8 -*-
import glob
import cv2
import numpy as np
# loading classifiers
faceCascade = cv2.CascadeClassifier('./haarClassifier/haarcascade_frontalface_alt.xml')
"""
Filename: imageListResize
Author: Sogo
Project title: Yerago image processing
Contribution date: 03/02/2015

Sogang University (c) All rights reserved
"""

# collect images <.jpg>file, in dir_path, and attach label if user wants
def collect_images(dir_path):
    images = glob.glob(dir_path + '/*.jpg')
    # return list of <.jpg> file list
    return images

# using haar_classifier, find faces / return its coordinates
def face_detection(image, neighbors):
    item = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=neighbors,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    return item

# read images in the folder and separate & resize its images for face
def data_processing(image_list):
    print '[Notice] Image loaded and will be separatle'
    # load images
    for image_name in image_list:
        print 'Processing in %s', image_name
        dir_path = './'
        dir_path += (image_name.split('/')[1] + '/')
        file_name = image_name.split('/')[2][:-4]

        # read image
        image = cv2.imread(image_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detection(gray, 5)
        if len(faces) <= 0:
            print "[ERROR] there's no face in %s." % file_name
        else:
            cropFace = image
            # face extraction
            for (x, y, w, h) in faces:
                # draw a line into face (h * 2 is additional face line including neck)
                x -= (w/2)
                y -= (h/2)
                if x < 0:
                    origX = (x + w/2)
                    w += (origX*2)
                    x = 0
                else:
                    w *= 2
                if y < 0:
                    origY = (y + h/2)
                    h += (origY*2)
                    y = 0
                else:
                    h *= 2
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cropFace = image[y:y+h, x:x+w]
                cropRatio = 300.0/w
                cropH = int(h * cropRatio)
                cropSize = (300, cropH)
                print 'cropRatio is %f' % cropRatio
                # crop and save
                cropFace = cv2.resize(cropFace, cropSize)
                cv2.imwrite(dir_path + file_name + '_cvtd.jpg', cropFace)