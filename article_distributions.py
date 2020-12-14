import pandas as pd
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

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
df['year'] = df['year'].apply(np.int64)
df['publisher'].replace({'ereview': 'Eugenics Review'}, inplace=True)
print(df.head())

# num articles of each total
publishers = df.publisher.unique()
counts = []
for pub in publishers:
    num = df[df.publisher == pub].shape[0]
    counts.append(num)

fig1, ax1 = plt.subplots()
ax1.pie(counts, labels=publishers, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
# plt.show()

# num articles per decade, for each article

decades = []
journals = []
for index, row in df.iterrows():
    year = int(row['year'])
    decade = int(str(year)[:-1] + '0')
    decades.append(decade)
    journals.append(row['publisher'])

# pre-ww2, ww2, post-ww2
