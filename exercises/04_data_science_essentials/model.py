import sklearn
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def prediction():
    df=pd.read_csv('data/talks.csv')

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    vectorized_text = vectorizer.fit_transform(df['description'])
    labels = df[df.year == 2017]['label']
    count_labeled = len(df[df.year == 2017])
    vectorized_text_labeled = vectorized_text[:count_labeled]
    vectorized_text_predict = vectorized_text[count_labeled:]

    X_train, X_test, y_train, y_test = train_test_split(vectorized_text_labeled, labels, test_size=.3)
    classifier = LinearSVC()
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    predicted_talks_vector = classifier.predict(vectorized_text_predict)
    df_2018 = df[df.year==2018]
    predicted_talks_indexes = predicted_talks_vector.nonzero()[0] + count_labeled
    results = df_2018.loc[predicted_talks_indexes][['id', 'description', 'presenters', 'title', 'location']]

    return results.to_dict(orient='records')
