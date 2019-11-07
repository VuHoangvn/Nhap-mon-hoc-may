from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from ReadData import *

class IFIDF_LinearSVM:
    def __init__(self, balanced_x, balanced_y, x_test, y_test):
        self.balanced_x = balanced_x
        self.balanced_y = balanced_y
        self.x_test = x_test
        self.y_test = y_test

    def tfidf(self):
        vectorizer = TfidfVectorizer(ngram_range=(1,2))
        vectors = vectorizer.fit_transform(self.balanced_x)
        return vectors

    def fit(self):
        vectors = tfidf()
        classifier = LinearSVC()
        # train the classifier
        classifier.fit(vectors, self.y_train)
        return classifier

    def predict(self):
        classifier = fit()
        preds = classifier.predict(self.x_test)
        return preds

    def accuracy_score(self):
        accuracy_score(self.y_test, predict())
        