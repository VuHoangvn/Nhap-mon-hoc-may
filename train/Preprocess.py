import re
import string
from pyvi import ViTokenizer, ViPosTagger, ViUtils
import csv
from collections import Counter


class Preprocess:
    def __init__(self):
        stop_word = []
        with open('stopword.txt') as fp:
            for row in fp:
                stop_word.append(row.strip())
        stop_word = set(stop_word)
        self.stop_word = stop_word
        return
    @staticmethod
    def readStopWord(self):
        stop_word = []
        with open('stopword.txt') as fp:
            for row in fp:
                stop_word.append(row.strip())
        stop_word = set(stop_word)
        
        return stop_word

    def replaceCompositUnicode(self, str):
        str = str.replace('à', 'à')
        str = str.replace('ả', 'ả')
        str = str.replace('ã', 'ã')
        str = str.replace('á', 'á')
        str = str.replace('ạ', 'ạ')
        str = str.replace('ấ', 'ấ')
        str = str.replace('ầ', 'ầ')
        str = str.replace('ậ', 'ậ')
        str = str.replace('ẩ', 'ẩ')
        str = str.replace('ẫ', 'ẫ')
        str = str.replace('ắ', 'ắ')
        str = str.replace('ằ', 'ằ')
        str = str.replace('ặ', 'ặ')
        str = str.replace('ẳ', 'ẳ')
        str = str.replace('ẵ', 'ẵ')
        str = str.replace('è', 'è')
        str = str.replace('ẻ', 'ẻ')
        str = str.replace('ẽ', 'ẽ')
        str = str.replace('é', 'é')
        str = str.replace('ẹ', 'ẹ')
        str = str.replace('ế', 'ế')
        str = str.replace('ề', 'ề')
        str = str.replace('ệ', 'ệ')
        str = str.replace('ể', 'ể')
        str = str.replace('ễ', 'ễ')
        str = str.replace('ì', 'ì')
        str = str.replace('ỉ', 'ỉ')
        str = str.replace('ĩ', 'ĩ')
        str = str.replace('í', 'í')
        str = str.replace('ị', 'ị')
        str = str.replace('ò', 'ò')
        str = str.replace('ỏ', 'ỏ')
        str = str.replace('õ', 'õ')
        str = str.replace('ó', 'ó')
        str = str.replace('ọ', 'ọ')
        str = str.replace('ố', 'ố')
        str = str.replace('ồ', 'ồ')
        str = str.replace('ộ', 'ộ')
        str = str.replace('ổ', 'ổ')
        str = str.replace('ỗ', 'ỗ')
        str = str.replace('ớ', 'ớ')
        str = str.replace('ờ', 'ờ')
        str = str.replace('ợ', 'ợ')
        str = str.replace('ở', 'ở')
        str = str.replace('ỡ', 'ỡ')
        str = str.replace('ù', 'ù')
        str = str.replace('ủ', 'ủ')
        str = str.replace('ũ', 'ũ')
        str = str.replace('ú', 'ú')
        str = str.replace('ụ', 'ụ')
        str = str.replace('ứ', 'ứ')
        str = str.replace('ừ', 'ừ')
        str = str.replace('ự', 'ự')
        str = str.replace('ử', 'ử')
        str = str.replace('ữ', 'ữ')
        str = str.replace('ỳ', 'ỳ')
        str = str.replace('ỷ', 'ỷ')
        str = str.replace('ỹ', 'ỹ')
        str = str.replace('ý', 'ý')
        str = str.replace('ỵ', 'ỵ')
        return str

    def removeSpecialCharacter(self, str):
        # Loai bo ki tu dac biet
        str = re.sub(r'[^0-9a-zăâđêôơưàảãáạấầậẩẫắằặẳẵèẻẽéẹếềệểễìỉĩíịòỏõóọốồộổỗớờợởỡùủũúụứừựửữỳỷỹýỵ,\s\*]+', ' ',str)
        # Xoa bo khoang trang dai
        str = re.sub(' {2,}', ' ', str)
        return str

    def replaceAcronym(self, str):
        # mot so tu viet tat
        # 1*->1 sao, 2*-> 2 sao,...
        str = re.sub('(^| )([0-9])\*($| )', r'\1sao\2', str)
        # 1sao -> 1 sao, 2sao -> 2 sao, ...
        str = re.sub('(^| )([0-9])sao($| )', r'\1sao\2', str)
        # * -> sao
        str = re.sub("(^| )\*($| )", r"\1sao\2", str)
        # s -> sao
        str = re.sub("(^| )s($| )", r"\1sao\2", str)
        str = re.sub("(^| )sp($| )", r"\1sản phẩm\2", str)
        str = re.sub("(^| )rat($| )", r"\1rất\2", str)
        str = re.sub("(^| )dang($| )", r"\1đáng\2", str)
        str = re.sub("(^| )nhiu($| )", r"\1nhiều\2", str)
        str = re.sub("(^| )nhìu($| )", r"\1nhiều\2", str)
        str = re.sub("(^| )nhieu($| )", r"\1nhiều\2", str)
        str = re.sub("(^| )tot($| )", r"\1tốt\2", str)
        str = re.sub("(^| )tôt($| )", r"\1tốt\2", str)
        str = re.sub("(^| )muot($| )", r"\1mượt\2", str)
        str = re.sub("(^| )muọt($| )", r"\1mượt\2", str)
        str = re.sub("(^| )mươt($| )", r"\1mượt\2", str)
        str = re.sub("(^| )may($| )", r"\1máy\2", str)
        str = re.sub("(^| )tr($| )", r"\1trước\2", str)
        str = re.sub("(^| )trc($| )", r"\1trước\2", str)
        str = re.sub("(^| )ae($| )", r"\1anh em\2", str)
        str = re.sub("(^| )đc($| )", r"\1được\2", str)
        str = re.sub("(^| )dc($| )", r"\1được\2", str)
        str = re.sub("(^| )dk($| )", r"\1được\2", str)
        str = re.sub("(^| )đk($| )", r"\1được\2", str)
        str = re.sub("(^| )k($| )", r"\1không\2", str)
        str = re.sub("(^| )ko($| )", r"\1không\2", str)
        str = re.sub("(^| )kg($| )", r"\1không\2", str)
        str = re.sub("(^| )kh($| )", r"\1không\2", str)
        str = re.sub("(^| )hk($| )", r"\1không\2", str)
        str = re.sub("(^| )khg($| )", r"\1không\2", str)
        str = re.sub("(^| )r($| )", r"\1rồi\2", str)
        str = re.sub("(^| )m($| )", r"\1mình\2", str)
        str = re.sub("(^| )mh($| )", r"\1mình\2", str)
        str = re.sub("(^| )mih($| )", r"\1mình\2", str)
        str = re.sub("(^| )mìh($| )", r"\1mình\2", str)
        str = re.sub("(^| )mk($| )", r"\1mình\2", str)
        str = re.sub("(^| )mik($| )", r"\1mình\2", str)
        str = re.sub("(^| )bh($| )", r"\1bao giờ\2", str)
        str = re.sub("(^| )h($| )", r"\1giờ\2", str)
        str = re.sub("(^| )jo($| )", r"\1giờ\2", str)
        str = re.sub("(^| )z($| )", r"\1vậy\2", str)
        str = re.sub("(^| )j($| )", r"\1gì\2", str)
        str = re.sub("(^| )cx($| )", r"\1cũng\2", str)
        str = re.sub("(^| )vs($| )", r"\1với\2", str)
        str = re.sub("(^| )ah($| )", r"\1à\2", str)
        str = re.sub("(^| )ak($| )", r"\1à\2", str)
        str = re.sub("(^| )ntn($| )", r"\1như thế nào\2", str)
        str = re.sub("(^| )lm($| )", r"\1làm\2", str)
        str = re.sub("(^| )trc($| )", r"\1trước\2", str)
        str = re.sub("(^| )t2($| )", r"\1thứ 2\2", str)
        str = re.sub("(^| )cn($| )", r"\1chủ nhật\2", str)
        str = re.sub("(^| )t3($| )", r"\1thứ 3\2", str)
        str = re.sub("(^| )t4($| )", r"\1thứ 4\2", str)
        str = re.sub("(^| )t5($| )", r"\1thứ 5\2", str)
        str = re.sub("(^| )t6($| )", r"\1thứ 6\2", str)
        str = re.sub("(^| )t7($| )", r"\1thứ 7\2", str)
        str = re.sub("(^| )mn($| )", r"\1mọi người\2", str)
        return str

    def doPreprocess(self, str):
        str = str.lower()
        str = self.replaceCompositUnicode(str)
        str = self.removeSpecialCharacter(str)
        str = self.replaceAcronym(str)
        # to lower case
        
        # number removing
#         str = re.sub(r'\d+', '', str)
        # remove punctuation
#         str = str.translate(str.maketrans("","", string.punctuation))
        # remove white spaces
#         str = str.strip()
#         str = re.sub(' +', ' ', str)
        # # tokenize by pyvi
#         str = ViTokenizer.tokenize(str)
        # # remove stopword
        # str = str.split()
        # str = [i for i in str if not i in self.stop_word]
        # str = ' '.join(str)
        return str

    def balance_classes(self,xs, ys):
        freqs = Counter(ys)
        max_allowable = freqs.most_common()[-1][1]
        num_added = {clss: 0 for clss in freqs.keys()}
        new_ys = []
        new_xs = []
        for i, y in enumerate(ys):
            if num_added[y] < max_allowable:
                new_ys.append(y)
                new_xs.append(xs[i])
                num_added[y] += 1
        return new_xs, new_ys


