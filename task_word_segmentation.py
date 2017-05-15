from underscore import _
from underthesea.word_sent.tokenize import tokenize
from underthesea import word_sent
import io
from os.path import join
from os import listdir
from underthesea.corpus import PlainTextCorpus


def convert_to_text(sentences):
    content = [u"\n".join(s) for s in sentences]
    content = u"\n\n".join(content)
    return content


def segment_words(corpus_dir, target_dir):
    corpus = PlainTextCorpus()
    corpus.load(corpus_dir)
    existed_documents = listdir(target_dir)
    n_ignore = 0
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
            filepath = join(target_dir, document.id)
            io.open(filepath, "w", encoding="utf8").write(content)
        else:
            n_ignore += 1
    print("Ignore %s documents" % n_ignore)


if __name__ == '__main__':
    segment_words(corpus_dir="data", target_dir="corpus.pending")
    segment_words(corpus_dir="corpus/corpus.viwiki.data", target_dir="corpus/corpus.viwiki.segmented")
