import pickle

# see contents of pickled files

FILENAME = "socbio_clean_articles/socbio_1978_25-3_Social Biology, 25:3, 258.pickle"
pickle_off = open(FILENAME, "rb")
contents = pickle.load(pickle_off)

print(contents)