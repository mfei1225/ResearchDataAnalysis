# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:32:45 2018

@author: Michael
"""

num_files=9 #change this value of number of files
sample="A4"# change this based on the sample
for num in range(num_files):
    file_name= "PCU_"+ sample+"_NA_" + str(num+1) + ".csv"
    print(file_name)