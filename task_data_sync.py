from os import mkdir
from os.path import join

from dirsync import sync

try:
    source_dir = join("corpus", "corpus.vinews", "vn_news", "data")
    target_dir = join("corpus", "corpus.vinews.data")
    mkdir(target_dir)
except:
    pass
finally:
    sync(source_dir, target_dir, "sync")

try:
    source_dir = join("corpus", "corpus.viwiki", "viwiki")
    target_dir = join("corpus", "corpus.viwiki.data")
    mkdir(target_dir)
except:
    pass
finally:
    sync(source_dir, target_dir, "sync")
