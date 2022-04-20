import os
import sys
import time

path = os.getcwd()
tabs = 0

# Creatign the File And Adding the map
mapFile = open("mapFile.txt","w")
mapFile.close()

mapFile = open("mapFile.txt","a")

print("________________________________________________________________________________________\n")
mapFile.write("________________________________________________________________________________________\n")

print( "\n" + path + "\n") 
mapFile.write("\n" + path + "\n")

def printDirs(path,tabs):
	dirs = os.listdir(path)
	
	tabs = tabs + 1
	for fileObj in dirs:
		# Identify the file
		if (os.path.isfile(path+"/"+fileObj)):
			print("\t"*tabs + "|_ " + fileObj)
			mapFile.write("\t"*tabs + "|_ " + fileObj+"\n")
		elif (os.path.isdir(path+ "/" + fileObj)):
			print("\t"*tabs +  "|_ " + fileObj)
			mapFile.write("\t"*tabs + "|_ " + fileObj+"\n")
			printDirs(path+"/"+fileObj,tabs)
	tabs = tabs -1
printDirs(path,tabs)
print("\n________________________________________________________________________________________")
mapFile.write("\n________________________________________________________________________________________")
mapFile.close()

# Identifying the file and folder

# --- Files
#	1) Having a only one "." in whole filename and that is not at "0" index
#	2) Having a two "." in filename, one at only "0"th index and another at any other index

