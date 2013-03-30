#!/usr/bin/python

###############################################################################
################################# Description #################################
###############################################################################

'''
								ShrinkyPic

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

import os, sys, codecs, shutil, argparse, subprocess

# Set some global vars
systemName      = 'ShrinkyPic'
systemVersion   = '0.2.20130330124914'

# Give a welcome message
print '\n\t\tWelcome to ' + systemName
print '\n\t\tVersion ' + systemVersion + '\n'



###############################################################################
############################## General Functions ##############################
###############################################################################

def processPic (filename, size, rotate, caption = None) :
	'''Prepare the arguments for process and then process.'''

	# Build file names
	(name, ext)     = filename.split('.')
	outFile         = os.path.join(os.getcwd(), name + '-' + size + '.png')
	inFile          = os.path.join(os.getcwd(), filename)

	# Begin the output command set
	cmds = ['convert']
	# Set rotate var
	if not rotate :
		rotate = '0'
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
	cmds.append(inFile)
	# Build the rest of the command set
	base = ['-thumbnail', sizeDim, '-font', 'Andika-Basic-Regular', '-pointsize', str(fontSize), '-border', '2x2', '-density', '72', '-gravity', 'center', '-bordercolor', 'white', '-background', 'black', '-polaroid', str(rotate), outFile]
	for c in base :
		cmds.append(c)

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
		os.system('eog ' + outFile + ' &')


################################################################################
############################### Command Processing #############################
################################################################################

# The argument handler
def userArguments (args) :
	'''Process incoming command arguments.'''

	if args.filename :
		processPic(args.filename, args.size, args.rotate, args.caption)


###############################################################################
############################### Argparser Setup ###############################
###############################################################################

# Setup the arg parser
parser = argparse.ArgumentParser(description=systemName)

# Add main arguments (first postion options)
#parser.add_argument('-a', '--about', action='store_true', help = 'The shrinky_pic script resizes images for use in an eUpdate email message and Dreschers Info newsletters.  It starts with JPG of any size and ends with a 400x300 72 dpi compressed PNG image and a larger 800x600 300 dpi PNG image.')
parser.add_argument('filename', help='The file to process (a positional argument required for all actions with this process)')
parser.add_argument('-c', '--caption', help='A caption to add to the output files.')
parser.add_argument('-r', '--rotate', default=0, help='Degrees to rotate the output. Default is none.')
parser.add_argument('-s', '--size', default='small', help='Size of the output, small, medium, or large.')

# Send the collected arguments to the handler
userArguments(parser.parse_args())
