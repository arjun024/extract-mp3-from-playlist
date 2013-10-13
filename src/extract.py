#!/usr/bin/env python

####################################################
# Author: Arjun Sreedharan
# Email: arjun024@gmail.com
# Original Repo: github.com/arjun024/meg
# License: GPL v2
# IF YOU RELEASE ANY MODIFIED VERSION OF THIS CODE,
# YOU ARE REQUIRED TO MAKE THE MODIFIED SOURCE CODE
# AVAILABLE AS FREE AND OPEN SOURCE.
####################################################

#note: this file is optimized to be compiled as a windows executable

import os, sys
from xml.dom import minidom
import Tkinter
import tkFileDialog


def main():

	if (len(sys.argv) < 2):
		Tkinter.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		playListName = tkFileDialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
		os.chdir(os.path.dirname(playListName))
	else:
		playListName = sys.argv[1]

	print("Selected playlist is " + playListName)
	folderName = os.path.basename(playListName) + "_songs"

	xmldoc = minidom.parse(playListName)
	itemlist = xmldoc.getElementsByTagName('media')
	os.system("rd /Q /S " + folderName)
	if(os.system("mkdir " + folderName) == 0):
		for media in itemlist:
			filePath = media.attributes['src'].value
			print("Copying file " + filePath + " to the folder " + playListName + "\n")
			os.system('copy  "'+ filePath +'" '+ folderName);
		print("\nCopy Successful. Check the folder " + folderName + " for the songs ;) \n")
	else:
		print("Couldn't create directory. Pls check if the directory " + folderName + "already exists of if you have sufficient privileges")
		sys.exit(0)


if __name__ == "__main__":
	main()