# Libraries for preprocessing function
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def processData(message):
    lemma = WordNetLemmatizer()
    review = re.sub('\W', ' ', message)
    review = review.lower()
    review = review.split()
    lemmatized_review = [lemma.lemmatize(word) for word in review if word not in stopwords.words('english')]
    review = ' '.join(lemmatized_review)
    return review