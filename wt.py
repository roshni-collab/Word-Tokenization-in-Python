import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

text = "Hello! How are you doing today? NLP is fun and exciting."
tokens = word_tokenize(text)
print(tokens)

def tokenize_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return words

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
print(filtered_tokens)


user_text = input("Enter a sentence for tokenization: ")
tokens = tokenize_text(user_text)
print(tokens)
