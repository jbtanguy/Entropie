import io
import re

class DanielDocument:
	"""La classe DanielDocument modélise les documents du corpus Daniel, les versions "parsées" des HTML. 
	"""
	def __init__(self, path, encoding='utf-8'):
		self.path_ = path
		self.text_ = ''
		try:
			file = io.open(self.path_, mode='r', encoding=encoding)
			text = file.read()
			file.close()
			self.text_ = text
		except IOError as e:
			print(e)
		blocks = []
		# Dans ces documents, on a une suite de "<p> text text text text </p>"
		for block_found in re.findall('<.+?>.+?</.+?>', self.text_):
			bloc = re.sub('<[^<]+?>', '', block_found)
			blocks.append(bloc)
		self.blocks_ = blocks
		