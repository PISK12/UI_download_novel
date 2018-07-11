from os.path import abspath
from sys import exit, argv

from PyQt5 import QtWidgets
from icecream import ic

from Wuxii.config import Ui_Form as Ui_FormConfig
from Wuxii.aboutApp import Ui_FormAboutApp
from Wuxii.aboutMe import Ui_FormAboutMe
from Wuxii.main_window import Ui_Window as Ui_MainWindow

from Wuxii.back import Back


class MainWindow(Ui_MainWindow):
    def __init__(self):
        self.last_current_Text_in_ComboBox_comboBoxTop = ""
        self.last_current_Text_in_ComboBox_comboBoxbottom = ""

        self.back = Back()
        self.app = QtWidgets.QApplication(argv)
        self.Window = QtWidgets.QMainWindow()
        self.widget = QtWidgets.QWidget()

    def play(self):
        self.setupUi(self.Window)
        self.action_widgets()
        self.action_menu_widgets()
        self.Window.show()
        exit(self.app.exec_())

    def save_setting_from_Ui_FormConfig(self):
        pass

    def show_Ui_FormConfig(self):
        ic()
        if self.startDownloadButton.isEnabled():
            self.widget_ui = Ui_FormConfig()
            self.widget_ui.setupUi(self.widget)
            self.widget.show()

            self.widget_ui.pushButton.clicked.connect(self.get_Directory)

    def show_Ui_FormAboutMe(self):
        ic()
        ui = Ui_FormAboutMe()
        ui.setupUi(self.widget)
        self.widget.show()

    def show_Ui_FormAboutApp(self):
        ic()
        ui = Ui_FormAboutApp()
        ui.setupUi(self.widget)
        self.widget.show()

    def stop(self):
        if not self.startDownloadButton.isEnabled():
            self.back.stop()
        else:
            self.addText("I can't")

    def reload(self):
        self.back.clear_offline_data()
        self.addText("The database was cleared")

    def get_Directory(self):
        if self.startDownloadButton.isEnabled():
            self.back.change_main_catalog(
                abspath(str(QtWidgets.QFileDialog.getExistingDirectory())))
        else:
            self.addText("I can't")

    def action_widgets(self):
        self.startDownloadButton.clicked.connect(self.click)
        self.comboBoxTop.addItem("")
        self.comboBoxTop.addItems([name for name in self.back.webs])
        self.comboBoxTop.currentTextChanged.connect(
            self.change_current_Text_in_ComboBox_List_Website)

    def action_menu_widgets(self):
        self.actionSelect_Catalog.triggered.connect(self.get_Directory)
        self.actionStop.triggered.connect(self.stop)
        self.actionReload_2.triggered.connect(self.reload)
        self.actionAbout_App.triggered.connect(self.show_Ui_FormAboutApp)
        self.actionAbout_me.triggered.connect(self.show_Ui_FormAboutMe)
        self.actionSettings.triggered.connect(self.show_Ui_FormConfig)

    def change_current_Text_in_ComboBox_List_Website(self):
        if self.last_current_Text_in_ComboBox_comboBoxTop != self.comboBoxTop.currentText():
            if self.comboBoxTop.currentText() != "":
                self.back.set_source_novel(self.comboBoxTop.currentText())
                self.comboBoxbottom.clear()
                self.comboBoxbottom.addItem("")
                self.comboBoxbottom.addItems(
                    [titles for titles in sorted(self.back.all_title_and_link_from_translating().keys())])
                self.last_current_Text_in_ComboBox_comboBoxTop = self.comboBoxTop.currentText()
                self.last_current_Text_in_ComboBox_comboBoxbottom = self.comboBoxbottom.currentText()

    def click(self):
        all_title_and_link_from_translating = self.back.all_title_and_link_from_translating()
        if all_title_and_link_from_translating != None:
            if self.comboBoxbottom.currentText() in self.back.all_title_and_link_from_translating():
                self.back.start_download(
                    self.comboBoxbottom.currentText(), self.back.all_title_and_link_from_translating()[
                        self.comboBoxbottom.currentText()], self.startDownloadButton, self.listWidget
                )

    def addText(self, text):
        self.listWidget.insertItem(0, text)
