# backend/train_model.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df = df[['text', 'label']]  # Ensure only the required columns
    df.dropna(inplace=True)
    df = df[df['text'].str.strip() != '']
    return df

def train_model(df):
    X = df['text']
    y = df['label']

    # Create TF-IDF features (using unigrams and bigrams)
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english', ngram_range=(1, 2))
    X_vect = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42, stratify=y)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))
    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, y_pred))

    return model, vectorizer

if __name__ == '__main__':
    dataset_path = '../content_dataset.csv'  # Adjust the path if needed
    data = load_and_clean_data(dataset_path)
    model, vectorizer = train_model(data)
    joblib.dump(model, 'harmful_content_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    print("Model and vectorizer saved successfully.")
