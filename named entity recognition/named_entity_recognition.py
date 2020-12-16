import pickle
import pandas as pd
from collections import Counter
import collections
import numpy as np
import matplotlib.pyplot as plt

pickle_off = open('ner.pickle', "rb")
ner_dict = pickle.load(pickle_off)
df = pd.DataFrame(ner_dict).T

ner_list_of_lists = df.entities.tolist()

ner_list = []
for lister in ner_list_of_lists:
    for entity in lister:
        ner_list.append(entity)

entities, tags = zip(*ner_list)
unique_tags = list(set(tags))

# TOP BEFORE/AFTER WW2
year_list = df.year.tolist()

pre_ww2 = []
post_ww2 = []
i = 0
for lister in ner_list_of_lists:
    for entity in lister:
        if year_list[i] > 1945:
            post_ww2.append(entity)
        elif year_list[i] <= 1945:
            pre_ww2.append(entity)
    i += 1

pre_entities, tags = zip(*pre_ww2)
post_entities, tags = zip(*post_ww2)

pre_labels, pre_values = zip(*Counter(pre_entities).most_common(25))
post_labels, post_values = zip(*Counter(post_entities).most_common(25))


indexes = np.arange(len(pre_labels))
width = 0.5
plt.bar(indexes, pre_values, width)
plt.xticks(indexes + width * 0.5, pre_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 Entities Pre-WW2')
plt.ylabel('Number of Occurences')
plt.show()

indexes = np.arange(len(post_labels))
width = 0.5
plt.bar(indexes, post_values, width, color='darkorange')
plt.xticks(indexes + width * 0.5, post_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 Entities Post-WW2')
plt.ylabel('Number of Occurences')
plt.show()

# TOP PERSON BEFORE/AFTER WW2
pre_ww2 = []
post_ww2 = []
i = 0
for lister in ner_list_of_lists:
    for entity, label in lister:
        if label == 'PERSON':
            if year_list[i] > 1945:
                post_ww2.append((entity, label))
            elif year_list[i] <= 1945:
                pre_ww2.append((entity, label))
    i += 1

pre_entities, tags = zip(*pre_ww2)
post_entities, tags = zip(*post_ww2)

pre_labels, pre_values = zip(*Counter(pre_entities).most_common(25))
post_labels, post_values = zip(*Counter(post_entities).most_common(25))


indexes = np.arange(len(pre_labels))
width = 0.5
plt.bar(indexes, pre_values, width)
plt.xticks(indexes + width * 0.5, pre_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 People Pre-WW2')
plt.ylabel('Number of Occurences')
plt.show()

indexes = np.arange(len(post_labels))
width = 0.5
plt.bar(indexes, post_values, width, color='darkorange')
plt.xticks(indexes + width * 0.5, post_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 People Post-WW2')
plt.ylabel('Number of Occurences')
plt.show()

# TOP NORP BEFORE/AFTER WW2
pre_ww2 = []
post_ww2 = []
i = 0
for lister in ner_list_of_lists:
    for entity, label in lister:
        if label == 'NORP':
            if year_list[i] > 1945:
                post_ww2.append((entity, label))
            elif year_list[i] <= 1945:
                pre_ww2.append((entity, label))
    i += 1

pre_entities, tags = zip(*pre_ww2)
post_entities, tags = zip(*post_ww2)

pre_labels, pre_values = zip(*Counter(pre_entities).most_common(25))
post_labels, post_values = zip(*Counter(post_entities).most_common(25))


indexes = np.arange(len(pre_labels))
width = 0.5
plt.bar(indexes, pre_values, width)
plt.xticks(indexes + width * 0.5, pre_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 NORPs Pre-WW2')
plt.ylabel('Number of Occurences')
plt.show()

indexes = np.arange(len(post_labels))
width = 0.5
plt.bar(indexes, post_values, width, color='darkorange')
plt.xticks(indexes + width * 0.5, post_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 NORPs Post-WW2')
plt.ylabel('Number of Occurences')
plt.show()

# TOP GPE BEFORE/AFTER WW2
pre_ww2 = []
post_ww2 = []
i = 0
for lister in ner_list_of_lists:
    for entity, label in lister:
        if label == 'GPE':
            if year_list[i] > 1945:
                post_ww2.append((entity, label))
            elif year_list[i] <= 1945:
                pre_ww2.append((entity, label))
    i += 1

pre_entities, tags = zip(*pre_ww2)
post_entities, tags = zip(*post_ww2)

pre_labels, pre_values = zip(*Counter(pre_entities).most_common(25))
post_labels, post_values = zip(*Counter(post_entities).most_common(25))


indexes = np.arange(len(pre_labels))
width = 0.5
plt.bar(indexes, pre_values, width)
plt.xticks(indexes + width * 0.5, pre_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 GPEs Pre-WW2')
plt.ylabel('Number of Occurences')
plt.show()

indexes = np.arange(len(post_labels))
width = 0.5
plt.bar(indexes, post_values, width, color='darkorange')
plt.xticks(indexes + width * 0.5, post_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 GPEs Post-WW2')
plt.ylabel('Number of Occurences')
plt.show()

# TOP EVENT BEFORE/AFTER WW2
pre_ww2 = []
post_ww2 = []
i = 0
for lister in ner_list_of_lists:
    for entity, label in lister:
        if label == 'EVENT':
            if year_list[i] > 1945:
                post_ww2.append((entity, label))
            elif year_list[i] <= 1945:
                pre_ww2.append((entity, label))
    i += 1

pre_entities, tags = zip(*pre_ww2)
post_entities, tags = zip(*post_ww2)

pre_labels, pre_values = zip(*Counter(pre_entities).most_common(25))
post_labels, post_values = zip(*Counter(post_entities).most_common(25))


indexes = np.arange(len(pre_labels))
width = 0.5
plt.bar(indexes, pre_values, width)
plt.xticks(indexes + width * 0.5, pre_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 Events Pre-WW2')
plt.ylabel('Number of Occurences')
plt.show()

indexes = np.arange(len(post_labels))
width = 0.5
plt.bar(indexes, post_values, width, color='darkorange')
plt.xticks(indexes + width * 0.5, post_labels, rotation=70)
plt.tight_layout()
plt.title('Top 25 Events Post-WW2')
plt.ylabel('Number of Occurences')
plt.show()
