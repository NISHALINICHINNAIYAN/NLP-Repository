import re
import spacy
from langdetect import detect_langs
from googletrans import Translator

from google_trans_new import google_translator
from textblob import TextBlob
from bs4 import BeautifulSoup
import nltk
from translator import translator

nltk.download('averaged_perceptron_tagger')

text = """1.Into this graceful setting was fitted an architectural fabric that was traditional,
subdued, and generally harmonious, and which remains substantially intact. Its
spatial composition was carefully planned. To create the ideal middle-class suburb
of 1907, the original deeds of sale incorporated clauses that required adherence to
a plan for the arrangement of homes.<html> Building zones were created that placed a
minimum value on construction costs.The most expensive homes at a value of at
least $2,500 were built near Montfort Hall on Boylan Avenue <html>. "Dwelling's on the
secondary streets such as Kinsey and Cutler were to cost at least $2,000 and the
least expensive homes on streets that made up the outer fringes of the subdivision
like Lenoir and South streets!".
2.<p> Thus, there are tall, substantial (but architecturally conservative), large woodframed dwellings in Boylan Heights (predominantly Queen Anne/Colonial
Hybrid, Colonial Box or Foursquare, and Dutch Colonial) along Boylan Avenue
in particular, which as a result has an air of dominance in the neighborhood <p>.
Nevertheless, it might be said that Boylan's Heights is the suburb of the bungalow.
Generous numbers of this popular style of house descend the hillside flanking the
Boylan Avenue spine?.<br> The bungalow’s infinite variety of scale, size, shape, and
detail can be seen in Boylan Heights and demonstrates the form’s importance as a
staple for housing the rising middle-class <br>."""

print("REMOVE HTML TAGS:")

soup = BeautifulSoup(text, "html.parser")
clean_text = soup.get_text()
print(clean_text)

print("REMOVE SPECIAL CHARACTERS:")

clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', clean_text)
print(clean_text)

print("REMOVE UNWANTED VERB AND PRONOUNS:")

tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

filtered_words = [word for word, tag in pos_tags if tag not in ['VB', 'VBD', 'VBG', 'VBM', 'VBP', 'VBZ', 'PRP']]
clean_text = ' '.join(filtered_words)
print(clean_text)

print("SPLIT THE TEXT INTO SENTENCES:")

clean_text = nltk.sent_tokenize(text)
print(clean_text)

print("SPLIT THE TEXT INTO WORDS:")

clean_text = nltk.word_tokenize(text)
print(clean_text)

def search_word_in_split_words(clean_text: object, search_word: object) -> object:
    for word in clean_text:
        if search_word  in word:
            return word
    return None

search_word = input("Enter the word to search: ")
matched_word: object = search_word_in_split_words(clean_text, search_word)
print(f"Word {matched_word} found in the split words list.")
if matched_word:
    search_language = (detect_langs(matched_word))
    print(f"The language of the search word is:{search_language}")
    target_language = input("Enter the target language for translation: ")
    translator = Translator()
    translated_word = translator.translate (matched_word, dest=target_language).text
    print(f" The translated word in {target_language} is : {translated_word}")
else:
    print(f"The word '{matched_word}' was not found in the clean_text.")

