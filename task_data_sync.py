from os import mkdir
from os.path import join

from dirsync import sync


def sync_dir(source_dir, target_dir):
    try:
        mkdir(target_dir)
    except:
        pass
    finally:
        sync(source_dir, target_dir, "sync")


def init_folders_for_modeling():
    init_folders = ["logs", "model"]
    for folder in init_folders:
        try:
            mkdir(folder)
        except:
            pass

if __name__ == '__main__':
    source_dir = join("corpus", "corpus.vinews", "vn_news", "data")
    target_dir = join("corpus", "corpus.vinews.data")
    sync_dir(source_dir, target_dir)

    source_dir = join("corpus", "corpus.vinews", "corpus.titles", "data")
    target_dir = join("corpus", "corpus.vinews.titles.data")
    sync_dir(source_dir, target_dir)

    source_dir = join("corpus", "corpus.viwiki", "viwiki")
    target_dir = join("corpus", "corpus.viwiki.data")
    sync_dir(source_dir, target_dir)

    init_folders_for_modeling()
