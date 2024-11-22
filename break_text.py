from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# pip install nltk

nltk.download('stopwords')
nltk.download('wordnet')


def remove_stop_words(question):
    stop_words = set(stopwords.words('english'))
    # Filter out stopwords and join the words back into a single string
    filtered_words = [word for word in question.split() if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def remove_plural(question):
    lemmatizer = WordNetLemmatizer()
    # Lemmatize each word and join them back into a single string
    lemmatized_words = [lemmatizer.lemmatize(word) for word in question.split()]
    return ' '.join(lemmatized_words)

