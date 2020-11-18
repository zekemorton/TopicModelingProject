import pickle

# see contents of pickled files

FILENAME = "equarterly_1961_8-2_81.pickle"
pickle_off = open(FILENAME, "rb")
contents = pickle.load(pickle_off)

print(contents)