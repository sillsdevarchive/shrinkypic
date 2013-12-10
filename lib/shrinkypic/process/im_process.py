#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modules needed for ShrinkyPic class
import sys, os, shutil, subprocess, tempfile
from shrinkypic.process             import crush


class ImProcess (object) :

	def __init__ (self, parent=None) :
		self.crush = crush.Crush()

	###############################################################################
	############################## General Functions ##############################
	###############################################################################

	def outlinePic (self, inFile) :
		'''Add a simple outline to a picture. Return the name of the file
		that was just created.'''

		(name, ext)     = os.path.splitext(inFile)
		outFile         = name + '-border.png'
		cmd = ['convert', inFile, '-bordercolor', 'black', '-border', '1x1', outFile]

		# Run the command
		rCode = subprocess.call(cmd)
		# Process and report the return code
		if rCode == 0 :
			return outFile
		else :




#FIXME: Add an error dialog box for this
			sys.exit('ERROR: Failed to add outline to file: ' + inFile + ' (shrinky_pic.outlinPic())')





	def processPicFile (self, inFile, outFile, rotate, size, caption, outline=False, viewer=False) :
		'''Prepare the arguments for an Imagemagick process and then run the process.'''

		# Make tempfile
		workFile        = tempfile.NamedTemporaryFile().name + '.png'
		shutil.copyfile(inFile, workFile)

		# Add an outline to a pic
# FIXME: May need to turn this into an option at some point
		if outline :
			workFile        = self.outlinePic(workFile)

		# Begin the output command set
		cmds = ['convert']
		# Set the output size
		sizeDim = '400x300'
		fontSize = 18
		if size :
			if size.lower() == 'small' :
				sizeDim = '400x300'
				fontSize = 18
			elif size.lower() == 'medium' :
				sizeDim = '800x600'
				fontSize = 24
			elif size.lower() == 'large' :
				sizeDim = '1024x768'
				fontSize = 28
		# Need to append the caption now if there is one
		if caption :
			cmds.append('-caption')
			cmds.append(caption)
		# Now tack on the input file
		cmds.append(workFile)
		# Build the rest of the command set
		base = ['-thumbnail', sizeDim, '-font', 'Andika-Basic-Regular', \
			'-pointsize', str(fontSize), '-border', '2x2', '-density', '72', \
				'-gravity', 'center', '-bordercolor', 'white', '-background', 'black', \
					'-polaroid', str(rotate), outFile]
		for c in base :
			cmds.append(c)

		# Run the command
		rCode = subprocess.call(cmds)
		# Process and report the return code
		if rCode == 0 :
			if size.lower() == 'small' :
				self.crush.crushPic(outFile)

			# View the results (os.system allows the terminal to return right away)
			if viewer :
				os.system('eog ' + outFile + ' &')


	################################################################################
	################################# Util Functions ###############################
	################################################################################


	def isImage (self, filename) :
		'''Return True if this is an image file that can be processed.'''

		# Define a couple image types we can work with
		imageTypes = ['jpg', 'png', 'tiff', 'tif']

		# Look at file extention first
		f = os.path.split(filename)[1]
		if f.rfind('.') != -1 :
			if f[f.rfind('.')+1:].lower() in imageTypes :
				return True
