import streamlit as st
import nltk
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

st.title("Revison")

corpus = st.text_input("Enter your corpus here")
# st.write(corpus)

sentences = sent_tokenize(corpus)

stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(lemmatizer.lemmatize(word.lower(),pos='v')) for word in words if word not in set(stopwords.words('english'))]
    # words = [stemmer.stem(word) for word in words]
    sentences[i] = ' '.join(words)

st.write(sentences)
