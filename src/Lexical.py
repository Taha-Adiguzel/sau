import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')
nlp = spacy.load("en_core_web_sm")
class Lexical:
    def __init__(self,text):
        self.text = text

    def get_verbs(self):
        words = word_tokenize(self.text)
        tagged_words = pos_tag(words) #kelimeleri etiketler özne,yüklem,edat vb..

        verbs = [word for word,tag in tagged_words if tag.startswith('VB')]
        return verbs
    
    def get_people_names(self):
        doc = nlp(self.text)
        names = [entity.text for entity in doc.ents if entity.label_ == "PERSON"]
        return names