import os
import sys
import time

path = os.getcwd()
tabs = 0

print("________________________________________________________________________________________")
print( "\n" + path) 
def printDirs(path,tabs):
	dirs = os.listdir(path)
	
	tabs = tabs + 1
	for fileObj in dirs:
		# Identify the file
		if (os.path.isfile(path+"/"+fileObj)):
			print("\t"*tabs + "|_ " + fileObj)
		elif (os.path.isdir(path+ "/" + fileObj)):
			print("\t"*tabs +  "|_ " + fileObj)
			printDirs(path+"/"+fileObj,tabs)
	tabs = tabs -1
printDirs(path,tabs)
print("________________________________________________________________________________________")

# Identifying the file and folder

# --- Files
#	1) Having a only one "." in whole filename and that is not at "0" index
#	2) Having a two "." in filename, one at only "0"th index and another at any other index


'''
def printDirs(path,tabs):
  9         dirs = os.listdir(path)
 10
 11         tabs = tabs + 1
 12         for fileObj in dirs:
 13                 # Identify the file
 14                 if ( (fileObj.rfind(".") > 0 ) or (fileObj.find(".") == 0) and (fileObj.rfind(".") != 0) ):
 15                         print("\t"*tabs + "--" + fileObj)
 16                 else:
 17                         print("\t"*tabs +  "--" + fileObj)
 18                         printDirs(path+"/"+fileObj,tabs)
 19         tabs = tabs -1
 20 printDirs(path,tabs)
 '''
