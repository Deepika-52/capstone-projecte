# backend/model.py

import joblib
import os

MODEL_PATH = 'harmful_content_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

# Load model and vectorizer when the module is imported
if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    raise FileNotFoundError("Model or vectorizer not found. Run train_model.py first.")

def predict_text(text):
    """
    Predicts the label for the given text.
    """
    X_vect = vectorizer.transform([text])
    prediction = model.predict(X_vect)[0]
    return prediction
