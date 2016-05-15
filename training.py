import csv
import nltk
import pickle
File = open('testdata.manual.2009.06.14.csv')
Reader = csv.reader(File)
Data = list(Reader)
tweets = []
row_count = sum(1 for row in Data)
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
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

for row in range(row_count):
    string=nltk.word_tokenize(Data[row][5])
    tweets.append((string,Data[row][0]))
#print sum(1 for row in tweets)
#print tweets

word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
f = open('my_classifier.pickle10', 'wb')
pickle.dump(classifier, f)
f.close()
File.close();
#tweet = 'william dafoe'
#print classifier.classify(extract_features(tweet.split()))



