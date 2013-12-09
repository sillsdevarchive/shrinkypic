# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shrinky_pic_gui.ui'
#
# Created: Mon Dec  9 16:32:36 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(322, 385)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons/shrinkypic_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Form.setWindowIcon(icon)
		self.horizontalLayout = QtGui.QHBoxLayout(Form)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.PictureRotationLabel = QtGui.QLabel(Form)
		self.PictureRotationLabel.setObjectName("PictureRotationLabel")
		self.gridLayout.addWidget(self.PictureRotationLabel, 4, 0, 1, 1)
		self.FileNameLabel = QtGui.QLabel(Form)
		self.FileNameLabel.setObjectName("FileNameLabel")
		self.gridLayout.addWidget(self.FileNameLabel, 0, 0, 1, 1)
		self.CaptionEdit = QtGui.QLineEdit(Form)
		self.CaptionEdit.setObjectName("CaptionEdit")
		self.gridLayout.addWidget(self.CaptionEdit, 11, 0, 1, 3)
		self.SizeSelect = QtGui.QComboBox(Form)
		self.SizeSelect.setObjectName("SizeSelect")
		self.SizeSelect.addItem("")
		self.SizeSelect.addItem("")
		self.SizeSelect.addItem("")
		self.gridLayout.addWidget(self.SizeSelect, 3, 0, 1, 1)
		self.CaptionLabel = QtGui.QLabel(Form)
		self.CaptionLabel.setObjectName("CaptionLabel")
		self.gridLayout.addWidget(self.CaptionLabel, 10, 0, 1, 1)
		self.PictureSizeLabel = QtGui.QLabel(Form)
		self.PictureSizeLabel.setObjectName("PictureSizeLabel")
		self.gridLayout.addWidget(self.PictureSizeLabel, 2, 0, 1, 1)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem, 13, 0, 1, 1)
		self.FileNameEdit = QtGui.QLineEdit(Form)
		self.FileNameEdit.setObjectName("FileNameEdit")
		self.gridLayout.addWidget(self.FileNameEdit, 1, 0, 1, 2)
		self.CancelButton = QtGui.QPushButton(Form)
		self.CancelButton.setObjectName("CancelButton")
		self.gridLayout.addWidget(self.CancelButton, 13, 2, 1, 1)
		self.OkButton = QtGui.QPushButton(Form)
		self.OkButton.setObjectName("OkButton")
		self.gridLayout.addWidget(self.OkButton, 13, 1, 1, 1)
		self.RotationDial = QtGui.QDial(Form)
		self.RotationDial.setMinimum(-20)
		self.RotationDial.setMaximum(20)
		self.RotationDial.setPageStep(1)
		self.RotationDial.setObjectName("RotationDial")
		self.gridLayout.addWidget(self.RotationDial, 7, 0, 1, 1)
		self.GetPictureButton = QtGui.QPushButton(Form)
		self.GetPictureButton.setObjectName("GetPictureButton")
		self.gridLayout.addWidget(self.GetPictureButton, 1, 2, 1, 1)
		self.RotationBox = QtGui.QSpinBox(Form)
		self.RotationBox.setMinimum(-20)
		self.RotationBox.setMaximum(20)
		self.RotationBox.setObjectName("RotationBox")
		self.gridLayout.addWidget(self.RotationBox, 5, 0, 1, 1)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem1)
		self.OutlineCheckBox = QtGui.QCheckBox(Form)
		self.OutlineCheckBox.setObjectName("OutlineCheckBox")
		self.verticalLayout.addWidget(self.OutlineCheckBox)
		self.ViewCheckBox = QtGui.QCheckBox(Form)
		self.ViewCheckBox.setChecked(True)
		self.ViewCheckBox.setObjectName("ViewCheckBox")
		self.verticalLayout.addWidget(self.ViewCheckBox)
		self.gridLayout.addLayout(self.verticalLayout, 7, 2, 1, 1)
		self.horizontalLayout.addLayout(self.gridLayout)

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.OkButton, QtCore.SIGNAL("pressed()"), Form.setupUi)
		QtCore.QObject.connect(self.CaptionEdit, QtCore.SIGNAL("textChanged(QString)"), Form.setupUi)
		QtCore.QObject.connect(self.GetPictureButton, QtCore.SIGNAL("clicked()"), Form.setupUi)
		QtCore.QObject.connect(self.CancelButton, QtCore.SIGNAL("clicked()"), Form.close)
		QtCore.QObject.connect(self.RotationDial, QtCore.SIGNAL("sliderMoved(int)"), self.RotationBox.setValue)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "ShrinkyPic v0.1", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureRotationLabel.setText(QtGui.QApplication.translate("Form", "Picture Rotation", None, QtGui.QApplication.UnicodeUTF8))
		self.FileNameLabel.setText(QtGui.QApplication.translate("Form", "File Name", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionEdit.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setItemText(0, QtGui.QApplication.translate("Form", "Small", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setItemText(1, QtGui.QApplication.translate("Form", "Medium", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setItemText(2, QtGui.QApplication.translate("Form", "Large", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setText(QtGui.QApplication.translate("Form", "Caption", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureSizeLabel.setText(QtGui.QApplication.translate("Form", "Picture Size", None, QtGui.QApplication.UnicodeUTF8))
		self.CancelButton.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
		self.OkButton.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))
		self.GetPictureButton.setToolTip(QtGui.QApplication.translate("Form", "Browse for a picture to shrink", None, QtGui.QApplication.UnicodeUTF8))
		self.GetPictureButton.setWhatsThis(QtGui.QApplication.translate("Form", "Opens the file browser", None, QtGui.QApplication.UnicodeUTF8))
		self.GetPictureButton.setText(QtGui.QApplication.translate("Form", "Get Picture", None, QtGui.QApplication.UnicodeUTF8))
		self.OutlineCheckBox.setText(QtGui.QApplication.translate("Form", "Outline", None, QtGui.QApplication.UnicodeUTF8))
		self.ViewCheckBox.setToolTip(QtGui.QApplication.translate("Form", "Check to view after processing", None, QtGui.QApplication.UnicodeUTF8))
		self.ViewCheckBox.setText(QtGui.QApplication.translate("Form", "View", None, QtGui.QApplication.UnicodeUTF8))

