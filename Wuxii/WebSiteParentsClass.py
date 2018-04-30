from string import ascii_letters
from sys import exc_info
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import requests
from PyQt5.QtCore import QThread
from bs4 import BeautifulSoup
from icecream import ic


class BaseWebSite(QThread):
    MAIN_ADRES = ""

    def __init__(self, class_ToFile):
        ic.enable()
        # ic.disable()
        super(QThread, self).__init__()
        self.cacheCookies = {}
        self.class_ToFile = class_ToFile
        self.toTextFile = self.class_ToFile.toTextFile
        self.title = ""
        self.link = ""
        self.work = True

    def set_title_and_link(self, title, link):
        ic()
        self.title = title
        self.link = link

    def run(self):
        ic()
        self.work = True
        self.swith_button_from_GUI()
        self.running()
        self.swith_button_from_GUI()
        self.add_text_to_listWidget_from_Gui("I'm done")

    def running(self):
        pass

    def getTitle(self, tite_novel):
        ic()
        self.title = tite_novel
        self.title = self._clean_from_bad_characters(
            self.title).replace(" ", "_")
        if self.title[-1] == "_":
            self.title = self.title[:-1]

    def make_soup(self, url):
        ic()
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            return BeautifulSoup(webpage, "html.parser")
        except HTTPError as error:
            ic()
            ic(error)
            ic(url)
        except:
            ic()
            ic(exc_info())
            ic(url)
            exit()

    def _clean_to_name_file (self, text):
        new = ""
        for l in text:
            if l not in ("/", "\\", "|", "'", ":", "?", ">", "<"):
                new += l
        return new

    def _clean_from_bad_characters (self, text):
        ic()
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
        ic()
        if self.button.isEnabled():
            self.button.setEnabled(False)
        else:
            self.button.setEnabled(True)

    def add_text_to_listWidget_from_Gui(self, text):
        try:
            ic()
            self.listWidget.insertItem(0, text)
        except AttributeError as e:
            ic()
        except Exception as e:
            ic()
            ic(e)

    def button_from_GUI(self, button):
        try:
            ic()
            self.button = button
        except AttributeError as e:
            ic()
        except Exception as e:
            ic()
            ic(e)

    def listWidget_from_Gui(self, listWidget):
        ic()
        self.listWidget = listWidget

    def stop(self):
        ic()
        self.work = False

    def getCookies(self, adres="") -> dict:
        ic()
        if adres in self.cacheCookies:
            pass
        else:
            session = requests.Session()
            response = session.get(adres)
            self.cacheCookies[adres] = session.cookies.get_dict()
        return self.cacheCookies[adres]
