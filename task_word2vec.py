# -*- coding: utf-8 -*-
from datetime import datetime
import gensim, logging
from os import listdir
import io
from underscore import _
from os.path import join
from tabulate import tabulate


def load_documents(folder):
    documents = listdir(folder)
    documents = [join(folder, document) for document in documents]
    return documents


def get_sentence(document):
    content = open(document, "r").read().decode("utf-8").lower()
    sentences = content.split("\n\n")
    sentences = [s.split("\n") for s in sentences]
    return sentences


def log(s):
    print s
    s = unicode(s) + u"\n"
    f.write(s)


if __name__ == '__main__':
    documents = load_documents("corpus.pending")
    documents.extend(load_documents("corpus\\corpus.viwiki.segmented"))

    sentences = [get_sentence(document) for document in documents]
    sentences = [s for sublist in sentences for s in sublist]

    # train word2vec on the two sentences
    params = {"size": 300, "min_count": 2}
    model = gensim.models.Word2Vec(sentences, size=params["size"], min_count=params["min_count"])
    vocab = list(model.wv.vocab.keys())

    log_file = "logs\\%s.txt" % datetime.now().strftime('%Y-%m-%d_%H-%M')
    f = io.open(log_file, "w", encoding="utf-8")

    log(u"Params: " + unicode(params))
    log(u"Vocab Size: %d\n" % len(vocab))

    words = [u"Hà Nội", u"đặc biệt", u"quyết tâm", u"khó khăn", u"cha", u"gái", u"Microsoft", u"Apple", u"Samsung"]
    model_file = "model\\word2vec-%s.model" % datetime.now().strftime('%Y-%m-%d_%H')
    model.save(model_file)

    for word in words:
        word = word.lower()
        if word in vocab:
            log(u"Most similar with: %s" % word)
            log(tabulate(model.most_similar(word)))
        else:
            log(u"word '%s' not in vocabulary" % word)
        log(u"\n")
