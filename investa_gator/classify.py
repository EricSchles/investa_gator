from textblob.classifiers import NaiveBayesClassifier as NBC

train = pickle.load( open("train.p","rb") )

cl = NBC(train)
