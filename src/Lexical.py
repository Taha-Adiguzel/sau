import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')

class Lexical:
    def __init__(self,text):
        self.text = text

    def get_verbs(self):
        words = word_tokenize(self.text)
        tagged_words = pos_tag(words) #kelimeleri etiketler özne,yüklem,edat vb..

        verbs = [word for word,tag in tagged_words if tag.startswith('VB')]
        return verbs