# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShrinkyPic-Basic.ui'
#
# Created: Mon Nov 11 16:47:32 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(332, 276)
		self.gridLayout = QtGui.QGridLayout(Form)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.CaptionEdit = QtGui.QLineEdit(Form)
		self.CaptionEdit.setObjectName(_fromUtf8("CaptionEdit"))
		self.gridLayout.addWidget(self.CaptionEdit, 8, 0, 1, 1)
		self.FileNameLabel = QtGui.QLabel(Form)
		self.FileNameLabel.setObjectName(_fromUtf8("FileNameLabel"))
		self.gridLayout.addWidget(self.FileNameLabel, 0, 0, 1, 1)
		self.RotationBox = QtGui.QSpinBox(Form)
		self.RotationBox.setMinimum(-20)
		self.RotationBox.setMaximum(20)
		self.RotationBox.setObjectName(_fromUtf8("RotationBox"))
		self.gridLayout.addWidget(self.RotationBox, 5, 0, 1, 1)
		self.SizeBox = QtGui.QComboBox(Form)
		self.SizeBox.setObjectName(_fromUtf8("SizeBox"))
		self.SizeBox.addItem(_fromUtf8(""))
		self.SizeBox.addItem(_fromUtf8(""))
		self.SizeBox.addItem(_fromUtf8(""))
		self.gridLayout.addWidget(self.SizeBox, 3, 0, 1, 1)
		self.PictureRotationLabel = QtGui.QLabel(Form)
		self.PictureRotationLabel.setObjectName(_fromUtf8("PictureRotationLabel"))
		self.gridLayout.addWidget(self.PictureRotationLabel, 4, 0, 1, 1)
		self.RotationSlider = QtGui.QSlider(Form)
		self.RotationSlider.setMinimum(-20)
		self.RotationSlider.setMaximum(20)
		self.RotationSlider.setSingleStep(0)
		self.RotationSlider.setProperty("value", 0)
		self.RotationSlider.setSliderPosition(0)
		self.RotationSlider.setOrientation(QtCore.Qt.Horizontal)
		self.RotationSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.RotationSlider.setObjectName(_fromUtf8("RotationSlider"))
		self.gridLayout.addWidget(self.RotationSlider, 6, 0, 1, 1)
		self.FileNameEdit = QtGui.QLineEdit(Form)
		self.FileNameEdit.setObjectName(_fromUtf8("FileNameEdit"))
		self.gridLayout.addWidget(self.FileNameEdit, 1, 0, 1, 1)
		self.PictureSizeLabel = QtGui.QLabel(Form)
		self.PictureSizeLabel.setObjectName(_fromUtf8("PictureSizeLabel"))
		self.gridLayout.addWidget(self.PictureSizeLabel, 2, 0, 1, 1)
		self.CaptionLabel = QtGui.QLabel(Form)
		self.CaptionLabel.setObjectName(_fromUtf8("CaptionLabel"))
		self.gridLayout.addWidget(self.CaptionLabel, 7, 0, 1, 1)

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.RotationBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.RotationSlider.setValue)
		QtCore.QObject.connect(self.RotationSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.RotationBox.setValue)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "ShrinkyPic", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionEdit.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.FileNameLabel.setText(QtGui.QApplication.translate("Form", "File Name", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeBox.setItemText(0, QtGui.QApplication.translate("Form", "Small", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeBox.setItemText(1, QtGui.QApplication.translate("Form", "Medium", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeBox.setItemText(2, QtGui.QApplication.translate("Form", "Large", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureRotationLabel.setText(QtGui.QApplication.translate("Form", "Picture Rotation", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureSizeLabel.setText(QtGui.QApplication.translate("Form", "Picture Size", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setText(QtGui.QApplication.translate("Form", "Caption", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
