# -*- coding: utf-8 -*-
import os
import sys
import time

path = os.getcwd()
tabs = 0
no_of_files = 0
no_of_folders = 0

# Creating the File And Adding the map
print( "\n" + path + "\n") 

def printDirs(path,tabs):
	dirs = os.listdir(path)

	tabs = tabs + 1
	for fileObj in dirs:
		# Identify the file
		if (os.path.isfile(path+"/"+fileObj)):
                        global no_of_files
                        no_of_files += 1
                        if (dirs[-1] == fileObj):
                            print("\t"*tabs + "└── " + fileObj)
                        else:
                            print("\t"*tabs + "├── " + fileObj)
		elif (os.path.isdir(path+ "/" + fileObj)):
                        global no_of_folders
                        no_of_folders += 1
                        if (fileObj == ".git"):
                            continue
                        if (dirs[-1] == fileObj):
                            print("\t"*tabs + "└── " + fileObj)
                        else:
                            print("\t"*tabs +  "└── " + fileObj)
                            printDirs(path+"/"+fileObj,tabs)
	tabs = tabs -1
printDirs(path,tabs)
print(f"\n ( {no_of_files} files, {no_of_folders} directories found )")
