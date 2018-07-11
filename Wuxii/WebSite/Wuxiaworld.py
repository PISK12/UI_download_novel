import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from Wuxii.WebSiteParentsClass import BaseWebSite

from icecream import ic


class Wuxiaworld(BaseWebSite):
    MAIN_ADRES = "http://www.wuxiaworld.com"
    OPTIONS_DIR = {"Completed": "/tag/completed",
                   "Chinese": "/language/chinese", "Korean": "/language/korean", "English": "/language/english"}
    NEXTCOMMAND = "Next Chapter"

    def __init__(self, class_ToFile):
        super(Wuxiaworld, self).__init__(class_ToFile)
        self.index_adres = self.MAIN_ADRES
        self.list = list(self.OPTIONS_DIR.keys())

    def running(self):
        for adres in self._get_all_chapters(Wuxiaworld.MAIN_ADRES + self.link):
            self.add_text_to_listWidget_from_Gui(adres)
            self._download_www_to_text(Wuxiaworld.MAIN_ADRES + adres)
            if not self.work:
                break

    def _get_all_chapters(self, link):
        ic()
        soup = self.make_soup(link)
        chapters = soup.find_all("li", {"class": "chapter-item"})
        for chapter in chapters:
            yield chapter.find("a").get("href")

    def _get_all_title_and_link_from_translating(self):
        ic()
        dict_with_all_title_and_links = {}
        for link_type in Wuxiaworld.OPTIONS_DIR:
            raw_link = "{}{}".format(
                Wuxiaworld.MAIN_ADRES, Wuxiaworld.OPTIONS_DIR[link_type])
            soup = self.make_soup(raw_link)
            for parts in soup.find_all("ul", {"class": "media-list genres-list"}):
                for part in parts.find_all("a", {"class": "text-white"}):
                    if part.h4 not in dict_with_all_title_and_links:
                        dict_with_all_title_and_links[part.h4.text] = part.get(
                            "href")
        return dict_with_all_title_and_links

    # get from website all titles with links
    def all_title_and_link_from_translating(self):
        return self._get_all_title_and_link_from_translating()

    def _download_www_to_text(self, adres):
        ic()
        ic(adres)
        name = adres.split("/")[-1]
        soup = self.make_soup(adres)
        text = ""
        if soup != None:
            soup = soup.find("div", {"class": "fr-view"})
            for s in soup.find_all("p"):
                text += s.text
                text += "\r\n\r\n"
            self.toTextFile(text, name)

    def _clean_big_text(self, text):
        ic()
        text = text.lstrip().rstrip()
        text = text.split("\r\n")
        texti = ""
        for t in text:
            if len(t) > len(texti):
                texti = t
        return texti.replace("\r\n\r\n", "\r\n")
