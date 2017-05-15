from underscore import _
from underthesea.word_sent.tokenize import tokenize
from underthesea import word_sent
import io
from os.path import join
from os import listdir
from underthesea.corpus import PlainTextCorpus

corpus = PlainTextCorpus()
corpus.load("data")

def convert_to_text(sentences):
    content = [u"\n".join(s) for s in sentences]
    content = u"\n\n".join(content)
    return content

existed_documents = listdir("corpus.pending")
for document in corpus.documents:
    document_id = document.id
    if document_id not in existed_documents:
        print("Process %s" % document_id)
        sentences = document.sentences
        sentences = _.flatten(sentences)
        sentences = [tokenize(s).split(" . ") for s in sentences]
        sentences = _.flatten(sentences)
        segmented_sentences = [word_sent(s) for s in sentences]
        content = convert_to_text(segmented_sentences)
        filepath = join("corpus.pending", document.id)
        io.open(filepath, "w", encoding="utf8").write(content)
    else:
        print("Ignore %s" % document_id)