import re

with open('data/equarterly/19485565%2E1954%2E9987158.txt', encoding='ISO-8859-1') as file:
    data = file.read() #.replace('\n', ' ')

# get unique download times
download_inst = re.findall("Downloaded.*2015",data)
list_set = set(download_inst)
downloads = list(list_set)

# split into metadata beginning and article portion
partitioned = data.partition(downloads[0])
metadata_part = partitioned[0]
article_part = (partitioned[2]).replace('\n', ' ')

# remove "Downloaded by..." from article
for instance in downloads:
    article_part = article_part.replace(instance,'')