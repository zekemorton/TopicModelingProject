import pandas as pd
import os
import pickle
import matplotlib.pyplot as plt

# get dataframe with article content + metadata
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
df['publisher'].replace({'ereview': 'Eugenics Review'}, inplace=True)


# pie plot for num articles of each total

publishers = df.publisher.unique()
counts = []
for pub in publishers:
    num = df[df.publisher == pub].shape[0]
    counts.append(num)

fig1, ax1 = plt.subplots()
ax1.pie(counts, labels=publishers, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Articles per Journal')
ax1.axis('equal')
plt.show()


# stacked bar plot of num articles per decade, for each article

decades = []
for index, row in df.iterrows():
    year = int(row['year'])
    decade = int(str(year)[:-1] + '0')
    decades.append(decade)

df['decade'] = decades
decade_periods = sorted(list(set(decades)))

equarterly_decades = []
ereview_decades = []
socbio_decades = []

equarterly_df = df.loc[df['publisher'] == 'Eugenics Quarterly']
ereview_df = df.loc[df['publisher'] == 'Eugenics Review']
socbio_df = df.loc[df['publisher'] == 'Social Biology']

print('equarterly num = ', equarterly_df.shape[0])
print('ereview num = ', ereview_df.shape[0])
print('socbio num = ', socbio_df.shape[0])
print('total articles = ', equarterly_df.shape[0] + ereview_df.shape[0] + socbio_df.shape[0])

for dec in decade_periods:
    equarterly_decades.append(len(equarterly_df[equarterly_df['decade'] == dec]))
    ereview_decades.append(len(ereview_df[ereview_df['decade'] == dec]))
    socbio_decades.append(len(socbio_df[socbio_df['decade'] == dec]))

plotdata = pd.DataFrame({'Eugenics Quarterly': equarterly_decades, 'Eugenics Review': ereview_decades, 'Social Biology': socbio_decades}, index=decade_periods)
plotdata.plot(kind='bar', stacked='True')
plt.title('Articles per Decade')
plt.xlabel('Decades')
plt.ylabel('Number of Articles')
plt.show()

# stacked bar plot of num articles per year, for each article

year_periods = [*range(1909, 2000, 1)]

equarterly_years = []
ereview_years = []
socbio_years = []

for yr in year_periods:
    equarterly_years.append(len(equarterly_df[equarterly_df['year'] == yr]))
    ereview_years.append(len(ereview_df[ereview_df['year'] == yr]))
    socbio_years.append(len(socbio_df[socbio_df['year'] == yr]))

plotdata = pd.DataFrame({'Eugenics Quarterly': equarterly_years, 'Eugenics Review': ereview_years, 'Social Biology': socbio_years}, index=year_periods)
plotdata.plot(kind='bar', stacked='True')
plt.title('Articles per Year')
plt.xlabel('Years')
plt.ylabel('Number of Articles')
plt.show()

