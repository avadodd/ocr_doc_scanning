import codecs
import os
import shutil
import docx2txt

directory = "/home/muthur-admin/Desktop/ocr-extraction-data-samples/word/"

if os.path.isdir(directory+"locked_files"):
	pass
else:
	os.mkdir(directory+"locked_files")

for file in os.listdir(directory):
	if file[-4:] == "docx":
		try:	
			doc = docx2txt.process(file)
		except:
			shutil.move(directory+file, directory+"locked_files/"+file)
