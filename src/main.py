from Lexical import Lexical

txt = input('Enter Text:')
lexical = Lexical(txt)
print("Verbs in text: ",lexical.get_verbs())
print("Names: ",lexical.get_people_names())