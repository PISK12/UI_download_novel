import os
import os.path
from datetime import date
from string import ascii_letters
from sys import exc_info
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from zipfile import ZipFile

from Wuxii.WriteOrReadFromFile import ToFile
from Wuxii.Tools import Tools

from PyQt5.QtCore import QThread
from bs4 import BeautifulSoup


class BaseWebSite(QThread):
    def __init__(self, class_ToFile):
        super(QThread, self).__init__()

        self.class_ToFile = class_ToFile
        self.toTextFile = self.class_ToFile.toTextFile
        self.title = ""
        self.link = ""
        self.work = True

    def set_title_and_link(self, title, link):
        self.title = title
        self.link = link

    def run(self):
        self.work = True
        self.swith_button_from_GUI()
        self.running()
        self.swith_button_from_GUI()
        self.add_text_to_listWidget_from_Gui("I'm done")

    def running(self):
        pass

    def getTitle(self, tite_novel):
        self.title = tite_novel
        self.title = self.clean_from_bad_characters(
            self.title).replace(" ", "_")
        if self.title[-1] == "_":
            self.title = self.title[:-1]

    def make_soup(self, url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            return BeautifulSoup(webpage, "html.parser")
        except HTTPError:
            print("it's last chapter")
        except:
            print(exc_info())
            exit()

    def clean_to_name_file(self, text):
        new = ""
        for l in text:
            if l not in ("/", "\\", "|", "'", ":", "?", ">", "<"):
                new += l
        return new

    def clean_from_bad_characters(self, text):
        new = ""
        for i in text:
            if i.isdigit() or i in ascii_letters or i == " ":
                new += i
            elif i == "\r\n":
                new += "\r\n"
            elif i in "!%&*()<>?.,:\/{}[];'" or i == '"':
                new += i
        return new

    def swith_button_from_GUI(self):
        if self.button.isEnabled():
            self.button.setEnabled(False)
        else:
            self.button.setEnabled(True)

    def add_text_to_listWidget_from_Gui(self, text):
        self.listWidget.insertItem(0, text)

    def button_from_GUI(self, button):
        self.button = button

    def listWidget_from_Gui(self, listWidget):
        self.listWidget = listWidget

    def stop(self):
        self.work = False
