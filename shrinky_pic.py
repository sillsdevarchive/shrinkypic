#!/usr/bin/python

###############################################################################
################################# Description #################################
###############################################################################

''' ShrinkyPic

	Resize images and outputs a "polaroid" style image in three different sizes:

		small   400x300 (default)
		medium  800x600
		large   1024x768

	Output will be in PNG with a size indicator added to the file name. If small
	is selected for size, a special compression will be applied so the file size
	is as small as possible.

	Options are available for adding a caption and rotating too.

	The utility depends on the following command-line utilities:

		convert (ImageMagick package for picture manipulation)
		pngnq (PNG compression utility, not pngcrush)
		eog (Eye of GNOME image viewer utility)
'''

import os, sys, codecs, shutil, argparse, subprocess, csv

# Set some global vars
systemName      = 'ShrinkyPic'
systemVersion   = '0.2.20130608'

# Give a welcome message
print '\n\t\tWelcome to ' + systemName
print '\n\t\tVersion ' + systemVersion + '\n'



###############################################################################
############################## General Functions ##############################
###############################################################################


def processCsvFile (inFile) :
	'''Prepare arguments found in the CSV file for processing.'''

	path = os.path.split(inFile)[0]
	csvs = csv.DictReader(open(inFile), dialect=csv.excel)
	records = list((row.pop('filename'),row) for row in csvs)

	for f in records :
		params = f[1]
		imgFile = os.path.join(path, f[0])
		# Make sure we pass something for rotate
		rotate = '0'
		size = 'small'
		if params['rotate'] :
			rotate = params['rotate']
		if params['size'] :
			size = params['size']
		# Call the process for this record
		processPicFile(imgFile, rotate, size, params['caption'], False)


def outlinePic (inFile) :
	'''Add a simple outline to a picture. Return the name of the file
	that was just created.'''

	(name, ext)     = inFile.split('.')
	outFile         = os.path.join(os.getcwd(), name + '-outline' + '.png')
	cmd = ['convert', inFile, '-bordercolor', 'black', '-border', outFile]

	# FIXME: Still working here yet.

	return outFile


def processPicFile (inFile, rotate = None, size = 'small', caption = None, viewerOn = True, outFile = None) :
	'''Prepare the arguments for an Imagemagick process and then run the process.'''

	# Build file names, if an outFile is not given, create one
	if not size :
		size = 'small'
	inFile              = os.path.join(os.getcwd(), inFile)
	if not outFile :
		rd = ''
		outFile = ''
		if rotate :
			rd = '_' + str(rotate)
		(name, ext)     = inFile.split('.')
		outFile         = os.path.join(os.getcwd(), name + '-' + size + rd + '.png')

	# Begin the output command set
	cmds = ['convert']
	# Set the output size
	fontSize = 18
	density = 72
	thumbnail = []
	if size.lower() == 'small' :
		thumbnail = ['-thumbnail', '400x300']
		fontSize = 18
		density = 72
	elif size.lower() == 'medium' :
		thumbnail = ['-thumbnail', '800x600']
		fontSize = 24
		density = 150
	elif size.lower() == 'large' :
		thumbnail = ['-thumbnail', '1024x768']
		fontSize = 28
		density = 300
	# Now tack on the input file
	cmds = cmds + ['-bordercolor', 'black', '-border', '2', inFile]
	# Need to append the caption now if there is one
	if caption :
		cmds = cmds + ['-caption', caption, '-font', 'Andika-Basic-Regular', '-pointsize', str(fontSize)]
	if rotate :
		cmds = cmds + ['-polaroid', str(rotate)]

	# Build the rest of the command set


#    base = ['-thumbnail', sizeDim, '-font', 'Andika-Basic-Regular', '-pointsize', str(fontSize), '-border', '2x2', '-density', '72', '-gravity', 'center', '-bordercolor', 'white', '-background', 'black', '-polaroid', str(rotate), outFile]
	base = ['-density', str(density), outFile]


	for c in base :
		cmds.append(c)

	print cmds

	# Run the command
	rCode = subprocess.call(cmds)
	# Process and report the return code
	if rCode == 0 :
		if size == 'small' :
			rc = subprocess.call(['pngnq', outFile])
			# Clean up - The only way I could seem to get pngnq to work in this
			# configuration was to let it put its special extention on the back.
			# Because of this, some cleanup has to be done.
			crushFile = outFile.replace('.png', '-nq8.png')
			shutil.copyfile(crushFile, outFile)
			os.remove(crushFile)

		print 'Created: ' + os.path.split(outFile)[1]
		# View the results (os.system allows the terminal to return right away)
		if viewerOn :
			os.system('eog ' + outFile + ' &')


################################################################################
############################### Command Processing #############################
################################################################################

def isCsv (filename) :
	'''Return True if this is a CSV file.'''

	f = os.path.split(filename)[1]
	if f.rfind('.') != -1 :
		if f[f.rfind('.')+1:].lower() == 'csv' :
			return True


def isImage (filename) :
	'''Return True if this is an image file that can be processed.'''

	# Define a couple image types we can work with
	imageTypes = ['jpg', 'png', 'tiff', 'tif']

	# Look at file extention first
	f = os.path.split(filename)[1]
	if f.rfind('.') != -1 :
		if f[f.rfind('.')+1:].lower() in imageTypes :
			return True


# The argument handler
def userArguments (args) :
	'''Process incoming command arguments.'''

	if isCsv(args.filename) :
		processCsvFile(os.path.realpath(os.path.expanduser(args.filename)))
	elif isImage(args.filename) :
		processPicFile(args.filename, args.size, args.rotate, args.caption)
	else :
		sys.exit('ERROR: File name [' + args.filename + '] could not be processed.')


###############################################################################
############################### Argparser Setup ###############################
###############################################################################

# Setup the arg parser
parser = argparse.ArgumentParser(description=systemName)

# Add main arguments (first postion options)
#parser.add_argument('-a', '--about', action='store_true', help = 'The shrinky_pic script resizes images for use in an eUpdate email message and Dreschers Info newsletters.  It starts with JPG of any size and ends with a 400x300 72 dpi compressed PNG image and a larger 800x600 300 dpi PNG image.')
parser.add_argument('filename', help='The file to process (a positional argument required for all actions with this process)')
parser.add_argument('-c', '--caption', help='A caption to add to the output files.')
parser.add_argument('-r', '--rotate', help='Degrees to rotate the output. Default is none.')
parser.add_argument('-s', '--size', choices=['small', 'medium', 'large'], help='Size of the output, small, medium, or large.')

# Send the collected arguments to the handler
userArguments(parser.parse_args())
