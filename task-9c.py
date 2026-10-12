from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

queries = [
    "Software installation failed",
    "Application crashes frequently",
    "Configuration error in software",
    "Unable to install the application"
]

solutions = [
    "Check system requirements and run the installer again.",
    "Restart the application and update the software.",
    "Verify configuration settings and restart the software.",
    "Check disk space and administrator permissions."
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(queries)

while True:
    user = input("User: ")

    if user.lower() == "exit":
        break

    q = vectorizer.transform([user])
    scores = cosine_similarity(q, matrix).flatten()

    if scores.max() == 0:
        print("Bot: No solution found.")
    else:
        print("Bot:", solutions[scores.argmax()])
