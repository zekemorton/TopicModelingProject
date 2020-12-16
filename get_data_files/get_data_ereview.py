import pandas as pd
import json
import re
import pickle
import os

# create directory for clean articles if doesn't exist yet
save_path = '../clean_articles/ereview_clean_articles'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# go through all text files in equarterly directory
file_path = '../data/ereview_good_txt'
files = os.listdir(file_path)

# get file metadata
fd = open('data/' + 'ereview' + '.json')
data = json.load(fd)
data = data['ereview']
cols = data[0].keys()
metadata_df = pd.DataFrame(data, columns=cols)
metadata_df['publisher'] = 'ereview'

# get article endings from metadata urls
url_ends = []
for i, row in metadata_df.iterrows():
    ending = re.search(r"pdf/(.*).pdf", row['url']).group(1)
    url_ends.append(ending)

    # check if article path exists in txt folder
    article_path = file_path + '/' + ending + '.txt'
    if os.path.exists(article_path):

        # get metadata
        title = row['title']
        year = row['year']
        if year == '><h2':
            year = '1910'
        publisher = 'ereview'
        vol = row['volume']
        issue = row['issue']
        end_num = ending[8:]

        # get article content
        with open(article_path) as file:
            data = file.read()

        # remove title repeats thru out article
        data = data.replace(title.upper(), ' ')

        data = data.replace('THE EUGENICS REVIEW', ' ')

        # if dash then newline -> remove newline and dash replace with nothing
        data = data.replace('-\n', '').replace('--', ' ').replace('- ', ' ')

        # if number, no space, word -> add a space
        data = re.sub('(\d+(\.\d+)?)', r' \1 ', data)

        # remove remaining all newlines and dashes
        data = data.replace('\n', ' ').replace('-', ' ').replace('  ', ' ')

        # if has references, separate and save them
        has_ref = False
        references_part = ''
        if 'REFERENCES' in data:
            has_ref = True
            partitioned = data.partition('REFERENCES')
            article_part, references_part = partitioned[0], partitioned[2]
        else:
            article_part = data

        # store article info in dictionary
        info_dict = {}
        info_dict['title'] = title
        info_dict['year'] = year
        info_dict['publisher'] = publisher
        info_dict['content'] = article_part
        info_dict['has_ref'] = has_ref
        info_dict['references'] = references_part
        info_dict['end_num'] = end_num

        # save clean article dict in specific directory
        file_name = 'ereview_' + year + '_' + vol + '-' + issue + '_' + end_num + '.pickle'
        with open(save_path + '/' + file_name, 'wb') as fd:
            pickle.dump(info_dict, fd)
