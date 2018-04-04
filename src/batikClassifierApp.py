from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os

import evaluate

class LoadDialog(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)


class Root(FloatLayout):
	loadfile = ObjectProperty(None)
	nama_batik = ObjectProperty(None)
	verdict_batik = ObjectProperty(None)
	filechooser = ObjectProperty(None)
	
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
		self._popup.open()

	def update_path(self, path):
		path = self.filechooser.path
	
	def load(self, path, filename):
		#with open(os.path.join(path, filename[0])) as stream:
		#	self.text_input.text = stream.read()
		self.nama_batik.text = filename[0]
		self.dismiss_popup()
	
	def classify(self):
		verdict = evaluate.Evaluate.run(self.nama_batik.text)
		self.verdict_batik.text = verdict

class BatikClassifier(App):
	pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
	BatikClassifier().run()