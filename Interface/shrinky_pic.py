#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import QDialog, QMessageBox, QApplication
import sys
import shrinky_pic_gui

class ShrinkyPicForm (QDialog, shrinky_pic_gui.Ui_Form) :

	def __init__ (self, parent=None) :
		'''Initialize and start up the UI'''

		super(ShrinkyPicForm, self).__init__(parent)
		self.setupUi(self)
		self.connectionActions()

	def main (self) :
		'''This function shows the main dialog'''

		self.show()

	def connectionActions (self) :
		'''Connect to form buttons.'''

		self.OkButton.clicked.connect(self.okClicked)
		self.GetPictureButton.clicked.connect(self.getPictureFile)

	def okClicked (self) :
		'''Execute the OK button.'''

		fileName    = self.FileNameEdit.text()
		caption     = self.CaptionEdit.text()
		size        = self.SizeSelect.currentText()
		rotation    = self.RotationBox.text()

		# Call the main class to do the work with the data we collected
		# FIXME: This is just a temporary call
		QMessageBox.information(self, "Data", 'File: ' + fileName + '\nCaption: ' + caption + '\nRotation: ' + rotation + '\nSize: ' + size)

	def getPictureFile (self) :
		'''Call a basic find file widget to get the file we want to process.'''

		fileName = None
		dialog = QtGui.QFileDialog(self, "Find a Picture")
		dialog.setViewMode(QtGui.QFileDialog.Detail)
		dialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
		dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
		if dialog.exec_():
			fileName = dialog.selectedFiles()[0]

		# When the file is found, change the FileNameEdit text
		self.FileNameEdit.setText(fileName)

# Script starts running from here
if __name__ == '__main__' :

	app = QApplication(sys.argv)
	window = ShrinkyPicForm()
	window.main()
	sys.exit(app.exec_())
