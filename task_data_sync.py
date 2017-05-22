from os import mkdir
from dirsync import sync

try:
    mkdir("corpus/corpus.vinews.data")
except:
    pass
finally:
    sync("corpus/corpus.vinews/vn_news/data", "corpus/corpus.vinews.data", "sync")

try:
    mkdir("corpus/corpus.viwiki.data")
except:
    pass
finally:
    sync("corpus/corpus.viwiki/viwiki", "corpus/corpus.viwiki.data", "sync")
