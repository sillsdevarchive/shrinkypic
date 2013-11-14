# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shrinky_pic_gui.ui'
#
# Created: Thu Nov 14 21:13:08 2013
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
		Form.resize(267, 344)
		self.formLayout = QtGui.QFormLayout(Form)
		self.formLayout.setObjectName(_fromUtf8("formLayout"))
		self.FileNameLabel = QtGui.QLabel(Form)
		self.FileNameLabel.setObjectName(_fromUtf8("FileNameLabel"))
		self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.FileNameLabel)
		self.PictureSizeLabel = QtGui.QLabel(Form)
		self.PictureSizeLabel.setObjectName(_fromUtf8("PictureSizeLabel"))
		self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.PictureSizeLabel)
		self.SizeBox = QtGui.QComboBox(Form)
		self.SizeBox.setObjectName(_fromUtf8("SizeBox"))
		self.SizeBox.addItem(_fromUtf8(""))
		self.SizeBox.addItem(_fromUtf8(""))
		self.SizeBox.addItem(_fromUtf8(""))
		self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.SizeBox)
		self.PictureRotationLabel = QtGui.QLabel(Form)
		self.PictureRotationLabel.setObjectName(_fromUtf8("PictureRotationLabel"))
		self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.PictureRotationLabel)
		self.CaptionLabel = QtGui.QLabel(Form)
		self.CaptionLabel.setObjectName(_fromUtf8("CaptionLabel"))
		self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.CaptionLabel)
		self.CaptionEdit = QtGui.QLineEdit(Form)
		self.CaptionEdit.setObjectName(_fromUtf8("CaptionEdit"))
		self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.CaptionEdit)
		self.FileNameEdit = QtGui.QLineEdit(Form)
		self.FileNameEdit.setObjectName(_fromUtf8("FileNameEdit"))
		self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.FileNameEdit)
		self.RotationBox = QtGui.QSpinBox(Form)
		self.RotationBox.setMinimum(-20)
		self.RotationBox.setMaximum(20)
		self.RotationBox.setObjectName(_fromUtf8("RotationBox"))
		self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.RotationBox)
		self.RotationSlider = QtGui.QSlider(Form)
		self.RotationSlider.setMinimum(-20)
		self.RotationSlider.setMaximum(20)
		self.RotationSlider.setSingleStep(0)
		self.RotationSlider.setProperty("value", 0)
		self.RotationSlider.setSliderPosition(0)
		self.RotationSlider.setOrientation(QtCore.Qt.Vertical)
		self.RotationSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.RotationSlider.setObjectName(_fromUtf8("RotationSlider"))
		self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.RotationSlider)
		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.formLayout.setWidget(10, QtGui.QFormLayout.SpanningRole, self.pushButton)

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.RotationBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.RotationSlider.setValue)
		QtCore.QObject.connect(self.RotationSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.RotationBox.setValue)
		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.setupUi)
		QtCore.QObject.connect(self.CaptionEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Form.setupUi)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "ShrinkyPic", None, QtGui.QApplication.UnicodeUTF8))
		self.FileNameLabel.setText(QtGui.QApplication.translate("Form", "File Name", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureSizeLabel.setText(QtGui.QApplication.translate("Form", "Picture Size", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeBox.setItemText(0, QtGui.QApplication.translate("Form", "Small", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeBox.setItemText(1, QtGui.QApplication.translate("Form", "Medium", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeBox.setItemText(2, QtGui.QApplication.translate("Form", "Large", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureRotationLabel.setText(QtGui.QApplication.translate("Form", "Picture Rotation", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setText(QtGui.QApplication.translate("Form", "Caption", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionEdit.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))


class Form(QtGui.QWidget, Ui_Form):
	def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QWidget.__init__(self, parent, f)

		self.setupUi(self)
