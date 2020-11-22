import re
import os
import pickle

# create directory for clean articles if doesn't exist yet
save_path = 'ereview_clean_articles'
if not os.path.exists(save_path):
    os.makedirs(save_path)

file_path = 'data/ereview'
files = os.listdir(file_path)
for f in files:
    with open(file_path + '/' + f, encoding='ISO-8859-1') as file:
        data = file.read()

    data = data.replace('-\n', '').replace('--', ' ').replace('- ', ' ')

    data = re.sub('(\d+(\.\d+)?)', r' \1 ', data)

    # remove remaining all newlines and dashes
    data = data.replace('\n', ' ').replace('-', '')

    # has_ref = False
    # article = ''
    # references = ''
    # if 'REFERENCES' in data:
    #     has_ref = True
    #     partitioned = data.partition('REFERENCES')
    #     article, references = partitioned[0], partitioned[2]

    info_dict = {}
    info_dict['content'] = data

    file_name = 'ereview_' + f[8:18] + '.pickle'
    with open(save_path + '/' + file_name, 'wb') as fd:
        pickle.dump(info_dict, fd)

    