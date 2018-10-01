import inputParameters
import pandas as pd
import numpy as np
import os
import sys
import glob
from collections import Counter
import re
import string
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import spacy
from spacy.lemmatizer import Lemmatizer
#for sentiment analysis

import pickle
from sklearn import metrics  # import metrics from sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

if __name__ == "__main__":
    # execute only if run as a script
    main()
