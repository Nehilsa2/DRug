import nltk
import re  #provides support for regex
from nltk.tokenize import word_tokenize #To splits the input text into individual words (tokens)
from Drug_keywords import drug_keywords

nltk.download('punkt_tab')
nltk.download('punkt') #Dataset for tokenizing text into words

def detect_drug_keywords(text):

    tokens = word_tokenize(text.lower()) #Tokenize the text

    text = ' '.join(tokens) #adding back to string for regex 

    found_keywords=[]  #To store any detected keywords

    for keyword in drug_keywords:    #search keyword in text if found append it to array
        if re.search(keyword,text):
            found_keywords.append(keyword.strip(r'\b'))


return found_keywords if(found_keywords) else "No drug-related keywords found."



sample_text = ""
result = detect_drug_keywords(sample_text)
print(result)