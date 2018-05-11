import sklearn
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def prediction():
    # Exercise A: Load the data
    df = pd.read_csv('data/talks.csv')

    # Exercise B: Feature Extraction
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    year_labeled = 2017
    year_predict = 2018
    vectorized_text_labeled = vectorizer.fit_transform(df[df.year==year_labeled]['description'])
    vectorized_text_predict = vectorizer.transform(df[df.year==year_predict]['description'])

    # Exercise C: Split into Training and Testing Set
    labels = df[df.year == 2017]['label']
    test_size=0.3
    X_train, X_test, y_train, y_test = train_test_split(vectorized_text_labeled, labels, test_size=test_size, random_state=1)

    # Exercise D: Train the model
    classifier = LinearSVC()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    report = sklearn.metrics.classification_report(y_test, y_pred)
    print(report)

    # Exercise E: Make Predictions
    predicted_talks_vector = classifier.predict(vectorized_text_predict)
    df_2018 = df[df.year==2018]
    predicted_talk_indexes = predicted_talks_vector.nonzero()[0] + len(df[df.year==2017])

    # change the empty data frame with your predictions data frame
    results = df_2018.loc[predicted_talk_indexes][['id', 'description', 'presenters', 'title', 'location']]
    return results.to_dict(orient='records')
