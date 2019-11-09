from ReadData import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


x_train, y_train = readCSVData('data_final2.csv')
x_test, y_test = readTXTData('train.txt')
x_train = x_train + x_test[:450]
y_train = y_train + y_test[:450]
y_test = y_test[451:499]
x_test = x_test[451:499]


vectorizer = TfidfVectorizer(ngram_range=(1,2))
vectors = vectorizer.fit_transform(x_train)
    #     return vectors

    # def fit(self):
        # vectors = self.tfidf()
classifier = LinearSVC()
        # train the classifier
classifier.fit(vectors, y_train)
vectors1 = vectorizer.transform(x_test)
predict = classifier.predict(vectors1)
ac = accuracy_score(y_test, predict)
print(ac)