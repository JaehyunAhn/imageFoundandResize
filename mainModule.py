# -*- coding: utf-8 -*-
from imageListResize import *
"""
Filename: mainModule
Author: Sogo
Project title: Yerago image processing
Contribution date: 03/02/2015

Sogang University (c) All rights reserved
"""

# read and crop images
images = collect_images('./yeragoData')
print len(images), 'files will read.'
data_processing(images)
