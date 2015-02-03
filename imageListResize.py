# -*- coding: utf-8 -*-
import glob
import cv2
import numpy as np
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

# read images in the folder and separate & resize its images for face
def