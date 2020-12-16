import pickle

# see contents of pickled files

FILENAME = "/clean_articles/ereview_clean_articles/ereview_><h2_2-1_00396-0033.pickle"
pickle_off = open('ner.pickle', "rb")
contents = pickle.load(pickle_off)

print(contents)