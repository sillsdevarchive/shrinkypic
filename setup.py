#!/usr/bin/python
# -*- coding: utf-8 -*-

#    Copyright 2014, Dennis Drescher
#    All rights reserved.
#
#    This library is free software; you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 2.1 of License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should also have received a copy of the GNU Lesser General Public
#    License along with this library in the file named "LICENSE".
#    If not, write to the Free Software Foundation, 51 Franklin Street,
#    suite 500, Boston, MA 02110-1335, USA or visit their web page on the
#    internet at http://www.fsf.org/licenses/lgpl.html.

# Import modules
from distutils.core import setup
from glob import glob


setup(name = 'shrinkypic',
		version = '0.1.r25',
		description = "Image Processing Application",
		long_description = "ShrinkyPic is a simple image processing application that provides a (very) small interface for Imagemagick.",
		maintainer = "Dennis Drescher",
		maintainer_email = "dennis_drescher@sil.org",
		package_dir = {'':'lib'},
		packages = ["shrinkypic", 'shrinkypic.dialog', 'shrinkypic.icon', 'shrinkypic.process'],
		scripts = glob("shrinkypic*"),
		license = 'LGPL',
	 )


