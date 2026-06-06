# 4.0: Idex

# Container sind Variablen, die mehrere Werte halten können. In den folgenden Kapiteln 
# wirst du lists, tuples, sets und dictionaries kennen lernen. Bevor wir die einzelnen
# container kennen lernen, müssen wir aber erst über den index sprechen.

# Ein index ist ein Integer, den man in den Meisten Programmiersprachen antreffen kann.
# Ein index ist eine Möglichkeit einen bestimmten Wert in einem Container abzurufen.
# Einen idex beginnt man mit 0 zu zählen.

# 1 2 3 4 5 6 7 8 9 10 So würde man in natürlicher Sprache zählen.
# 0 1 2 3 4 5 6 7 8 9  So zählt man mit einem index. 

# Der erste Wert in einem Container hat also immer den index 0.

container = [1, 2, 3, 4, 5] 
# index      0  1  2  3  4

# Wollen wir auf den zweiten Wert im container zugreifen, nutzen wir den index 1. 
# Hier ein Beispiel dafür, wie man auf den zweiten Wert in einem Container zugreift.

print("Ich bin der zweite Wert in unserem Container: ", container[1])

# Nicht jeder container funktioniert mit einem Index. Nur solche, die ordered sind.
# Ein container, der ordered ist, hat eine feste Reihenfolge für seine Werte. Dadurch,
# dass ein ordered container eine feste Reihenfolge für seine Werte hat, können auch 
# duplikate Werte in ihm enthalten sein.

ordered_list = [1, 2, 3, 1, 2, 3]
print()
print("Index 0 von ordered_list: ", ordered_list[0])
print("Index 3 von ordered_list: ", ordered_list[3])
# In dem Beispiel ist der Wert der selbe, obwohl wir Werte an unterschiedlichen idexen abrufen.

# Ein container kann auch unordered sein. In ihm sind dann keine duplicaten werde zugelassen, 
# weil man in ihm die Werte nur anhand des Wertes abrufen kann. Gäbe es duplikate Werte, wäre
# das Ergebnis nicht mehr eindeutig. Das würde zu einem Fehler führen. Auf unordered container 
# gehen wir noch in den Kapiteln sets und dictionaries ein.

# TODO: 
# 1. Gib mit print() den vierten Wert von container aus.
# 2. Gib mit print() den ersten Wert von container aus.