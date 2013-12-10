#!/usr/bin/python

from distutils.core import setup
from glob import glob
import os


setup(name = 'shrinkypic',
		version = '0.1.r18',
		description = "Image Processing Application",
		long_description = "ShrinkyPic is a simple image processing application that provides a (very) small interface for Imagemagick.",
		maintainer = "Dennis Drescher",
		maintainer_email = "dennis_drescher@sil.org",
		package_dir = {'':'lib'},
		packages = ["shrinkypic", 'shrinkypic.dialog', 'shrinkypic.icon', 'shrinkypic.process'],
		scripts = glob("shrinkypic*"),
		license = 'LGPL',
		data_files = datafiles
	 )


