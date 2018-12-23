# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:51:25 2018

@author: Michael
"""
from PIL import Image
import pytesseract as pt
import cv2
import numpy as np
num_files=8 #change this value of number of files
sample="A4"
width = []
for num in range(num_files):
    file_name= sample+"_NA_" + str(num+1) + ".jpg"
    #save_name = "tearanalysis_" + sample + "_NA_" + str(num+1) + ".jpg"
    raw = cv2.imread(file_name)
    h, w = raw.shape[:2]# initially cropping image 
    img= raw[100:h,0:w]
    #cv2.imshow("img",img)
    
    rimg = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #resizing
    #cv2.imshow("resized",rimg)

    kernel = np.ones((15,15),np.uint8)
    e = cv2.erode(rimg,kernel,iterations = 2)#eroding
    #cv2.imshow("erode",e)

    gray = cv2.cvtColor(e, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray",gray)
    ret, th = cv2.threshold(gray,5, 255, cv2.THRESH_BINARY_INV)
    #cv2.imshow("th",th)
    
    im2, cnt, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(cnt[0][0][0][0],cnt[0][0][0][1])#prints coordinates
    #print(cnt[0][2][0][0],cnt[0][1][0][1])
    crop= img[cnt[0][0][0][1]*2:cnt[0][1][0][1]*2,cnt[0][0][0][0]*2:cnt[0][2][0][0]*2]
    
    #cv2.imshow("Crop im",crop)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    #im = Image.open(crop)
    text = pt.image_to_string(crop, lang = "eng")# uses tessercact to find width from cropped img
    #print(text)
    width += [round(float("".join(text[11:-2])),1)/1000]
    
    print(width)
