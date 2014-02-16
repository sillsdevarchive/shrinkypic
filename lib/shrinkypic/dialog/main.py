# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib/shrinkypic/dialog/main.ui'
#
# Created: Sun Feb 16 20:04:25 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(321, 382)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../icon/shrinkypic_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.horizontalLayout = QtGui.QHBoxLayout(MainWindow)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.PictureRotationLabel = QtGui.QLabel(MainWindow)
		self.PictureRotationLabel.setObjectName("PictureRotationLabel")
		self.gridLayout.addWidget(self.PictureRotationLabel, 4, 0, 1, 1)
		self.FileNameLabel = QtGui.QLabel(MainWindow)
		self.FileNameLabel.setObjectName("FileNameLabel")
		self.gridLayout.addWidget(self.FileNameLabel, 0, 0, 1, 1)
		self.CaptionEdit = QtGui.QLineEdit(MainWindow)
		self.CaptionEdit.setObjectName("CaptionEdit")
		self.gridLayout.addWidget(self.CaptionEdit, 11, 0, 1, 3)
		self.SizeSelect = QtGui.QComboBox(MainWindow)
		self.SizeSelect.setObjectName("SizeSelect")
		self.SizeSelect.addItem("")
		self.SizeSelect.addItem("")
		self.SizeSelect.addItem("")
		self.gridLayout.addWidget(self.SizeSelect, 3, 0, 1, 1)
		self.CaptionLabel = QtGui.QLabel(MainWindow)
		self.CaptionLabel.setObjectName("CaptionLabel")
		self.gridLayout.addWidget(self.CaptionLabel, 10, 0, 1, 1)
		self.PictureSizeLabel = QtGui.QLabel(MainWindow)
		self.PictureSizeLabel.setObjectName("PictureSizeLabel")
		self.gridLayout.addWidget(self.PictureSizeLabel, 2, 0, 1, 1)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem, 13, 0, 1, 1)
		self.FileNameEdit = QtGui.QLineEdit(MainWindow)
		self.FileNameEdit.setObjectName("FileNameEdit")
		self.gridLayout.addWidget(self.FileNameEdit, 1, 0, 1, 2)
		self.CancelButton = QtGui.QPushButton(MainWindow)
		self.CancelButton.setObjectName("CancelButton")
		self.gridLayout.addWidget(self.CancelButton, 13, 2, 1, 1)
		self.OkButton = QtGui.QPushButton(MainWindow)
		self.OkButton.setObjectName("OkButton")
		self.gridLayout.addWidget(self.OkButton, 13, 1, 1, 1)
		self.RotationDial = QtGui.QDial(MainWindow)
		self.RotationDial.setMinimum(-20)
		self.RotationDial.setMaximum(20)
		self.RotationDial.setPageStep(1)
		self.RotationDial.setObjectName("RotationDial")
		self.gridLayout.addWidget(self.RotationDial, 7, 0, 1, 1)
		self.GetPictureButton = QtGui.QPushButton(MainWindow)
		self.GetPictureButton.setObjectName("GetPictureButton")
		self.gridLayout.addWidget(self.GetPictureButton, 1, 2, 1, 1)
		self.RotationBox = QtGui.QSpinBox(MainWindow)
		self.RotationBox.setMinimum(-20)
		self.RotationBox.setMaximum(20)
		self.RotationBox.setObjectName("RotationBox")
		self.gridLayout.addWidget(self.RotationBox, 5, 0, 1, 1)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem1)
		self.OutlineCheckBox = QtGui.QCheckBox(MainWindow)
		self.OutlineCheckBox.setObjectName("OutlineCheckBox")
		self.verticalLayout.addWidget(self.OutlineCheckBox)
		self.ViewCheckBox = QtGui.QCheckBox(MainWindow)
		self.ViewCheckBox.setChecked(True)
		self.ViewCheckBox.setObjectName("ViewCheckBox")
		self.verticalLayout.addWidget(self.ViewCheckBox)
		self.gridLayout.addLayout(self.verticalLayout, 7, 2, 1, 1)
		self.horizontalLayout.addLayout(self.gridLayout)

		self.retranslateUi(MainWindow)
		QtCore.QObject.connect(self.OkButton, QtCore.SIGNAL("pressed()"), MainWindow.setupUi)
		QtCore.QObject.connect(self.GetPictureButton, QtCore.SIGNAL("clicked()"), MainWindow.setupUi)
		QtCore.QObject.connect(self.CancelButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
		QtCore.QObject.connect(self.RotationDial, QtCore.SIGNAL("sliderMoved(int)"), self.RotationBox.setValue)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ShrinkyPic - v0.1.r26", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureRotationLabel.setText(QtGui.QApplication.translate("MainWindow", "Picture Rotation", None, QtGui.QApplication.UnicodeUTF8))
		self.FileNameLabel.setText(QtGui.QApplication.translate("MainWindow", "File Name", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter a caption for this picture", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setToolTip(QtGui.QApplication.translate("MainWindow", "Choose a size to output the picture", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setItemText(0, QtGui.QApplication.translate("MainWindow", "Small", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setItemText(1, QtGui.QApplication.translate("MainWindow", "Medium", None, QtGui.QApplication.UnicodeUTF8))
		self.SizeSelect.setItemText(2, QtGui.QApplication.translate("MainWindow", "Large", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Enter a caption for this picture.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.CaptionLabel.setText(QtGui.QApplication.translate("MainWindow", "Caption", None, QtGui.QApplication.UnicodeUTF8))
		self.PictureSizeLabel.setText(QtGui.QApplication.translate("MainWindow", "Picture Size", None, QtGui.QApplication.UnicodeUTF8))
		self.FileNameEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter the original picture path and file name", None, QtGui.QApplication.UnicodeUTF8))
		self.CancelButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Click to close the program", None, QtGui.QApplication.UnicodeUTF8))
		self.CancelButton.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
		self.OkButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Click to begin process", None, QtGui.QApplication.UnicodeUTF8))
		self.OkButton.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
		self.RotationDial.setToolTip(QtGui.QApplication.translate("MainWindow", "Rotate to change picture orientation", None, QtGui.QApplication.UnicodeUTF8))
		self.GetPictureButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Browse for a picture to shrink", None, QtGui.QApplication.UnicodeUTF8))
		self.GetPictureButton.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Opens the file browser", None, QtGui.QApplication.UnicodeUTF8))
		self.GetPictureButton.setText(QtGui.QApplication.translate("MainWindow", "Get Picture", None, QtGui.QApplication.UnicodeUTF8))
		self.RotationBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Change picture orientation (-20 to 20 degrees)", None, QtGui.QApplication.UnicodeUTF8))
		self.OutlineCheckBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Add an outline to the picture", None, QtGui.QApplication.UnicodeUTF8))
		self.OutlineCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Outline", None, QtGui.QApplication.UnicodeUTF8))
		self.ViewCheckBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Check to view after processing", None, QtGui.QApplication.UnicodeUTF8))
		self.ViewCheckBox.setText(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))

