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

import os, sys, codecs, shutil, argparse, subprocess, csv, tempfile

# Set some global vars
systemName      = 'ShrinkyPic'
systemVersion   = '0.2.r005'

# Give a welcome message
print '\n\t\tWelcome to ' + systemName
print '\n\t\tVersion ' + systemVersion + '\n'


###############################################################################
############################## General Functions ##############################
###############################################################################


def processCsvFile (csvFile) :
	'''Prepare arguments found in the CSV file for processing.'''

	csvs = csv.DictReader(open(csvFile), dialect=csv.excel)
	records = list((row.pop('filename'),row) for row in csvs)

	for f in records :
		params = f[1]
		imgFile = f[0]
		# Make sure we pass something for options
		outline = 'false'
		rotate = '0'
		size = 'small'
		subdir = ''
		if params['outline'] :
			outline = params['outline']
		if params['rotate'] :
			rotate = params['rotate']
		if params['size'] :
			size = params['size']
		if params['subdir'] :
			subdir = params['subdir']
		# Call the process for this record
		processPicFile(imgFile, rotate, size, params['caption'], outline, subdir, False)


def outlinePic (inFile) :
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
		sys.exit('ERROR: Failed to add outline to file: ' + inFile + ' (shrinky_pic.outlinPic())')


def crushPic (inFile) :
	'''Use the pngnq utility to take out the fluff from a PNG file.'''

	rc = subprocess.call(['pngnq', inFile])
	# Clean up - The only way I could seem to get pngnq to work in this
	# configuration was to let it put its special extention on the back.
	# Because of this, some cleanup has to be done.
	crushFile = inFile.replace('.png', '-nq8.png')
	shutil.copyfile(crushFile, inFile)
	os.remove(crushFile)


def processPicFile (inFile, rotate, size, caption, outline, subdir, viewer) :
	'''Prepare the arguments for an Imagemagick process and then run the process.'''

	# Workaround: cannot seem to with None args that come from argparse
	if not rotate :
		rotate = '0'
	if not size :
		size = 'small'
	if not caption :
		caption = ''
	if not outline :
		outline = 'False'
	if not subdir :
		subdir = ''

	# Build file names
	dirPath         = os.getcwd()
	(name, ext)     = os.path.splitext(inFile)
	inFile          = os.path.join(dirPath, inFile)
	if subdir :
		outFile     = os.path.join(dirPath, subdir, name + '-' + size + '_' + str(rotate) + '.png')
		if not os.path.exists(os.path.join(dirPath, subdir)) :
			os.mkdir(os.path.join(dirPath, subdir))
	else :
		outFile     = os.path.join(dirPath, name + '-' + size + '_' + str(rotate) + '.png')

	workFile        = tempfile.NamedTemporaryFile().name + '.png'
	shutil.copyfile(inFile, workFile)

	# Add an outline to a pic
	# FIXME: May need to turn this into an option at some point
	if outline.lower() == 'true' :
		workFile        = outlinePic(workFile)

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
		if size == 'small' :
			crushPic(outFile)

		print 'Created: ' + os.path.split(outFile)[1]
		# View the results (os.system allows the terminal to return right away)
		if viewer :
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
		processPicFile(args.filename, args.rotate, args.size, args.caption, args.outline, args.subdir, True)
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
parser.add_argument('-o', '--outline', choices=['True', 'true', 'False', 'false'], help='Add a thin outline around the base picture.')
parser.add_argument('-d', '--subdir', help='Create a sub folder in the current folder to output the new files.')

# Send the collected arguments to the handler
userArguments(parser.parse_args())
