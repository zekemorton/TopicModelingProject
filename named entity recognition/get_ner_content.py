import pandas as pd
import os
import pickle
import spacy
import nltk
import ssl

# download nltk popular library portions
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('popular')


# get dataframe with article content and metadata
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

# get year + decade for each article
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

# create spacy model object
nlp = spacy.load('en_core_web_sm')

# get all non-numerical entities in each article
entities = []
numerical_types = ['DATE', 'TIME', 'QUANTITY', 'CARDINAL', 'PERCENT', 'MONEY', 'ORDINAL']
for i, row in df.iterrows():
    nlp_ed = nlp(row['content'])
    article_entities = []
    for ent in nlp_ed.ents:
        entity = ent.text
        label = ent.label_
        if (label not in numerical_types) and (len(entity) > 1):
            article_entities.append((entity, label))
    entities.append(article_entities)
    print('article ', i)

# create dictionary from dataframe
df['entities'] = entities
ner_df = df[['title', 'publisher', 'year', 'decade', 'entities']]
ner_dict = ner_df.T.to_dict()

# save clean article dict in specific directory
with open('ner.pickle', 'wb') as fd:
    pickle.dump(ner_dict, fd)


