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

def get_domain(url):
    return re.sub(r'^www.', '', re.sub(r'^https?://', '', url.split('/')[2]))


analyzer = SentimentIntensityAnalyzer()
def get_sentiment_score(text):
    text_str = str(text)  # convert to a string
    return analyzer.polarity_scores(text_str)['compound']

def get_number_of_words(text):
    return len(text.split())