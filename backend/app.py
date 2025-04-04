# backend/app.py

from flask import Flask, request, jsonify
from model import predict_text

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Expects a JSON payload with 'text' key.
    Returns the predicted label.
    """
    data = request.get_json(force=True)
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    prediction = predict_text(text)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
