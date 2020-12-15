import pandas as pd
import json

# journals being examined
journals = ['equarterly', 'ereview', 'socbio']

# get file metadata
metadata_df = pd.DataFrame()
for journal_name in journals:
    cur_dir = 'data/' + journal_name + '.json'
    fd = open(cur_dir)
    data = json.load(fd)

    data = data[journal_name]
    cols = data[0].keys()

    temp_df = pd.DataFrame(data, columns=cols)
    temp_df['publisher'] = journal_name
    metadata_df = pd.concat([metadata_df, temp_df])


print(metadata_df.head())