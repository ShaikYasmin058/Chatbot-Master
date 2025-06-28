import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

patterns = []
responses = []

# Read patterns and responses from Example.template
with open("Example.template", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Skip comments and blank lines
        if "@" in line:
            pattern, response = line.split("@", 1)
        elif "=" in line:
            pattern, response = line.split("=", 1)
        else:
            continue  # Skip malformed lines
        patterns.append(pattern.strip().lower())
        responses.append(response.strip())

# Train the model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
model = MultinomialNB()
model.fit(X, responses)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model training complete. Files saved: model.pkl, vectorizer.pkl")
