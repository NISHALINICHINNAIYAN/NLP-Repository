import re
from bs4 import BeautifulSoup
import nltk
nltk.download('averaged_perceptron_tagger')


text1= """1.Into this graceful setting was fitted an architectural fabric that was traditional,
subdued, and generally harmonious, and which remains substantially intact. Its
spatial composition was carefully planned. To create the ideal middle-class suburb
of 1907, the original deeds of sale incorporated clauses that required adherence to
a plan for the arrangement of homes.<html> Building zones were created that placed a
minimum value on construction costs.The most expensive homes at a value of at
least $2,500 were built near Montfort Hall on Boylan Avenue <html>. "Dwelling's on the
secondary streets such as Kinsey and Cutler were to cost at least $2,000 and the
least expensive homes on streets that made up the outer fringes of the subdivision
like Lenoir and South streets!"."""

text2= """2.<p> Thus, there are tall, substantial (but architecturally conservative), large woodframed dwellings in Boylan Heights (predominantly Queen Anne/Colonial
Hybrid, Colonial Box or Foursquare, and Dutch Colonial) along Boylan Avenue
in particular, which as a result has an air of dominance in the neighborhood <p>.
Nevertheless, it might be said that Boylan's Heights is the suburb of the bungalow.
Generous numbers of this popular style of house descend the hillside flanking the
Boylan Avenue spine?.<br> The bungalow’s infinite variety of scale, size, shape, and
detail can be seen in Boylan Heights and demonstrates the form’s importance as a
staple for housing the rising middle-class <br>."""

print("REMOVE SPECIAL CHARACTERS:")

clean_text1 = re.sub(r'[^a-zA-Z0-9\s]','',text1)
print(clean_text1)

clean_text2 = re.sub(r'[^a-zA-Z0-9\s]', '', text2)
print(clean_text2)

print("REMOVE HTML TAGS:")

soup = BeautifulSoup(text1,"html.parser")
clean_text1 =soup.get_text()
print(clean_text1)

soup = BeautifulSoup(text2,"html.parser")
clean_text2 =soup.get_text()
print(clean_text2)

print("REMOVE UNWANTED VERB AND PRONOUNS:")

tokens = nltk.word_tokenize(text1)
pos_tags =nltk.pos_tag(tokens)

filtered_words = [word for word, tag in pos_tags if tag not in ['VB','VBD','VBG','VBM','VBP','VBZ','PRP']]
clean_text1 = ' '.join(filtered_words)
print(clean_text1)

tokens = nltk.word_tokenize(text2)
pos_tags =nltk.pos_tag(tokens)

filtered_words = [word for word, tag in pos_tags if tag not in ['VB','VBD','VBG','VBM','VBP','VBZ','PRP']]
clean_text2 = ' '.join(filtered_words)
print(clean_text2)

print("SPLIT THE TEXT INTO SENTENCES:")

sentences = nltk.sent_tokenize(text1)
print(sentences)

sentences = nltk.sent_tokenize(text2)
print(sentences)

print("SPLIT THE TEXT INTO WORDS:")

words = nltk.word_tokenize(text1)
print(words)

words = nltk.word_tokenize(text2)
print(words)






