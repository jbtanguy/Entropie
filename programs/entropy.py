from document import DanielDocument
from corpus import DanielCorpus
from utils import entropy
import json

doc_lang_path = '/home/jbtanguy/These/Corpus/Daniel/Extractions_corpus_daniel/corpora/Corpus_daniel_v2.1/doc_lg.json'
corpus_path = '/home/jbtanguy/These/Corpus/Daniel/Extractions_corpus_daniel/corpora/Corpus_daniel_v2.1/reference/'
nmin, nmax = (2, 4)
# 1. Parsing du json 
languages = json.load(open(doc_lang_path))
lang = set(languages.values())
# 2. Chargement du corpus
corpus_ref = DanielCorpus(corpus_path, languages)
# 3. Apprentissage des modèles de langue et sauvegarde
LMs = {}
for l in lang:
	language_model = corpus_ref.get_language_model(l, nmin=nmin, nmax=nmax)
	file = open('./../language_models/proba_condi/reference'+'_'+l+'_LM.json', 'w')
	json.dump(language_model, file, indent=4)
	LMs[l] = language_model
# 4. Calcul de l'entropie
entropies = {}
for l in lang:
	for doc in corpus_ref.part_lang_[l]:
		txt = doc.text_
		path = doc.path_
		H = entropy(txt, LMs[l], nmin, nmax)
		entropies[path] = H
		print(H)

file = open('./../entropies/entropies_reference.json', 'w')
json.dump(entropies, file, indent=4)