import os
import glob
from document import DanielDocument
from utils import learn_language_model

class DanielCorpus:
	def __init__(self, path, json_lang):
		self.path_ = path
		self.part_lang_ = {}
		for f in os.listdir(path):
			if f in json_lang.keys():
				if json_lang[f] not in self.part_lang_.keys():
					self.part_lang_[json_lang[f]] = [DanielDocument(path+f)]
				else:
					self.part_lang_[json_lang[f]].append(DanielDocument(path+f))


	def get_language_model(self, lang, nmin=4, nmax=4):
		doc_blocks = [d.blocks_ for l in self.part_lang_.keys() for d in self.part_lang_[l] if l==lang]
		raw_text = ''
		for blocks in doc_blocks:
			for block in blocks:
				raw_text += block + ' '
		lm = learn_language_model(text=raw_text, nmin=nmin, nmax=nmax)
		return lm