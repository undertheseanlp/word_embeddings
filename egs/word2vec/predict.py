import gensim
from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('tmp/word2vec.10M.bin')
print(model)