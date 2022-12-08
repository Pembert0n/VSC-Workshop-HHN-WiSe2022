text = ["Nennt", "mich", "Ishmael"]
# gewünschtes Dictionary:
# {"n": 3, "e": 2, "t": 1,
#  "m": 2, "i": 2, "c": 1,
#  "h": 2, "s": 1, "a": 1,
#  "l": 1}

############################################

# Funktion zum Zählen von Buchstaben
# innerhalb eines Worts
def count_letters_in_word(word):
    letters = {}
    # durch alle Buchstaben iterieren
    for l in word:
        # prüfen, ob das aktuelle Zeichen
        # schon mal vorkam
        if l.lower() not in letters:
            # falls nicht: Wert auf 0 setzen
            letters[l.lower()] = 0
        # Wert um 1 erhöhen
        letters[l.lower()] += 1
    return letters

############################################

# durch alle Wörter iterieren
for current_word in text:
    # Funktion auf jedes Wort anwenden
    letters = count_letters_in_word(current_word)

############################################

# entspricht das Dictionary dem
# gewünschten Wert?
print(letters)