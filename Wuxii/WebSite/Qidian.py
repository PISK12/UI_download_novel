import sys
sys.path.append("..")  # Adds higher directory to python modules path.
import json
from urllib.request import Request, urlopen

from Wuxii.WebSiteParentsClass import BaseWebSite


class Qidian(BaseWebSite):
    MAIN_ADRES="https://www.webnovel.com"
    # used
    def running(self):
        self.get_chapter(self.link)

    # used
    def get_chapter(self, number):
        token=self.getCookies(Qidian.MAIN_ADRES)["_csrfToken"]
        adres="https://www.webnovel.com/apiajax/chapter/GetChapterList?_csrfToken={}&bookId={}&_=1524300826628".format(token,number)
        req = Request(adres, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        webpage = json.loads(webpage)
        # chapterItems = webpage["data"]["volumeItems"][0]['chapterItems']
        bookName = webpage["data"]["bookInfo"]["bookName"]
        self.title = bookName
        bookId = webpage["data"]["bookInfo"]["bookId"]
        for x in range(len(webpage["data"]["volumeItems"])):
            for i in webpage["data"]["volumeItems"][x]['chapterItems']:
                text = self.download_www_to_text(i["id"], bookId)
                name = "%s-%s-%s" % (bookName, str(i["index"]).rjust(
                    4).replace(" ", "0"), i["name"])
                name = self._clean_to_name_file (name.replace (" ", "_"))
                self.toTextFile(text, name)
                self.add_text_to_listWidget_from_Gui(name)
                if not self.work:
                    break

    # used
    def download_www_to_text(self, chapterId, bookId):

        www = "https://www.webnovel.com/book/%s/%s" % (bookId, chapterId)

        soup = self.make_soup(www)
        text = soup.find("div", class_="cha-words")
        text = str(text.text)
        text = text.replace(chr(32) + chr(32), "")
        text = text.replace(chr(10), "\n")
        text = text.replace(chr(13), "\n")
        while "\n\n" in text:
            text = text.replace("\n\n", "\n")

        return text.replace("\n", "\r\n")

    def _get_all_title_and_link_from_translating(self, number_web=1):
        adres = "https://www.webnovel.com/apiajax/category/ajax?_csrfToken={}&orderBy=4&pageIndex=".format(
            self.getCookies(Qidian.MAIN_ADRES)["_csrfToken"])
        dict_with_all_title_and_links = {}
        id = "bookId"
        name = "bookName"

        while True:
            adres_all_title_ajax = adres + str(
                number_web)
            req = Request(adres_all_title_ajax, headers={
                'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            webpage = webpage.decode("utf-8")
            webpage = json.loads(webpage)
            items = webpage["data"]["items"]
            if not len(items):
                break
            number_web += 1
            for dic in items:
                dict_with_all_title_and_links[dic["bookName"]] = dic["bookId"]
        return dict_with_all_title_and_links

    # used
    def all_title_and_link_from_translating(self, number_web=1):
        return self._get_all_title_and_link_from_translating(number_web)
