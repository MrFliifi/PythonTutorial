# 3.2: try except finally

# Währen if-Statements und match-cases verwendet werden, um Entscheidungen zu treffen,
# wird ein try-except-Block verwendet, um Fehler aufzufangen.
# Hierbei gibt es wieder drei keywords:
# - try + body
# - exept + body
# - finally + body

# Ein try-except-Block wird von Oben nach Unten gelesen. Zunächst versucht das Programm
# den Body von try auszuführen. Ist das erfolgreich, wird der Rest vom Block ignoriert.
# Schlägt es fehl, wird der try Block an der Stelle wo der fehler auftritt abgebrochen. 
# Das Programm springt dann zum except und führt dessen Body aus. 
# try und except sind Pflicht. Verwendet man ein try, muss man auch ein except verwenden.
# finally hingegen ist optional. finally wird immer ausgeführt. Dabei ist es völlig egal,
# ob try erfolgreich durchgelaufen ist, oder nicht.  

try:
    print("Mich siehst du immer, weil ich vor dem Fehler stehe!")
    x = 0
    result = 10 / x
    print("Mich siehst du nur, wenn alles gut geht!")
# Hier kann man genau angeben, welchen Fehler man angezeigt bekommt.
# Wenn du mehr dazu lesen willst, findest du hier die Dokumentation:
# https://docs.python.org/3/library/exceptions.html
except ZeroDivisionError: 
    print("Division durch Null ist nicht erlaubt!")
finally:
    print("Mich siehst du immer, weil ich im body von finally bin!")
    
# TODO:
# 1. verändere das Beispiel so, dass der body von except nicht ausgeführt wird.
