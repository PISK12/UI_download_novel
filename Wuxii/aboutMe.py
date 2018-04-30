# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutMe.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_FormAboutMe (object) :
	def setupUi (self, FormAboutMe) :
		FormAboutMe.setObjectName ("FormAboutMe")
		FormAboutMe.resize (397, 61)
		FormAboutMe.setLocale (QtCore.QLocale (QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.label_2 = QtWidgets.QLabel (FormAboutMe)
		self.label_2.setGeometry (QtCore.QRect (50, 10, 261, 20))
		self.label_2.setObjectName ("label_2")

		self.retranslateUi (FormAboutMe)
		QtCore.QMetaObject.connectSlotsByName (FormAboutMe)

	def retranslateUi (self, FormAboutMe) :
		_translate = QtCore.QCoreApplication.translate
		FormAboutMe.setWindowTitle (_translate ("FormAboutMe", "About Me"))
		self.label_2.setText (_translate ("FormAboutMe", " Autor https://github.com/PISK12"))


if __name__ == "__main__" :
	import sys

	app = QtWidgets.QApplication (sys.argv)
	FormAboutMe = QtWidgets.QWidget ()
	ui = Ui_FormAboutMe ()
	ui.setupUi (FormAboutMe)
	FormAboutMe.show ()
	sys.exit (app.exec_ ())
