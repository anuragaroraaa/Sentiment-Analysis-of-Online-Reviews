import pickle
import re
import nltk
def get_words_in_tweet(tweet):
    all_words = []
    #for (words) in tweet:
      #all_words.extend(words)
    all_words=re.sub("[^\w]", " ", tweet).split()
    #print all_words
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


f = open('my_classifier.pickle1011', 'rb')
classifier = pickle.load(f)
open('classified.txt', 'w').close()
open('pre_processing.txt', 'w').close()
execfile('pre_processing.py')
File=open("twitDB46.csv")

File1=open("pre_processing.txt")
N=50

for i in range(N):
    original_line=File.next().strip()
    original_tweet=original_line
    processed_line=File1.next().strip()
    processed_tweet=processed_line
    word_features = get_word_features(get_words_in_tweet(processed_tweet))  
    classified_Tweet=classifier.classify(extract_features(processed_tweet.split()))+ " "+original_tweet
    saveFile=open('classified.txt','a')
    saveFile.write(classified_Tweet)
    saveFile.write('\n')
    
f.close();
File.close();
File1.close();
saveFile.close()
