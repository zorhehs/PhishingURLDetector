import sys
from src.model import PhishingModel


def main():
    # Command format check
    if len(sys.argv) != 3:
        print("Usage: python -m src.predict model.joblib URL")
        return

    model_path = sys.argv[1]
    url = sys.argv[2]

    # Load trained model
    model = PhishingModel()
    model.load(model_path)

    # Predict
    probability = model.predict(url)

    print("URL:", url)
    print("Phishing Probability:", round(probability, 4))

    if probability > 0.5:
        print("Result: PHISHING ⚠️")
    else:
        print("Result: SAFE ✅")


if __name__ == "__main__":
    main()