from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from .features import tokenize_url


class PhishingModel:
    """
    AI model for phishing URL detection
    """

    def __init__(self):
        # Convert text tokens into numbers
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))

        # Logistic Regression classifier
        self.model = LogisticRegression(max_iter=1000)

    def train(self, urls, labels):
        """
        Train the model on URLs and labels
        """
        texts = [tokenize_url(url) for url in urls]
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, url):
        """
        Predict phishing probability for a single URL
        """
        text = tokenize_url(url)
        X = self.vectorizer.transform([text])
        probability = self.model.predict_proba(X)[0][1]
        return probability

    def save(self, path):
        """
        Save trained model to disk
        """
        joblib.dump(
            {
                "vectorizer": self.vectorizer,
                "model": self.model
            },
            path
        )

    def load(self, path):
        """
        Load trained model from disk
        """
        data = joblib.load(path)
        self.vectorizer = data["vectorizer"]
        self.model = data["model"]