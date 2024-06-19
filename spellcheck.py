from spellchecker import SpellChecker

fp = open("pdftext.txt", "r")

words = fp.read()
words_list = words.split(" ")
# print(words_list)

spell = SpellChecker(distance=1)

misspelled = spell.unknown(words_list)

fp = open("spelled.txt", "w")
for word in misspelled:
    incorrect = spell.correction(word)
    
    if incorrect:
        fp.write(incorrect)
        fp.write("\n")