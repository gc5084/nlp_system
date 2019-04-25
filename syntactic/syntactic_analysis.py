import spacy
from spacy import displacy

class SyntaticAnalyzer:
	def __init__(self):
		self.nlp = spacy.load('en_core_web_sm')

	def analyze(self, text):
		# Analyze the dialogue : Find named entities, phrases and concepts
		doc = self.nlp(text)
		print("Printing data for each word in text")
		tokens_data = []
		for token in doc:
			token_analyzed = {'lemma': token.lemma_, 'dep': token.dep_, 'head_text': token.head.text,
			                  'head_pos': token.head.pos_, 'children': [child for child in token.children], 'pos': token.pos_}
			tokens_data.append(token_analyzed)
		print(tokens_data)
		#displacy.serve(doc, style='dep')
		return tokens_data