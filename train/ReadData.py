from Preprocess import Preprocess

def readCSVData(fileName):
    star= []
    review = []
    p = Preprocess()
    with open(fileName) as csv_file:
        for row in csv_file:
            row = row.split('<fff>')
            star.append(row[0])
            review.append(p.doPreprocess(row[1]))
    review, star = p.balance_classes(review, star)
    return review, star

def readTXTData(fileName):
    star = []
    review = []
    p = Preprocess()
    with open(fileName, 'r') as fp:
        line = fp.readline()
        while line:
            star.append(line[0])
            review.append(p.doPreprocess(line[2:]))
            line = fp.readline()
    return p.balance_classes(review, star)

review, star = readCSVData('data_final2.csv')
print(len(review))