import pickle

# see contents of pickled files

FILENAME = "/Users/kk/PycharmProjects/TopicModelingProject/ereview_clean_articles/ereview_><h2_2-1_00396-0033.pickle"
pickle_off = open(FILENAME, "rb")
contents = pickle.load(pickle_off)

print(contents)