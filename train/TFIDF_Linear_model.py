from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class TFIDF:
    def __init__(self):
        return
    
    def tfidf(self, x_train, y_train):
        vectorizer = TfidfVectorizer(ngram_range=(1,2))
        vectors = vectorizer.fit_transform(x_train)
    #     return vectors

    # def fit(self):
        # vectors = self.tfidf()
        classifier = LinearSVC()
        # train the classifier
        classifier.fit(vectors, y_train)
        # return classifier

    # def predict(self):
    #     classifier = self.fit()
        # preds = classifier.predict(self.x_test)
        return classifier

    # def accuracy_s(self):
        # return accuracy_score(self.y_test, predict())
        