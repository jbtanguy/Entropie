import os
import json
import glob
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

results_path = '/home/jbtanguy/These/Corpus/Daniel/results_corporaCorpus_daniel_v2.1cleaned.json'
results = json.load(open(results_path))
entropies_dir_path = '/home/jbtanguy/These/Entropie/entropies/'
engines = ['TRAFFallbackComments', 'TRAFFallback', 'TRAFComments', 'TRAF_BL', 'TRAF', 'READ_py', 'READABILITY', 'NEWSPLEASE', 'NEWSPAPER', 'JT_trueLg', 'JT_langid', 'JT_english', 'JT', 'INSCRIPTIS', 'HTML-text', 'HTML2TEXT', 'GOO', 'BP3Largest', 'BP3KeepEverything', 'BP3Article', 'BP3']

for engine in engines:
	entropy_path = './../entropies/entropies_'+engine+'.json'
	entropies = json.load(open(entropy_path))
	
	for metric in results['global'].keys():
		Hs = []
		ms = []
		# print(results['global'].keys()): dict_keys(['clean_eval', 'voc_eval_res', 'KL_res', 'occ_eval_res'])
		# results['global'][metric][engine].keys() : ['precision', 'recall', 'f-score']['KL divergence', 'Euclidean Dist.', 'Cosine Dist.']
		cpt = 0
		for file in glob.glob('../../Corpus/Daniel/Extractions_corpus_daniel/corpora/Corpus_daniel_v2.1/reference/*'):
			# on fait avec le dossier et glob car dans results gael n'a pas mis les identifiants mais c rangé dans l'ordre de glob
			measure = 'Cosine Dist.'
			docid = file.split('/')[-1]
			if docid in entropies.keys() and measure in results['global'][metric][engine].keys():
				H = entropies[docid]
				m = results['global'][metric][engine][measure][cpt]
				Hs.append(H)
				ms.append(m)
				cpt += 1
		if Hs != [] and ms != []:
			#rho = pearsonr(Hs, ms)
			#print('{}\t{}\t{}\t{}'.format(engine, metric, rho[0], rho[1]))
			plt.scatter(ms,Hs)
			plt.xlabel(metric)
			plt.ylabel('Entropie')
			plt.title(engine + ' / ' + measure)
			plt.savefig('./../plots/'+engine+'_'+measure+'.png')
