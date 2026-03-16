from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "selling ransomware access",
    "database breach dump",
    "buying corporate access",
    "crypto scam"
]

labels = [
    "ransomware",
    "data_leak",
    "initial_access",
    "fraud"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

model = MultinomialNB()

model.fit(X, labels)

test = vectorizer.transform(["selling ransomware builder"])

print("Threat classification:", model.predict(test)[0])
