# src/run.py
from src.model import PhishingModel

def main():
    model = PhishingModel()
    model.load("model.joblib")

    print("=== AI Phishing URL Detector ===")
    print("Type 'exit' to quit\n")

    while True:
        url = input("Enter URL: ").strip()

        if url.lower() == "exit":
            print("Exiting program.")
            break

        probability = model.predict(url)

        if probability > 0.5:
            print(f"Result: PHISHING ⚠️  (Probability: {probability:.2f})\n")
        else:
            print(f"Result: SAFE ✅  (Probability: {probability:.2f})\n")

if __name__ == "__main__":
    main()