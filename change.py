import os
from os import walk
import xml.etree.ElementTree as ET

for root1, dirs, files in os.walk('/Users/harsh/Desktop/data'):

    for file in files:

        
        if file == 'change.py' or file =='settings.json':
            continue
        else:
        
            tree = ET.parse(file)  
            root = tree.getroot()

            for elem in root.iter('object'):
                
                 
                for elem2 in elem.iter('name'): 


                    if  elem2.text == 'Hen':
                        elem2.text = 'hen'
                    if  elem2.text == 'Feed box':
                        elem2.text = 'Feedbox'
                    if  elem2.text == 'Watertank':
                        elem2.text = 'Water tank'
            #####
            for elem3 in root.iter('path'):
                s=str(file)
                s=s.replace('xml','JPG')
                elem3.text='C:\\Image\\'+s

            for elem4 in root.iter('folder'):
                elem4.text='Image'   
               
                


            tree.write(file) 