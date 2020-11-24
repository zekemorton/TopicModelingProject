import re
import pickle
import os

# create directory for clean articles if doesn't exist yet
save_path = 'socbio_clean_articles'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# go through all text files in equarterly directory
file_path = 'socbio_good_pdf'
files = os.listdir(file_path)

for f in files:
    with open(file_path + '/' + f) as file:
        data = file.read()

