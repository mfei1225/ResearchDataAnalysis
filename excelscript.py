# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:56:32 2018

@author: Michael
"""

import openpyxl as ox
import csv
import numpy as np
import pytesseract as pt
import cv2
num_files=8 #change this value of number of files
sample="A4"# change this based on the sample
width = []

#%%
time = []
temp = []
strain = []
stress = []
modulus = []
length = []
gap = []
force = []
aforce = []
#%%extract data from raw CSV files and paste into template
for num in range(num_files):
    file_name2= "PCU_"+ sample+"_NA_" + str(num+1) + ".csv"
    save_name = "tearanalysis_" + sample + "_NA_" + str(num+1) + ".xlsx"
    with open(file_name2) as csvfile:
        counter=0
        r = csv.reader(csvfile, delimiter=',')
        #rowcount = sum(1 for rows in readCSV)
        for k in range(9): # count from 0 to 8
            next(r)     # and discard the rows
        for row in r:
            if row:
                time += [float(row[0])]
                temp += [float(row[1])]
                strain += [float(row[2])]
                stress += [float(row[3])]
                length +=[float(row[5])]
                gap += [float(row[6])]
                force += [float(row[7])]
                aforce +=[float(row[8])]
                if row[4]:
                     modulus += [float(row[4])]    
                else:
                    modulus += [0]
    f_array = np.array([np.array(time),np.array(temp),np.array(strain),np.array(stress),np.array(modulus),np.array(length),
                        np.array(gap),np.array(force),np.array(aforce)])
    f_array = np.transpose(f_array)
#%%       
    template = ox.load_workbook("tearanalysis_template.xlsx") 
    temp_sheet = template.get_sheet_by_name("Sheet1") 
    temp_sheet2 = template.get_sheet_by_name("Tear Analysis")
#%%            
    def pasteRange(startCol, startRow, endCol, endRow, sheetReceiving,copiedData):
        countRow = 0
        for i in range(startRow,endRow+1,1):
            countCol = 0
            for j in range(startCol,endCol+1,1): 
                sheetReceiving.cell(row = i, column = j).value = copiedData[countRow][countCol]
                countCol += 1
            countRow += 1

#%%
    pastingRange = pasteRange(1,10,len(f_array[0]),9+len(time),temp_sheet, f_array)
   
    template.save(save_name)
    time = []
    temp = []
    strain = []
    stress = []
    modulus = []
    length = []
    gap = []
    force = []
    aforce = []
   
    
