from Tools import Tools
from WriteOrReadFromFile import ToFile
from WuxiaWorld import Wuxiaworld
from Qidian import Qidian

class Back:
	webs={"Wuxiaworld":Wuxiaworld,"Qidian":Qidian}
	def __init__(self, *args):
		self.webs=Back.webs
		self.status_downloading=False
		self.class_ToFile=ToFile()
		self.offline_data=Tools.load_obj("offline_data")

	def set_source_novel(self,select_source):
		self.select_source=select_source
		self.source=self.webs[select_source](self.class_ToFile)

	def clear_offline_data(self):
		self.offline_data.clear()
		Tools.save_obj({},"offline_data")

	def start_download(self,title,link,button,listWidget):
		self.button_from_GUI(button)
		self.listWidget_from_Gui(listWidget)
		self.class_ToFile.set_title(title)
		self.source.set_title_and_link(title,link)
		self.source.start()

	def all_title_and_link_from_translating(self):
		if self.select_source in self.offline_data:
			return self.offline_data[self.select_source]
		else:
			self.offline_data[self.select_source]=self.source.all_title_and_link_from_translating()
			Tools.save_obj(self.offline_data,"offline_data")
			return self.offline_data[self.select_source]

	def change_main_catalog(self,path):
		self.class_ToFile.change_main_catalog(path)

	def button_from_GUI(self,button):
		self.source.button_from_GUI(button)

	def listWidget_from_Gui(self,listWidget):
		self.source.listWidget_from_Gui(listWidget)

	def stop(self):
		self.source.stop()




