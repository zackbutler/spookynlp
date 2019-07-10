#Package Imports
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot
import string

#Download and import stopwords 
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')

#Load data and display head
data = pd.read_csv("train/train.csv")
print(data.head())

def preprocessing(data):
    """
    Manipulates input text, removing things like punctuation, casing, and stopwords
    Adds new columns with information to possibly be used as features
    
    :param data: DataFrame object containing author's text
    """
    
    processedLines = []
    processedAsString = []
    stopWordCount = []
    
    for currLine in data['text']:
        
        currLine = currLine.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
        
        stopWordCount.append(len([i for i in currLine.split() if i in stop])) # find stopword count
        
        # split text into individual words, undercase, and remove all stopwords
        currLine = currLine.lower().split()
        currLine = [word for word in currLine if not word in stop]
        
        processedLines.append(currLine)
        processedAsString.append(' '.join(currLine))

    data['processedText'] = processedLines
    data['processedTextAsString'] = processedAsString
    data['stopWordCount'] = stopWordCount