
"""
import gensim.downloader as api

#
model = api.load('glove-wiki-gigaword-50')
model = api.load('glove-twitter-25')


import os
native_path = os.path.expanduser("~/Desktop/glove_50_fast.wordvectors")
model.save(native_path)
fast_model_path = os.path.expanduser("~/Desktop/glove_50_fast.wordvectors")
model = KeyedVectors.load(fast_model_path, mmap='r')
model.similarity('university', 'professor')
"""

"""
fasttext-wiki-news-subwords-300 (~958 MB / 300 dimensions):
    Traditional Word2Vec completely crashes if you pass
    a word it hasn’t seen before (an "Out of Vocabulary" error).
    FastText solves this by breaking words down into smaller
    character chunks (subwords). It allows students to test
    completely made-up words or typos (like "happpy") and
    still get a valid vector similarity score.
    Code to load:
    model = api.load('fasttext-wiki-news-subwords-300')

conceptnet-numberbatch-17-06-300 (~1.2 GB / 300 dimensions):
It combines standard text training with structured knowledge
graphs (semantic data from WordNet and Wiktionary). It excels
at relational logic, making it a fantastic educational tool
for mapping true semantic common sense rather than raw text
statistics.
model = api.load('conceptnet-numberbatch-17-06-300')

word2vec-google-news-300 ~1.6 GB
News ArticlesThe classic standard;
best for heavy vector math (King - Man + Woman).

model = api.load('word2vec-google-news-300')
"""