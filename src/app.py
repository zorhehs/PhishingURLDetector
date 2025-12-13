from flask import Flask, request, render_template_string
from src.model import PhishingModel

app = Flask(__name__)

# Load trained model
model = PhishingModel()
model.load("model.joblib")

HTML = """
<!doctype html>
<html>
<head>
  <title>Phishing URL Detector</title>
  <style>
    body { font-family: Arial; margin: 40px; }
    input { width: 420px; padding: 8px; }
    button { padding: 8px 12px; }
    .safe { color: green; font-weight: bold; }
    .phish { color: red; font-weight: bold; }
  </style>
</head>
<body>
  <h2>AI-Based Phishing URL Detector</h2>

  <form method="post">
    <input name="url" placeholder="Enter URL" required>
    <button type="submit">Predict</button>
  </form>

  {% if result %}
    <p class="{{cls}}">
      {{result}} (Probability: {{prob}})
    </p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    prob = None
    cls = None

    if request.method == "POST":
        url = request.form["url"]
        p = model.predict(url)
        prob = round(p, 4)

        if p > 0.5:
            result = "PHISHING ⚠️"
            cls = "phish"
        else:
            result = "SAFE ✅"
            cls = "safe"

    return render_template_string(HTML, result=result, prob=prob, cls=cls)

if __name__ == "__main__":
 app.run(port=5001)