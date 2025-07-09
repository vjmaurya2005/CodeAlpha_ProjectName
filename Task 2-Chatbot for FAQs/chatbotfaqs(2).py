from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Create FAQ data
faqs = {
     "Is CodeAlpha internship free?": "Yes, CodeAlpha internships are completely free for students and learners.",
    "What is Python?": "Python is a programming language.",
    "What is Machine Learning?": "It helps computers learn from data.",
    "What is CodeAlpha?": "CodeAlpha is a learning platform.",
    "How many tasks do I need to complete in the AI internship?": "You must complete a minimum of 2 out of 4 tasks to be eligible for the certificate.",
   "What is AI?", : "AI stands for Artificial Intelligence.",
    }

# Step 2: Prepare data
questions = list(faqs.keys())
answers = list(faqs.values())

# Step 3: Convert text to numbers using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Step 4: Create chatbot
print("🤖 Chatbot is ready! Type your question or 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)

    index = np.argmax(similarity)

    if similarity[0][index] > 0.3:  # threshold
        print("Chatbot:", answers[index])
    else:
        print("Chatbot: I don't understand. Please try another question.")
