import os
import os.path
from datetime import date
from zipfile import ZipFile

from icecream import ic


class ToFile(object):
    FORMAT_FILE = ["txt", "pdf"]

    def __init__(self):
        ic.enable()
        ic.disable()


        self.format = ToFile.FORMAT_FILE[0]
        self.chack_catalog = False
        self.toZip = False
        self.files = []
        self.main_catalog = os.getcwd()

    def change_main_catalog(self, path):
        ic()
        self.main_catalog = path

    def toTextFile(self, text, name):
        ic()
        if self.format == "txt":
            file = self.toFileTxt(text, name)
        elif self.format == "pdf":
            file = self.toFilePdf(text, name)
        else:
            print(self.format)
            self.toZip = False
            print("why you life, I have never see you")
            exit()

        if self.toZip:
            self.files.append(name + "." + self.format)

    def last_work(self):
        ic()
        if self.toZip:
            self.resultToZip()

    def set_title(self, title):
        ic()
        self.title = title

    def toFileTxt(self, text, name):
        ic()
        self.title = self.title.strip()
        if not os.path.isdir(os.path.join(self.main_catalog, self.title)):
            os.makedirs(os.path.join(self.main_catalog, self.title))
        # errors="namereplace" it error is with chinese character
        file = open(os.path.join(self.main_catalog, self.title,
                                 name + ".txt"), mode="w", errors="namereplace")
        file.write(text)
        file.close()

    def toFilePdf(self, text, name):
        ic()
        if not self.chack_catalog:
            self.title = self.title.strip()
            if not os.path.isdir(self.title):
                os.makedirs(self.title)
            self.chack_catalog = True

    def toOneFilePdf(self):
        pass

    def toOneFileEpub(self):
        pass

    def resultToZip(self):
        ic()
        nameFile = "%s_%s.zip" % (self.title, date.today())
        print(nameFile)
        with ZipFile("%s_%s.zip" % (self.title, date.today()), "w") as zipfile:
            for file in self.files:
                zipfile.write(os.path.join(self.title, file))
