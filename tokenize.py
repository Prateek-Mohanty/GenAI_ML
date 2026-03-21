import streamlit as st
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
import nltk

nltk.download('wordnet',quiet=True)

st.title("Tokenization Example")

corpus = st.text_input("Enter your corpus:")

data = sent_tokenize(corpus)

st.write("After sentence tokenization")
st.write(data)

st.write("After word tokenization")
words_list=[]
for sentence in data:
   words_list.append(word_tokenize(sentence))

st.write(words_list)

lemmatizer = WordNetLemmatizer()

st.write("Will display stem words after you enter corpus")
stemming = PorterStemmer()
snowball_stem = SnowballStemmer('english')
for list in words_list:
   for word in list:
    st.write(f"Porter ----> {stemming.stem(word)}")
    st.write(f"Snowball ----> {snowball_stem.stem(word)}")
    st.write(f"Lemma ----> {lemmatizer.lemmatize(word,pos='v')}")
