import sys

sys.path.append ("..")  # Adds higher directory to python modules path.
from Wuxii.WebSiteParentsClass import BaseWebSite

from icecream import ic


class Liberspark (BaseWebSite) :
	MAIN_ADRES = "http://liberspark.com"

	# get from website all titles with links
	def all_title_and_link_from_translating (self) :
		return self._get_all_title_and_link_from_translating ()

	def _get_all_title_and_link_from_translating (self) -> dict :
		ic ()
		dict_with_all_title_and_links = { }
		soup = self.make_soup (Liberspark.MAIN_ADRES)
		table = soup.find ("ul", { "class" : "dropdown-menu projects-dropdown" })
		for link in table.find_all ('a') :
			dict_with_all_title_and_links [link.text] = link.get ('href')
		return dict_with_all_title_and_links

	def _get_link_first_chapter (self, link) :
		return self.make_soup (link).find ("div", { "class" : "card-container" }).find ("a").get ("href")

	def _download_www_to_text (self, link) :
		soup = self.make_soup (link)
		text = soup.find ("div", { "id" : "chapter_body" })
		name = "-".join (link.split ("/") [-2 :])
		self.link = soup.find ("div", { "class" : "col-lg-4 col-sm-4 col-xs-4", "align" : "right" }).a.get ("href")
		if not Liberspark.MAIN_ADRES in self.link :
			self.link = Liberspark.MAIN_ADRES + self.link
		ic (self.link)
		self.toTextFile (text.text, name)

	def running (self) :
		ic ()
		self.link = self._get_link_first_chapter (self.link)
		while self.link != None :
			self.add_text_to_listWidget_from_Gui ("/".join (self.link.split ("/") [4 :]))
			self._download_www_to_text (self.link)
			if not self.work :
				break
