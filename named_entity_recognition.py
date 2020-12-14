import pandas as pd
import os
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
from spacy import displacy
import ssl
from collections import Counter
import sqlite3

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('popular')


dicts = []
folders = ['equarterly_clean_articles/', 'ereview_clean_articles/', 'socbio_clean_articles/']
for folder in folders:
    filenames = os.listdir(folder)
    for file in filenames:
        infile = open(folder + file, 'rb')
        corp_dict = pickle.load(infile)
        dicts.append(corp_dict)
        infile.close()

df = pd.DataFrame(dicts)

df['title'] = df['title'].str.lower()
df['content'] = df['content'].str.lower()
df['year'] = pd.to_numeric(df['year'])


decades = []
years = []
for index, row in df.iterrows():
    year = int(row['year'])
    decade = int(str(year)[:-1] + '0')
    years.append(year)
    decades.append(decade)


del df['year']
df['year'] = years
df['decade'] = decades
print(df['year'].dtypes)
print(df['decade'].dtypes)
nlp = spacy.load('en', parse=False, tag=False, entity=True)

sentence = str(df.iloc[0].content)
sentence_nlp = nlp(sentence)

# print named entities in article
print([(word, word.ent_type_) for word in sentence_nlp if word.ent_type_])

# visualize named entities
displacy.render(sentence_nlp, style='ent', jupyter=True)

ner_questions = [nlp(s) for s in df.content]

net_question = [([w.ent_type_ for w in s]) for s in ner_questions]
net_question = [s if s else (["None"]) for s in net_question]

ners = [ne for n in net_question for ne in n[0]]

ner_cnt = Counter(ners)
print(ner_cnt.most_common(10))


print()
