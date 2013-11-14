#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from shrinky_pic_gui import Form

class ShrinkyPic (Form) :

	def __init__ (self) :
		Form.__init__ (self)
		self.pushButton.clicked.connect(self.clicked)
#        print dir(self.SizeBox)
		self.caption = self.CaptionEdit.text()

	def clicked (self) :
		print "Hellow World!"
		print self.caption

if __name__ == '__main__' :

	import sys
	app = QtGui.QApplication(sys.argv)
	window = ShrinkyPic()
	window.show()
	sys.exit(app.exec_())
