import pickle
import re
import nltk
from itertools import islice,izip

def get_words_in_tweet(tweet):
    pairs = []
    #for (words) in tweet:
     # all_words.extend(words)
    
    #all_words=re.sub("[^\w]", " ", tweet).split()
    tokens=nltk.word_tokenize(tweet)
    #pairs = [ " ".join(pair) for pair in nltk.bigrams(tokens)]
    
    pairs=nltk.bigrams(tokens)
    #print pairs
    return pairs

def get_word_features(wordlist):
   # print wordlist

    wordlist = nltk.FreqDist(wordlist)
   # print wordlist
    word_features = wordlist.keys()
   # print word_features
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s %s)' % (word)] = (word in document_words)
   # print features
    return features


f = open('bigram_classifier.pickle', 'rb')
classifier = pickle.load(f)
open('classified.txt', 'w').close()
open('hello.txt', 'w').close()
execfile('pre_processing.py')
File=open("twitDB46.csv")

File1=open("pre_processing.txt")
N=50

for i in range(N):
    original_line=File.next().strip()
    original_tweet=original_line
    processed_line=File1.next().strip()
    processed_tweet=processed_line
   # print "ello"
    word_features = get_word_features(get_words_in_tweet(processed_tweet))  
    #print word_features
    classified_Tweet=classifier.classify(extract_features(processed_tweet.split()))+ " "+original_tweet
    saveFile=open('classified.txt','a')
    saveFile.write(classified_Tweet)
    saveFile.write('\n')
    
f.close();
File.close();
File1.close();
saveFile.close()
