# following this tutorial https://rare-technologies.com/word2vec-tutorial/
import os
import gensim, logging
from underthesea.word_tokenize import tokenize

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class Sentences(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        for line in open(self.filepath):
            content = line.strip()
            yield tokenize(content).split()


sentences = Sentences('data/corpus.10M.txt')  # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences, workers=16, size=300)
model.save("tmp/text10M.size300.bin")
