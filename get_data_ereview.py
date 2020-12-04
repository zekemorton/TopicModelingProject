import pandas as pd
import json
import re
import pickle
import os

# create directory for clean articles if doesn't exist yet
save_path = 'ereview_clean_articles'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# go through all text files in equarterly directory
file_path = 'ereview_good_txt'
files = os.listdir(file_path)

# # store article info in dictionary
# info_dict = {}
# info_dict['title'] = title
# info_dict['year'] = year
# info_dict['publisher'] = publisher
# info_dict['content'] = article_part
# info_dict['has_ref'] = has_ref
# info_dict['references'] = references_part
# info_dict['start_page'] = start_page

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

    for ending in url_ends:
        article_path = file_path + '/' + ending + '.txt'
        if os.path.exists(article_path):

            # get metadata
            title = row['title']
            year = row['year']
            publisher = 'ereview'

            # get article content

            # info_dict['content'] = article_part
            # info_dict['has_ref'] = has_ref
            # info_dict['references'] = references_part
            # info_dict['start_page'] = start_page





# remove title if found in article
# "Eugenics Review"

# user json to match metadata to article
# url - the number portion at end match to last nums of text title
