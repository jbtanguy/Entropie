import math

def learn_language_model(text, nmin=4, nmax=4):
	language_model_abs = {}
	# 1. Compter les fréquences absolues des suites conditionnelles de caractères (ex. : avec Research, 'a' sachant 'Rese')
	total = 0 # Nb proba
	for n in range(nmin, nmax+1):
		i = 0
		while i < len(text)-n:
			previous_letters = text[i:i+n]
			current_letter = text[i+n]
			total += 1
			if previous_letters not in language_model_abs.keys():
				language_model_abs[previous_letters] = {}
			if current_letter not in language_model_abs[previous_letters].keys():
				language_model_abs[previous_letters][current_letter] = 1
			else:
				language_model_abs[previous_letters][current_letter] += 1
			i += 1
	
	# 2. Transformer ces fréquences absolues en probabilités (entre 0 et 1, donc)
	language_model_rel = {}
	for gram in language_model_abs.keys():
		language_model_rel[gram] = {}
		for letter in language_model_abs[gram].keys():
			language_model_rel[gram][letter] = language_model_abs[gram][letter] / total
	return language_model_rel

def entropy(text, LM, nmin=4, nmax=4):
	"""Entropie de Shannon : H(X) = - sum p log p
	"""
	entropy = 0
	for n in range(nmin, nmax+1):
		i = 0
		while i < len(text)-n:
			previous_letters = text[i:i+n]
			current_letter = text[i+n]
			if previous_letters in LM.keys():
				if current_letter in LM[previous_letters].keys():
					proba = LM[previous_letters][current_letter]
					entropy += proba * math.log(proba, 2)
			i += 1
	entropy = - entropy
	return entropy