import spacy


class SemanticAnalyzer:
	def __init__(self):
		self.nlp = spacy.load('en_core_web_sm')

	def analyze(self, text):
		pass
