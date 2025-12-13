import pandas as pd
import sys
from src.model import PhishingModel


def main():
    # Command format check
    if len(sys.argv) != 3:
        print("Usage: python -m src.train data/urls.csv model.joblib")
        return

    data_path = sys.argv[1]
    model_path = sys.argv[2]

    # Load dataset
    df = pd.read_csv(data_path)
    urls = df["url"].tolist()
    labels = df["label"].tolist()

    # Train model
    model = PhishingModel()
    model.train(urls, labels)
    model.save(model_path)

    print("Model trained and saved to:", model_path)


if __name__ == "__main__":
    main()