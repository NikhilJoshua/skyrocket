# This is a sample Python script.
import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
dv = CountVectorizer()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
df = pd.read_csv('amazon_one_plus_reviews.csv')
sia = SentimentIntensityAnalyzer()


# for title in df['review_title']:
#     print(title, " ", sia.polarity_scores(title))
X = dv.fit_transform(df['product'].values.astype('U'))
sv = dv.vocabulary_

print(len(df['product']))

#sv2 = dict(sorted(sv.items(), reverse=True))

print(sv2)

