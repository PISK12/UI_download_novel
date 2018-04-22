import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from Wuxii.WebSiteParentsClass import BaseWebSite
from Wuxii.Tools import Tools


class Wuxiaworld(BaseWebSite):
    MAIN_ADRES = "http://www.wuxiaworld.com/"
    OPTIONS_DIR = {"Completed": "menu-item-12207",
                   "Chinese": "menu-item-2165", "Korean": "menu-item-116520"}
    NEXTCOMMAND = "Next Chapter"

    def __init__(self, class_ToFile):
        super(Wuxiaworld, self).__init__(class_ToFile)
        self.index_adres = self.MAIN_ADRES
        self.list = list(self.OPTIONS_DIR.keys())

    def running(self):
        adres = self._get_first_chapter(self.title, self.link)
        while self.work and True != adres:
            soup = self._download_www_to_text(adres)
            if soup != None:
                self.add_text_to_listWidget_from_Gui(adres)
                adres = self._chack_and_get_next_adres(soup, adres)
            else:
                adres = True

    def _chack_and_get_next_adres(self, soup, old_adres):

        for link in soup.find_all('a')[:]:
            if link.text == self.NEXTCOMMAND:
                new_adres = link.get("href")
                if new_adres != old_adres:
                    return new_adres
        return True

    def _get_first_chapter(self, title, adres, number=1):
        self.getTitle(title)
        soup = self.make_soup(adres)
        for link in soup.find_all('a'):
            if "chapter-" + str(number) in str(link.get('href')):
                return link.get('href')
            elif "book-" in str(link.get('href')):
                return link.get('href')
        raise "I can't find first chapter"

    # download all titles with links
    def all_title_and_link_from_translating(self):
        soup = self.make_soup(self.index_adres)
        dict_with_all_title_and_links = {}
        for table in Wuxiaworld.OPTIONS_DIR:
            for raw_link in soup.find(id=Wuxiaworld.OPTIONS_DIR[table]).find_all('a')[1:]:
                text = raw_link.text
                text = self.clean_from_bad_characters(text)
                text = text.replace("()", "")
                clear_link = raw_link.get('href')
                dict_with_all_title_and_links[text] = clear_link
        return dict_with_all_title_and_links

    def _download_www_to_text(self, adres):
        name = adres.split("/")
        if "index" in name[-2]:
            name = name[-1]
        else:
            name = name[-2]
        soup = self.make_soup(adres)
        if soup != None:
            soup = soup.find(itemprop="articleBody")
            if soup != None:
                text = soup.text
                text = self._clean_big_text(text)
                self.toTextFile(text, name)
                return soup

    def _clean_big_text(self, text):
        text = text.replace("Previous Chapter", "").replace("Next Chapter", "")
        text = text.lstrip().rstrip()
        text = text.split("\r\n")
        texti = ""
        for t in text:
            if len(t) > len(texti):
                texti = t
        return texti.replace("\r\n\r\n", "\r\n")
