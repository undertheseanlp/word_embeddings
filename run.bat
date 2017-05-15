call activate underthesea.TMV
git submodule foreach git pull origin master
python task_data_sync.py
python task_word_segmentation.py
python task_model_evaluation.py
