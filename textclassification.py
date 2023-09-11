import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the 20 Newsgroups dataset
newsgroups = fetch_20newsgroups(subset='all')

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(newsgroups.data, newsgroups.target, test_size=0.25, random_state=42)

# Create a pipeline for text classification
# We'll use TF-IDF vectorizer for feature extraction and Multinomial Naive Bayes as the classifier
text_classifier = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the classifier
text_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = text_classifier.predict(X_test)

# Evaluate the classifier
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report shows precision, recall, F1-score for each class
print(metrics.classification_report(y_test, y_pred, target_names=newsgroups.target_names))

# Confusion matrix shows the number of correct and incorrect predictions for each class
confusion_mat = metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion_mat)
