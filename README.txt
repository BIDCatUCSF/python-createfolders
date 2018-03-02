Author:
	Kyle Marchuk, PhD
	kyle.marchuk@ucsf.edu
	Biological Imaging Development Center
	March, 3rd, 2018

Description:
	This is a simple GUI interface designed to create sequentially named folders within a 	directory. The script was originally designed to be a quality of life improvement while using 	a lattice light sheet microscope where many regions of interest were being saved into 	individual folders.

Usage:
	1) Launch the executable, or run the Python script.
	2) Copy/past the directory or use the button to launch the dialog box to choose the 		directory.
	3) Choose the range of numbers of the folders.
	4) Choose the Root Name for each folder.
	5) Press 'Create Folders' button to run.

	The UserInterface.png would create 20 folders within 'D:/Users/.../Folder' named 'ROI01', 	'ROI02', 'ROI03',...,'ROI20'.

Dependencies:
	Python 3.x
	tkinter package