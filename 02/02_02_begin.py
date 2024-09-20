from string import punctuation
from collections import Counter
from collections import defaultdict

post_comments_labels = [
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
    ("I love this product", "pos"),
    ("I hate this product", "neg"),
    ("This product is ok", "neu"),
]

class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": [], "neu": []}
        self.sample_count = len(samples)
        for text, label in samples:
            self.mapping[label]+= self.tokenize(text)
        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])
        self.neu_counter = Counter(self.mapping["neu"])
    
    @staticmethod
    def tokenize(text):
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )
    
    def classify(self, text):
        tokens = self.tokenize(text)
        pos = []
        neg = []
        neu = []
        
        for token in tokens:
            pos.append(self.pos_counter[token]/self.sample_count)
            neg.append(self.neg_counter[token])
            neu.append(self.neu_counter[token])