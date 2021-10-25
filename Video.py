# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:42:10 2021

@author: Marto
"""
import cv2
import numpy as np
import glob
 
img_array = []
#*png is used to select all the PNGs inside the directory.
for filename in glob.glob('Folder containing the images/*.png'):
    
    img = cv2.imread(filename)
    height, width, layers= img.shape
    size = (width,height)
    img_array.append(img)
 
    #change 4 for the times you want the 4 links to make a complete spin.
img_array= 4*img_array

#30 is the amount of fps u want
out = cv2.VideoWriter('project30.mp4',cv2.VideoWriter_fourcc(*'mp4v') , 30, size)
cv2.VideoWriter()

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
print("done")
