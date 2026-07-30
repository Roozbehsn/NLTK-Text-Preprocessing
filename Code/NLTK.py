import nltk
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


passage='''Hi , my name is Roozbeh Seyednozadi and I was born in 9/15/2005 and in Iranian callender it is 1384/6/24 in Mashhad . 
My heigh is 184cm and my weight is about 83kg. You can contact me via roozbehseyednozadi@gmail.com.  
I probably don't have an outstanding characteristic but I can call myself a hardworking person. My commonly used emoji is 😂  . I don't use any hashtag unfortunately
but if i want to say one it is #HALAMadrid.'''

# Part 1 Tokenization
pattern = r'''(?x)                
    \d{4}/\d{1,2}/\d{1,2}
    |
    \d{1,2}/\d{1,2}/\d{4}            
    |                               
    [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}   
    |                                
    \w+(?:'\w+)?
    |
    \#\w+ 
    |  
    [^\x00-\x7F] 
    | 
    [.,!?;:]                   
'''
tokens=nltk.regexp_tokenize(passage,pattern)
print(tokens)

# Part 2 Lemmetization
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
tagged = nltk.pos_tag(tokens)
lemmatizer = WordNetLemmatizer()

lemmas = [
    lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    for word, tag in tagged
]
print(lemmas)
 

#Part 3  Sentence Segmentation
sentences = sent_tokenize(passage)
print(sentences)