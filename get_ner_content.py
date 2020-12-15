import pandas as pd
import os
import pickle
import spacy
import nltk
import ssl

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
# print(df['year'].dtypes)
# print(df['decade'].dtypes)
nlp = spacy.load('en_core_web_sm')

ner_content = []
for i, row in df.iterrows():
    ner = nlp(row['content'])
    ner_content.append(ner)
    print('completed ', i, ' articles')

df['ner_content'] = ner_content
# save clean article dict in specific directory
file_name = 'df_ner.pickle'
df.to_pickle(file_name)
# ner_questions = [nlp(s) for s in df.content]

# save clean article dict in specific directory
file_name = 'ner_content.pickle'
with open(file_name, 'wb') as fd:
    pickle.dump(ner_content, fd)