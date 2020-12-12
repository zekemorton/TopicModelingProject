import pickle
import pandas as pd
import os
import nltk
from nltk.tokenize import sent_tokenize
import ssl
import spacy
from spacy.lang.en import English
import random
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim import corpora
import gensim
import pyLDAvis.gensim
from collections import Counter

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

spacy.load('en')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

parser = English()
lemmatizer = WordNetLemmatizer()

random.seed(42)


# Import Data
def get_data():
    dicts = []
    folders = ['equarterly_clean_articles/', 'ereview_clean_articles/', 'socbio_clean_articles/']
    for folder in folders:
        filenames = os.listdir(folder)
        for file in filenames:
            infile = open(folder + file,'rb')
            corp_dict = pickle.load(infile)
            dicts.append(corp_dict)
            infile.close

    df = pd.DataFrame(dicts)

    df['title'] = df['title'].str.lower()
    df['content'] = df['content'].str.lower()
    df['year'] = pd.to_numeric(df['year'])

    return df


def tokenize(text):
    tok = []
    tokens = parser(text)
    for token in tokens:
        if not token.orth_.isalpha() :
            continue
        if len(token) < 3:
            continue
        else:
            tok.append(token.lower_)
    return tok

def word_tok(sentances):
    new_sents = []
    for sent in sentances:
        new_sents.append(tokenize(sent))

    return new_sents

def lem_list(sentances):
    new_sents = []
    for sent in sentances:
        new_words = []
        for word in sent:
            new_words.append(lemmatizer.lemmatize(word))

        new_sents.append(new_words)

    return new_sents

def remove_stop(tokens):
    stop_words = set(stopwords.words('english'))
    stop_words.add('eee')
    stop_words.add('cece')
    new_tokens = []
    for sentance in tokens:
        new_tokens.append([w for w in sentance if not w in stop_words])

    return new_tokens

def get_tokens(df):
    for index, row in df.iterrows():
        for token in row['token']:
            yield token

def topic_model(df, num_topics):
    text_data = list(get_tokens(df))
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = num_topics, id2word=dictionary, passes=15)
    lda_display = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary, sort_topics=False)

    return ldamodel, lda_display, dictionary

def get_best_topic(vector):
    try:
        best_prob = -1
        for tuple in vector:
            if tuple[1] > best_prob:
                best_prob = tuple[1]
                best_topic = tuple[0]

        return best_topic

    except:
        return vector[0]


def get_topics(tokens, model, dictionary):
    new_vectors = []
    corpus = [dictionary.doc2bow(text) for text in tokens]
    vectors = model[corpus]
    for vector in vectors:

        new_vectors.append(get_best_topic(vector))

    return Counter(new_vectors)


def main():
    df = get_data()
    df['token'] = df['content'].apply(sent_tokenize)
    df['token'] = df['token'].apply(word_tok)
    df['token'] = df['token'].apply(lem_list)
    df['token'] = df['token'].apply(remove_stop)

    model, display, dictionary = topic_model(df, 25)

    df['topics'] = df['token'].apply(get_topics, args=(model, dictionary))

    save_cols = ['title', 'year', 'publisher', 'topics']
    save_df = df[save_cols]


    # Save Topic Models and Visualizations and DF
    with open('topic_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('topic_model_vis.pkl', 'wb') as f:
        pickle.dump(display, f)

    with open('DataFrame.pkl', 'wb') as f:
        pickle.dump(save_df, f)

main()
