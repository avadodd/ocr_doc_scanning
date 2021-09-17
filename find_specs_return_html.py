'''
This file finds the specifications as follows and prints them out to output.txt.
It grabs this info from a clean text file (tess.txt, created from convert_to_images.py) created from tesseract reading txt from images.

specs:

PD#
Series
Title
Copy txt
'''

import os
import re
import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd

path = '/home/muthur-admin/Desktop/Syntheta-business/210816-JPG-doc-scanner/pdf2image-outputs/'

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            
            
            
for pdf in os.listdir(path): 
	# Open the file for reading
	with open(path+pdf+'/'+'output.txt','w') as fw:
		with open(path+pdf+'/'+'tess.txt','r') as fr:
			f = fr.read()
			print(f)	
			# Find strings starting with PD#
			match = re.search(r'PD\s*#\s*:*\s*(\S+)', f)
			
			# Did we find a match for the PD#?
			if match:
				# Yes, process it
				pd = match.group(1)
			else:
				pd = 'None'
				
			#find all strings starting with GS
			match2 = re.findall(r'GS(\S+)', f)
		
			#if there are 8 characters after GS, save it as the series number
			for i in range(len(match2)):
				if len(match2[i]) == 8:
					series = match2[i]
			
			#look behind series number to find Title name
			res = re.search(series,f)
			loc = res.start()		
			title1 = f[loc-38:loc-3]
			
			#clean up newlines and non-letters in title
			if title1.find("\n") != -1:
				title1 = re.sub('\n+', '\n',title1)
				trash, title1 = title1.split("\n")[:2]	
				
			if title1[-1].isalpha() == False and title1[-1] != ')' :
				title1 = title1.replace(title1[-1],'')

			
			
			#write all info out to txt file
			fw.write('PD#: {}\n'.format(pd))
			fw.write('Series: GS{}\n'.format(series))
			fw.write('Title: {}\n'.format(title1))
			fw.write('Clean copy of text: {}\n'.format(f))
	
			
		
			
	with open(path+pdf+'/'+'tess.txt','r') as fr:
		f = fr.read()		
		# we make root element
		usrconfig = ET.Element("pdf_specs")
		  
		# create sub element
		usrconfig = ET.SubElement(usrconfig, "pdf_specs")

		  
		usr = ET.SubElement(usrconfig, "PD#")
		usr.text = str(pd)
		usr = ET.SubElement(usrconfig, "Series")
		usr.text = "GS"+str(series)
		usr = ET.SubElement(usrconfig, "Title")
		usr.text = str(title1)
		usr = ET.SubElement(usrconfig, "Copy Text")
		usr.text = str(f)
		

		  
		tree = ET.ElementTree(usrconfig)
		indent(usrconfig)
		# write the tree into an XML file
		tree.write(path+pdf+'/'+"output.xml", encoding ='utf-8', xml_declaration = True)
		
		


