import spacy
import random

nlp = spacy.load('en')
dick = open("moby10b.txt", "r")
myBook = ""
for x in dick:
    myBook = myBook+x
doc = nlp(myBook)
tokens = []
NOUN = []
NUM = []
SPACE = []
PUNCT = []
PRON = []
PROPN = []
DET = []
ADV = []
VERB = []
ADJ = []
CCONJ = []
ADP = []
PART = []
INTJ = []
X = []
SYM = []

for token in doc:
    if token.pos_ == "NOUN":
        if not NOUN.__contains__(token.text):
            NOUN.append(token.text)
    if token.pos_ == "NUM":
        if not NUM.__contains__(token.text):
            NUM.append(token.text)
    if token.pos_ == "SPACE":
        if not SPACE.__contains__(token.text):
            SPACE.append(token.text)
    if token.pos_ == "PUNCT":
        if not PUNCT.__contains__(token.text):
            PUNCT.append(token.text)
    if token.pos_ == "PRON":
        if not PRON.__contains__(token.text):
            PRON.append(token.text)
    if token.pos_ == "PROPN":
        if not PROPN.__contains__(token.text):
            PROPN.append(token.text)
    if token.pos_ == "DET":
        if not DET.__contains__(token.text):
            DET.append(token.text)
    if token.pos_ == "VERB":
        if not VERB.__contains__(token.text):
            VERB.append(token.text)
    if token.pos_ == "ADJ":
        if not ADJ.__contains__(token.text):
            ADJ.append(token.text)
    if token.pos_ == "CCONJ":
        if not CCONJ.__contains__(token.text):
            CCONJ.append(token.text)
    if token.pos_ == "ADP":
        if not ADP.__contains__(token.text):
            ADP.append(token.text)
    if token.pos_ == "PART":
        if not PART.__contains__(token.text):
            PART.append(token.text)
    if token.pos_ == "INTJ":
        if not INTJ.__contains__(token.text):
            INTJ.append(token.text)
    if token.pos_ == "X":
        if not X.__contains__(token.text):
            X.append(token.text)
    if token.pos_ == "SYM":
        if not SYM.__contains__(token.text):
            SYM.append(token.text)

for x in NOUN:
    print(x)
print("*************************************NOUN^***************************************")
for x in NUM:
    print(x)
print("************************************NUM^*********************************************")
for x in SPACE:
    print(x)
print("***********************************Space^********************************************")
for x in PUNCT:
    print(x)
print("*********************************Punct^************************************************")
for x in DET:
    print(x)
print("**********************************Det^************************************************")
for x in VERB:
    print(x)
print("********************************verb^**************************************************")
for x in ADJ:
    print(x)
print("*******************************Adjective^****************************************************")
for x in CCONJ:
    print(x)
print("******************************Conj^**************************************************")
for x in ADP:
    print(x)
print("********************************ADP^**************************************************")
for x in PART:
    print(x)
print("*****************************Part^**************************************************")
for x in NOUN:
    print(x)
print("***************************Noun^******************************************************")
for x in X:
    print(x)
print("******************************x^***************************************************")
for x in SYM:
    print(x)
print("****************************Symbol^******************************************************")
for x in PROPN:
    print(x)
print("*******************************propn^****************************************************")
for x in INTJ:
    print(x)
print("*******************************Intj^****************************************************")
f = open("sentences.txt", "w")
counter=1
for x in range(100):
    f.write(counter.__str__())
    f.write(": ")
    f.write(PROPN.__getitem__(random.randint(0, PROPN.__len__() - 1)))
    f.write(" ")
    f.write(CCONJ.__getitem__(random.randint(0, CCONJ.__len__() - 1)))
    f.write(" ")
    f.write(PROPN.__getitem__(random.randint(0, PROPN.__len__() - 1)))
    f.write(" ")
    f.write(VERB.__getitem__(random.randint(0, VERB.__len__() - 1)))
    f.write(" ")
    f.write(ADJ.__getitem__(random.randint(0, ADJ.__len__() - 1)))
    f.write(" ")
    f.write("apple.")
    f.write("\n")
    counter = counter +1
f.close()