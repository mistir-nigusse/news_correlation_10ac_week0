import os
import sys
import glob
import re
import json
import datetime
from collections import Counter
from collections import Counter

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def get_domain(url):
    return re.sub(r'^www.', '', re.sub(r'^https?://', '', url.split('/')[2]))


analyzer = SentimentIntensityAnalyzer()
def get_sentiment_score(text):
    text_str = str(text)  # convert to a string
    return analyzer.polarity_scores(text_str)['compound']

def get_number_of_words(text):
    return len(text.split())

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and mentions
    text = re.sub(r'<@[^>]+>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization using NLTK
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming using NLTK PorterStemmer
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    # Join tokens back into a single string
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text