# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 327)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabMAIN = QtWidgets.QWidget()
        self.tabMAIN.setObjectName("tabMAIN")
        self.radioButtonPDF = QtWidgets.QRadioButton(self.tabMAIN)
        self.radioButtonPDF.setEnabled(True)
        self.radioButtonPDF.setGeometry(QtCore.QRect(10, 10, 109, 26))
        self.radioButtonPDF.setObjectName("radioButtonPDF")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonPDF)
        self.radioButtonTXT = QtWidgets.QRadioButton(self.tabMAIN)
        self.radioButtonTXT.setGeometry(QtCore.QRect(10, 50, 109, 26))
        self.radioButtonTXT.setChecked(True)
        self.radioButtonTXT.setObjectName("radioButtonTXT")
        self.buttonGroup.addButton(self.radioButtonTXT)
        self.checkBox = QtWidgets.QCheckBox(self.tabMAIN)
        self.checkBox.setGeometry(QtCore.QRect(140, 10, 94, 26))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.tabMAIN)
        self.pushButton.setGeometry(QtCore.QRect(410, 160, 171, 36))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tabMAIN, "")
        self.tabPDF = QtWidgets.QWidget()
        self.tabPDF.setObjectName("tabPDF")
        self.tabWidget.addTab(self.tabPDF, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.radioButtonPDF.setText(_translate("Form", "PDF"))
        self.radioButtonTXT.setText(_translate("Form", "TXT"))
        self.checkBox.setText(_translate("Form", "ZIP"))
        self.pushButton.setText(_translate("Form", "SELECT CATALOG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMAIN), _translate("Form", "MAIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPDF), _translate("Form", "PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

