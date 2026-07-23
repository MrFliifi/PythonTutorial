# 5.0: While Loops

# Programme werden von Oben nach Unten, Zeile für Zeile ausgeführt. Möchte man einen code-Block
# mehr als ein mal ausführen, muss man die Zeilen entweder doppelt schreiben, oder das Programm 
# mehrmals ausführen. Das wird schnell unübersichtlich und unpraktisch. Deshalb gibt es loops.

# Loops sind eine Möglichkeit code-Blöcke öfters auszuführen, ohne den code mehr als ein mal zu
# schreiben. In diesem Kapitel lernen wir den while-loop kennen. Der while-loop verwendet 
# folgendes keyword:
# - while condition: + body

# Solange die condition im Kopf des while-loops True ist, wird der body des loops immer wieder 
# ausgeführt. Der body wird von Oben nach Unten gelesen. Kommen wir am Ende des bodies an, 
# springen wir wieder in den Kopf des loops und prüfen, ob dieser immer noch True ist. Ist er das
# laufen wir wieder den body durch. Ist er das nicht, wird der body übersprungen und der Rest vom 
# code wird ausgeführt. 
# Hier ein Beispiel:

x = 0 # counter variable
while x < 10: # der loop läuft 10 mal, da die condition erst nach 10 loops > 9 ist.
    print(x)
    x += 1 

isRunning = True

while isRunning:
    print(isRunning)
    isRunning = False # der loop läuft nur ein mal, weil die condition hier nach False ist.

# Bei den oben stehenden Beispielen kann man sehen, dass der body der Schleife das Ergebnis
# der condition verändert. Dadurch verhindern wir einen infinite loop.

# Man kann einen loop auch so schreiben, dass er endlos läuft. Hier ein Beispiel dafür:
# TODO: Entferne die folgenden 4 #, um dir den Output in der Konsole anzusehen.

# x = 0 
# while True: # Die condition ist als True hard coded und kann deshalb nie False sein -> infinite
#    print(x)
#    x += 1

# STRG + c um das Programm zu beenden

# Üblicherweise versucht man infinite loops zu vermeiden. Manchmal ist es aber trotzden sinnvoll
# einen zu verwenden. In Python kann man damit beispielsweise sicherstellen, dass das Programm 
# immer weiter läuft. Setze infinite loops aber mit Bedacht ein. 

# TODO:
# 1. Schreibe einen while loop, der den Wert einer Variable als condition verwendet. Setze eine 
# maximale Größe für den Wert. Zähle den Wert im body des loops hoch. Lass dir den Wert der 
# Variable mit print() in die Konsole ausgeben. Was siehst du?
# 2. Mache das selbe wie bei 1., aber probiere andere Datentypen für die counter Variable. Was 
# siehst du? 
