from os.path import abspath
from sys import exit, argv

from PyQt5 import QtCore, QtGui, QtWidgets

from Wuxii.Preferences import Ui_Form as Ui_PreferencesWidget
from Wuxii.back import Back


class PreferencesWidget(Ui_PreferencesWidget):
    def __init__(self):
        self.back = Back()

        app = QtWidgets.QApplication(argv)
        Window = QtWidgets.QMainWindow()

        self.setupUi(Window)
        Window.show()

        # exit(app.exec_())
