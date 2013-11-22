#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from shrinky_pic_gui import Form

class ShrinkyPicForm (Form) :

	def __init__ (self) :

		self.sp = ShrinkyPic()

		Form.__init__ (self)
		self.pushButton.clicked.connect(self.okClicked)

	def okClicked (self) :

# Question: How do I collect data like the following from the form?
		fileName    = 'Hello'
		caption     = 'World'
		size        = '!'
		rotation    = '0'
		self.sp.test(fileName, caption, size, rotation)


class ShrinkyPic (object) :

	def test (self, fileName, caption, size, rotation) :
		print fileName, caption, size, rotation


# Question: Why do I get this error when I click on the OK button:
#   TypeError: setupUi() takes exactly 2 arguments (1 given)


if __name__ == '__main__' :

	import sys
	app = QtGui.QApplication(sys.argv)
	window = ShrinkyPicForm()
	window.show()
	sys.exit(app.exec_())
