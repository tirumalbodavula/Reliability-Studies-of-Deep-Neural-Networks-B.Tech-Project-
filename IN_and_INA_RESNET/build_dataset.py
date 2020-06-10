# import the necessary packages
from configuration import config
from imutils import paths
import shutil
import os


d=[config.TRAIN, config.TEST, config.VAL]
p = config.ORIG_INPUT_DATASET
imagePaths = list(paths.list_images(p))
with os.scandir(p) as entries:
	for entry in entries:
		if entry.is_dir():
			#print(entry.name)
			new_path = p+"\\"+entry.name
			#print(new_path)
			with os.scandir(new_path) as images:
				temp=0
				for f in images:
					final_path = new_path+"\\"+f.name
					print(final_path)
					filename = f.name
					label = entry.name
					# construct the path to the output directory
					dirPath = os.path.sep.join([config.BASE_PATH, d[temp%3], label])
					if not os.path.exists(dirPath):
						os.makedirs(dirPath)
					# construct the path to the output image file and copy it
					pi = os.path.sep.join([dirPath, filename])
					shutil.copy2(final_path, pi)
					temp+=1

