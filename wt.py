import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = "Hello! How are you doing today? NLP is fun and exciting."
tokens = word_tokenize(text)
print(tokens)

tokens = [word for word in tokens if word.isalnum()]
print(tokens)

tokens = [word.lower() for word in tokens]
print(tokens)

from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
print(filtered_tokens)

