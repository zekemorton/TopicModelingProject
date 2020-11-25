import re
import pickle
import os

# create directory for clean articles if doesn't exist yet
save_path = 'socbio_clean_articles'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# go through all text files in socbio directory
file_path = 'socbio_good_txt'
files = os.listdir(file_path)

# iterate thru all socbio articles
for f in files:
    with open(file_path + '/' + f) as file:
        data = file.read()

        # get download times in text
        download_inst = re.findall("Downloaded.*2015", data)
        list_set = set(download_inst)
        downloads = list(list_set)

        # split into metadata beginning and article portion
        metadata_part, article_part = '', ''
        if len(downloads) >= 1:
            partitioned = data.partition(downloads[0])
            metadata_part, article_part = partitioned[0], partitioned[2]
        else:
            partitioned = data
            metadata_part = data

        # extract article metadata
        metadata_part = metadata_part.replace('\n', ' ')
        meta_data_str = re.findall(r"To cite this article:.*DOI", metadata_part)[0]
        publisher = 'Social Biology'
        title = re.search(r"\d\) (.*), Social Biology", meta_data_str).group(1)
        author = re.search(r"article: (.*) \(\d+", meta_data_str)
        if author is None:
            author = 'N/A'
        else:
            author = author.group(1)
        year = re.search(r'\((.*?)\)', meta_data_str).group(1)
        vol, issue = re.search(r"Social Biology, (.*), \d", meta_data_str).group(1).split(':')
        start_page = re.search(r":.*, (.*), DOI", meta_data_str).group(1).split('-')[0]

        # remove "Downloaded by..." instances from article
        for instance in downloads:
            article_part = article_part.replace(instance, '')

        # remove random publisher name appearances
        article_part = article_part.replace('\n\nSocial Biology\n\n','\n')

        # if dash then newline -> remove newline and dash replace with nothing
        article_part = article_part.replace('-\n', '').replace('--', ' ').replace('- ', ' ')

        # if number, no space, word -> add a space
        article_part = re.sub('(\d+(\.\d+)?)', r' \1 ', article_part)

        # remove remaining all newlines and dashes
        article_part = article_part.replace('\n', ' ').replace('-', ' ').replace('  ', ' ')

        # get acknowledgments/references/bibliography
        has_ref = False
        references_part = ''
        if 'ACKNOWLEDGMENTS' in article_part:
            has_ref = True
            partitioned = article_part.partition('ACKNOWLEDGMENTS')
            article_part, references_part = partitioned[0], partitioned[2]
        elif 'REFERENCES' in article_part:
            has_ref = True
            partitioned = article_part.partition('REFERENCES')
            article_part, references_part = partitioned[0], partitioned[2]
        elif 'BIBLIOGRAPHY' in article_part:
            has_ref = True
            partitioned = article_part.partition('BIBLIOGRAPHY')
            article_part, references_part = partitioned[0], partitioned[2]

        # remove discussion portion from references
        if 'DISCUSSION' in references_part:
            references_part = references_part.partition('DISCUSSION')[0]

        # store article info in dictionary
        info_dict = {}
        info_dict['title'] = title
        info_dict['year'] = year
        info_dict['publisher'] = publisher
        info_dict['content'] = article_part
        info_dict['has_ref'] = has_ref
        info_dict['references'] = references_part
        info_dict['start_page'] = start_page

        # save clean article dict in specific directory
        file_name = 'socbio_' + year + '_' + vol + '-' + issue + '_' + start_page + '.pickle'
        with open(save_path + '/' + file_name, 'wb') as fd:
            pickle.dump(info_dict, fd)
