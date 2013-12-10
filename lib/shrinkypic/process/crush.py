#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modules needed for Crush class
import os, shutil, subprocess



class Crush (object) :



	def crushPic (self, inFile) :
		'''Use the pngnq utility to take out the fluff from a PNG file.'''

		rc = subprocess.call(['pngnq', inFile])
		# Clean up - The only way I could seem to get pngnq to work in this
		# configuration was to let it put its special extention on the back.
		# Because of this, some cleanup has to be done.
		crushFile = inFile.replace('.png', '-nq8.png')
		shutil.copyfile(crushFile, inFile)
		os.remove(crushFile)



