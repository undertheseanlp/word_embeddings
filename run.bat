call activate underthesea.TMV
set PYTHONIOENCODING=utf-8
git submodule foreach git pull origin master
python task_data_sync.py
python task_word_segmentation.py
python task_word2vec.py
python task_model_evaluation.py
