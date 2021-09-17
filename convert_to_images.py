'''
This script:
 - reads pdf files from given path and converts them to images for each page
 - prints list of images in each directory into list.txt
 - uses list.txt to create a copy of clean text of all images into tess.txt
'''


from pdf2image import convert_from_path, convert_from_bytes
import os
import pytesseract

path = './ocr-extraction-data-samples/'

#create jpeg images of pdf pages
files = os.listdir(path)
for f in files:
	os.mkdir("./pdf2image-outputs/"+f[:-4])
	images_from_path = convert_from_path(path+f, output_folder = "./pdf2image-outputs/"+f[:-4], fmt="jpeg")
	
	
#output list of images	
path = "./pdf2image-outputs/"
files = os.listdir(path)
for f in files:	
	with open(path+f+'/'+'list.txt', 'w') as fp:
		dir_list = os.listdir("./pdf2image-outputs/"+f)
		for item in dir_list:
			if item=="list.txt":
        			continue
			fp.write(path+f+'/'+"%s\n" % item)

#convert images to text			
path = "./pdf2image-outputs/"
files = os.listdir(path)
for f in files:	
	with open(path+f+'/'+'tess.txt', 'w') as tess:
		tess.write(pytesseract.image_to_string(path+f+'/'+'list.txt'))
