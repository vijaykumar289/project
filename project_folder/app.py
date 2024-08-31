from flask import Flask, request, render_template
import joblib
import numpy as np
from feature_extraction import extract_features

# Load the model
model = joblib.load('phishing_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = np.array(extract_features(url)).reshape(1, -1)
    prediction = model.predict(features)
    result = 'Phishing' if prediction == 1 else 'Legitimate'
    return render_template('index.html', url=url, result=result)

if __name__ == "__main__":
    app.run(debug=True)
