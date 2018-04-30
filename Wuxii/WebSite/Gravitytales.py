from WebSiteParentsClass import BaseWebSite


class GravityTales(BaseWebSite):
    MAIN_ADRES = "http://gravitytales.com/"
    NEXTCOMMAND = "Next Chapter"

    def __init__(self, class_ToFile):
        super(GravityTales, self).__init__(class_ToFile)
        self.index_adres = self.MAIN_ADRES

    def all_title_and_link_from_translating(self):
        soup = self.make_soup(self.index_adres)
        dict_with_all_title_and_links = {}
        for raw_link in soup.find(id=Wuxiaworld.OPTIONS_DIR[table]).find_all('a')[1:]:
            text = raw_link.text
            text = self.clean_from_bad_characters(text)
            text = text.replace("()", "")
            clear_link = raw_link.get('href')
            dict_with_all_title_and_links[text] = clear_link
        return dict_with_all_title_and_links
