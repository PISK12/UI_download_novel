# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutApp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_FormAboutApp (object) :
	def setupUi (self, FormAboutApp) :
		FormAboutApp.setObjectName ("FormAboutApp")
		FormAboutApp.resize (400, 87)
		self.label = QtWidgets.QLabel (FormAboutApp)
		self.label.setGeometry (QtCore.QRect (10, 30, 391, 20))
		self.label.setObjectName ("label")

		self.retranslateUi (FormAboutApp)
		QtCore.QMetaObject.connectSlotsByName (FormAboutApp)

	def retranslateUi (self, FormAboutApp) :
		_translate = QtCore.QCoreApplication.translate
		FormAboutApp.setWindowTitle (_translate ("FormAboutApp", "About App"))
		self.label.setText (_translate ("FormAboutApp", "Third-party software component: PyQt, Qt, BeautifulSoup"))


if __name__ == "__main__" :
	import sys

	app = QtWidgets.QApplication (sys.argv)
	FormAboutApp = QtWidgets.QWidget ()
	ui = Ui_FormAboutApp ()
	ui.setupUi (FormAboutApp)
	FormAboutApp.show ()
	sys.exit (app.exec_ ())
